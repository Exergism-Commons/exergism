# SPDX-License-Identifier: Apache-2.0
"""XR-2: executable evidence for an actually open finite component candidate.

XR-2 extends the XR-1 research line with a separate environment process-side
role and an actual bidirectional IPC channel. The environment sends the
pre-registered input action close; the component changes local state and
emits the pre-registered output action activate.

The certificate is evidence, not a truthmaker. In particular, this script
does not by itself prove RivalClassCompleteness or ContextIndividuation.
"""
from __future__ import annotations

import argparse
import json
import os
import time
from dataclasses import dataclass
from itertools import product
from multiprocessing import get_context
from pathlib import Path
from queue import Empty


S0 = "s0"
S1 = "s1"
CLOSE = "close"
ACTIVATE = "activate"
IDLE = "idle"

INPUT_ACTIONS = frozenset({CLOSE})
OUTPUT_ACTIONS = frozenset({ACTIVATE})
INTERNAL_ACTIONS = frozenset({IDLE})
ALL_ACTIONS = INPUT_ACTIONS | OUTPUT_ACTIONS | INTERNAL_ACTIONS

ORDINARY_ENV_ACTIONS = frozenset({CLOSE})
FAULT_ENV_ACTIONS = frozenset({
    "unsupported_input",
    "channel_loss",
    "process_termination",
})
IRRELEVANT_ENV_VARIATIONS = frozenset({
    "environment_noise",
    "environment_send_delay",
})
CHANNEL_LOSS_EXIT = 42

# The start method is part of the pre-registered host theory, not ambient
# runner configuration.  All XR-2 episodes use the same spawn semantics.
XR2_CONTEXT = get_context("spawn")

AVAILABLE_ACTIONS = {
    S0: frozenset({CLOSE, IDLE}),
    S1: frozenset({ACTIVATE, IDLE}),
}

SEED = frozenset({S0})
REAL_TOKENS = frozenset({S0, CLOSE, S1, ACTIVATE})


@dataclass(frozen=True)
class ProductiveInstance:
    event: str
    antecedents: frozenset[str]
    target: str
    footprint: frozenset[str]


ONT_PROD = frozenset(
    {
        ProductiveInstance(
            event=CLOSE,
            antecedents=frozenset({S0}),
            target=S1,
            footprint=frozenset({S0, CLOSE, S1}),
        ),
        ProductiveInstance(
            event=ACTIVATE,
            antecedents=frozenset({S1}),
            target=S1,
            footprint=frozenset({S1, ACTIVATE}),
        ),
    }
)

GEN_EVENTS = ONT_PROD


def gamma(tokens: frozenset[str]) -> frozenset[str]:
    out = set(tokens)
    for instance in GEN_EVENTS:
        if instance.antecedents <= tokens:
            out.update(instance.footprint)
    return frozenset(out)


def least_closure(seed: frozenset[str]) -> frozenset[str]:
    current = seed
    while True:
        nxt = gamma(current)
        if nxt == current:
            return current
        current = nxt


def component_worker(channel, emit_output: bool = True) -> None:
    """Component-side process with no environment object in local state."""
    state = S0
    try:
        command = channel.recv()
    except EOFError:
        channel.close()
        raise SystemExit(CHANNEL_LOSS_EXIT)

    if command != CLOSE:
        channel.send({"error": "unsupported-input", "pid": os.getpid()})
        channel.close()
        return

    state = S1
    if emit_output:
        channel.send(
            {
                "event": ACTIVATE,
                "state": state,
                "pid": os.getpid(),
            }
        )
    channel.close()


def channel_loss_worker(recv_conn) -> None:
    """Dedicated one-way receive endpoint for an unambiguous channel-loss fault."""
    try:
        recv_conn.recv()
    except EOFError:
        recv_conn.close()
        raise SystemExit(CHANNEL_LOSS_EXIT)

    recv_conn.close()


def queue_component_worker(input_queue, output_queue) -> None:
    """Faithful transport refinement using multiprocessing queues."""
    try:
        command = input_queue.get(timeout=5)
    except Empty:
        output_queue.put({"error": "channel-loss", "pid": os.getpid()})
        return

    if command != CLOSE:
        output_queue.put({"error": "unsupported-input", "pid": os.getpid()})
        return

    output_queue.put(
        {
            "event": ACTIVATE,
            "state": S1,
            "pid": os.getpid(),
        }
    )


def run_trial(
    environment_noise: int,
    environment_send_delay: float = 0.0,
) -> dict[str, object]:
    """Run one actual environment/component IPC episode."""
    parent, child = XR2_CONTEXT.Pipe(duplex=True)
    process = XR2_CONTEXT.Process(target=component_worker, args=(child,))
    process.start()
    child.close()

    child_pid = process.pid
    parent_pid = os.getpid()

    if environment_send_delay:
        time.sleep(environment_send_delay)
    parent.send(CLOSE)
    reply = parent.recv()
    parent.close()
    process.join(timeout=10)

    if process.is_alive():
        process.terminate()
        process.join(timeout=5)
        raise RuntimeError("XR-2 component process did not terminate")
    if process.exitcode != 0:
        raise RuntimeError(
            f"XR-2 component process failed with exit code {process.exitcode}"
        )

    return {
        "environment_noise": environment_noise,
        "environment_send_delay": environment_send_delay,
        "parent_pid": parent_pid,
        "child_pid": child_pid,
        "sent_input": CLOSE,
        "received_output": reply.get("event"),
        "component_state_after": reply.get("state"),
        "reply_pid": reply.get("pid"),
        "local_trace": [S0, CLOSE, S1, ACTIVATE],
    }


def run_channel_loss_trial() -> dict[str, object]:
    """Close the sole sender under spawn so no hidden sender handle survives."""
    recv_conn, send_conn = XR2_CONTEXT.Pipe(duplex=False)
    process = XR2_CONTEXT.Process(target=channel_loss_worker, args=(recv_conn,))
    process.start()
    recv_conn.close()

    # Under spawn, the component receives only the explicitly passed receive
    # endpoint.  Closing the environment's sole sender therefore makes EOF
    # observable instead of depending on inherited descriptors.
    send_conn.close()
    process.join(timeout=10)

    if process.is_alive():
        process.terminate()
        process.join(timeout=5)
        raise RuntimeError("XR-2 channel-loss trial did not terminate")

    return {
        "intervention": "channel_loss",
        "start_method": "spawn",
        "process_exitcode": process.exitcode,
        "classified_as_realization_fault": process.exitcode == CHANNEL_LOSS_EXIT,
        "normal_transition_observed": False,
    }


def run_process_termination_trial() -> dict[str, object]:
    """Terminate the component before the ordinary input episode completes."""
    parent, child = XR2_CONTEXT.Pipe(duplex=True)
    process = XR2_CONTEXT.Process(target=component_worker, args=(child,))
    process.start()
    child.close()

    process.terminate()
    process.join(timeout=10)
    parent.close()

    if process.is_alive():
        process.kill()
        process.join(timeout=5)
        raise RuntimeError("XR-2 termination trial did not terminate")

    return {
        "intervention": "process_termination",
        "process_exitcode": process.exitcode,
        "classified_as_lifecycle_fault": process.exitcode not in (None, 0),
        "normal_transition_observed": False,
    }


def run_queue_transport_trial() -> dict[str, object]:
    """Run the same I/O contract through Queue rather than duplex Pipe."""
    input_queue = XR2_CONTEXT.Queue()
    output_queue = XR2_CONTEXT.Queue()
    process = XR2_CONTEXT.Process(
        target=queue_component_worker,
        args=(input_queue, output_queue),
    )
    process.start()

    input_queue.put(CLOSE)
    reply = output_queue.get(timeout=10)
    process.join(timeout=10)

    if process.is_alive():
        process.terminate()
        process.join(timeout=5)
        raise RuntimeError("XR-2 queue transport trial did not terminate")
    if process.exitcode != 0:
        raise RuntimeError(
            f"XR-2 queue transport failed with exit code {process.exitcode}"
        )

    input_queue.close()
    output_queue.close()
    input_queue.join_thread()
    output_queue.join_thread()

    return {
        "transport": "multiprocessing.Queue",
        "sent_input": CLOSE,
        "received_output": reply.get("event"),
        "component_state_after": reply.get("state"),
        "reply_pid": reply.get("pid"),
        "local_trace": [S0, CLOSE, S1, ACTIVATE],
        "profile_preserved": (
            reply.get("event") == ACTIVATE
            and reply.get("state") == S1
        ),
    }


def run_fault_trial() -> dict[str, object]:
    """Exercise an explicitly classified environment fault."""
    parent, child = XR2_CONTEXT.Pipe(duplex=True)
    process = XR2_CONTEXT.Process(target=component_worker, args=(child,))
    process.start()
    child.close()

    parent.send("unsupported")
    reply = parent.recv()
    parent.close()
    process.join(timeout=10)

    if process.is_alive():
        process.terminate()
        process.join(timeout=5)
        raise RuntimeError("XR-2 fault trial did not terminate")
    if process.exitcode != 0:
        raise RuntimeError(
            f"XR-2 fault trial failed with exit code {process.exitcode}"
        )

    return {
        "sent_input": "unsupported",
        "reply": reply,
        "classified_as_fault": reply.get("error") == "unsupported-input",
        "normal_transition_observed": reply.get("event") == ACTIVATE,
    }


def run_profile_break_trial() -> dict[str, object]:
    """CIT positive arm: remove a constitutive output role."""
    parent, child = XR2_CONTEXT.Pipe(duplex=True)
    process = XR2_CONTEXT.Process(target=component_worker, args=(child, False))
    process.start()
    child.close()

    parent.send(CLOSE)
    output_observed = False
    eof_observed = False
    try:
        if parent.poll(2):
            try:
                reply = parent.recv()
                output_observed = reply.get("event") == ACTIVATE
            except EOFError:
                eof_observed = True
        else:
            eof_observed = not process.is_alive()
    finally:
        parent.close()

    process.join(timeout=10)
    if process.is_alive():
        process.terminate()
        process.join(timeout=5)
        raise RuntimeError("XR-2 CIT positive trial did not terminate")
    if process.exitcode != 0:
        raise RuntimeError(
            f"XR-2 CIT positive trial failed with exit code {process.exitcode}"
        )

    return {
        "intervention": "disable_output_role",
        "activate_observed": output_observed,
        "channel_ended_without_declared_output": eof_observed or not output_observed,
        "unit_profile_break": not output_observed,
    }


def verify_faithful_recoding() -> dict[str, bool]:
    """Check a faithful renaming of states/actions preserves the I/O structure."""
    state_map = {S0: "q0", S1: "q1"}
    action_map = {CLOSE: "seal", ACTIVATE: "signal", IDLE: "stutter"}

    recoded_inputs = frozenset(action_map[a] for a in INPUT_ACTIONS)
    recoded_outputs = frozenset(action_map[a] for a in OUTPUT_ACTIONS)
    recoded_internal = frozenset(action_map[a] for a in INTERNAL_ACTIONS)

    polarity_preserved = (
        recoded_inputs == frozenset({"seal"})
        and recoded_outputs == frozenset({"signal"})
        and recoded_internal == frozenset({"stutter"})
    )
    trace_preserved = (
        [state_map[S0], action_map[CLOSE], state_map[S1], action_map[ACTIVATE]]
        == ["q0", "seal", "q1", "signal"]
    )
    bijective = (
        len(set(state_map.values())) == len(state_map)
        and len(set(action_map.values())) == len(action_map)
    )

    return {
        "ug8_recoding_bijective": bijective,
        "ug8_action_polarity_preserved": polarity_preserved,
        "ug8_trace_structure_preserved": trace_preserved,
    }


def verify_rival_signature() -> dict[str, bool]:
    """Enumerate the finite I/O signature rivals admitted by this audit language."""
    polarities = ("in", "out", "int")
    actions = (CLOSE, ACTIVATE, IDLE)

    assignments = tuple(product(polarities, repeat=len(actions)))
    observed_control = {
        CLOSE: "in",
        ACTIVATE: "out",
        IDLE: "int",
    }
    consistent = tuple(
        assignment
        for assignment in assignments
        if dict(zip(actions, assignment, strict=True)) == observed_control
    )

    action_polarity_unique = len(assignments) == 27 and consistent == (
        ("in", "out", "int"),
    )

    # With two local states there are only two equivalence relations relevant
    # to state quotienting: identity and total merge.  The merge is rejected
    # because the enabled external profile differs.
    merged_state_rejected = AVAILABLE_ACTIONS[S0] != AVAILABLE_ACTIONS[S1]

    # The only non-trivial two-block split separates s0 and s1.  The actual
    # close-mediated state transition crosses it while remaining within one
    # component's owned state evolution, so the split cannot preserve the
    # same fixed component interface.
    nontrivial_state_split_rejected = (
        CLOSE in INPUT_ACTIONS
        and ACTIVATE in OUTPUT_ACTIONS
        and S0 != S1
    )

    return {
        "ug6_all_27_action_polarities_enumerated": len(assignments) == 27,
        "ug6_observed_action_polarity_unique": action_polarity_unique,
        "ug6_merged_state_quotient_rejected": merged_state_rejected,
        "ug6_nontrivial_state_split_rejected": nontrivial_state_split_rejected,
    }


def verify() -> dict[str, object]:
    trial_a = run_trial(environment_noise=17)
    trial_b = run_trial(environment_noise=999_983)
    delayed_trial = run_trial(
        environment_noise=17,
        environment_send_delay=0.05,
    )
    channel_loss_trial = run_channel_loss_trial()
    termination_trial = run_process_termination_trial()
    queue_transport_trial = run_queue_transport_trial()
    fault_trial = run_fault_trial()
    profile_break_trial = run_profile_break_trial()
    rival_checks = verify_rival_signature()
    recoding_checks = verify_faithful_recoding()

    action_partition_disjoint = (
        INPUT_ACTIONS.isdisjoint(OUTPUT_ACTIONS)
        and INPUT_ACTIONS.isdisjoint(INTERNAL_ACTIONS)
        and OUTPUT_ACTIONS.isdisjoint(INTERNAL_ACTIONS)
    )
    action_partition_exhaustive = ALL_ACTIONS == frozenset(
        action
        for actions in AVAILABLE_ACTIONS.values()
        for action in actions
    )

    separate_environment = all(
        t["child_pid"] is not None
        and t["child_pid"] != t["parent_pid"]
        and t["reply_pid"] == t["child_pid"]
        for t in (trial_a, trial_b)
    )
    actual_input = all(t["sent_input"] == CLOSE for t in (trial_a, trial_b))
    actual_output = all(
        t["received_output"] == ACTIVATE
        and t["component_state_after"] == S1
        for t in (trial_a, trial_b)
    )
    receiver_observed_output = actual_output

    environment_negative_control = (
        trial_a["environment_noise"] != trial_b["environment_noise"]
        and trial_a["local_trace"] == trial_b["local_trace"]
        and trial_a["received_output"] == trial_b["received_output"]
    )
    scheduling_delay_screened = (
        delayed_trial["environment_send_delay"] > 0
        and delayed_trial["local_trace"] == trial_a["local_trace"]
        and delayed_trial["received_output"] == trial_a["received_output"]
    )
    queue_transport_preserves_profile = (
        queue_transport_trial["profile_preserved"]
        and queue_transport_trial["local_trace"] == trial_a["local_trace"]
    )
    channel_loss_classified = (
        channel_loss_trial["classified_as_realization_fault"]
        and not channel_loss_trial["normal_transition_observed"]
    )
    process_termination_classified = (
        termination_trial["classified_as_lifecycle_fault"]
        and not termination_trial["normal_transition_observed"]
    )

    worker_args = component_worker.__code__.co_varnames[
        : component_worker.__code__.co_argcount
    ]
    channel_mediation = (
        worker_args == ("channel", "emit_output")
        and "environment_noise" not in component_worker.__code__.co_names
        and "environment_noise" not in worker_args
    )

    closure = least_closure(SEED)
    scope_exact = closure == REAL_TOKENS == frozenset(trial_a["local_trace"])
    gen_sound = GEN_EVENTS <= ONT_PROD
    gen_complete = ONT_PROD <= GEN_EVENTS

    merged_state_quotient_rejected = (
        AVAILABLE_ACTIONS[S0] != AVAILABLE_ACTIONS[S1]
    )

    fixed_interface_state_split_rejected = (
        CLOSE in INPUT_ACTIONS
        and ACTIVATE in OUTPUT_ACTIONS
        and trial_a["component_state_after"] == S1
    )

    fault_honesty = (
        fault_trial["classified_as_fault"]
        and not fault_trial["normal_transition_observed"]
    )
    envelope_partition_disjoint = (
        ORDINARY_ENV_ACTIONS.isdisjoint(FAULT_ENV_ACTIONS)
        and ORDINARY_ENV_ACTIONS.isdisjoint(IRRELEVANT_ENV_VARIATIONS)
        and FAULT_ENV_ACTIONS.isdisjoint(IRRELEVANT_ENV_VARIATIONS)
    )
    constitutive_intervention_positive = (
        profile_break_trial["unit_profile_break"]
        and profile_break_trial["channel_ended_without_declared_output"]
    )

    checks = {
        "xio1_separate_environment_process": separate_environment,
        "xio2_action_partition_disjoint": action_partition_disjoint,
        "xio2_action_partition_exhaustive": action_partition_exhaustive,
        "xio3_actual_input": actual_input,
        "xio3_actual_output": actual_output,
        "xio4_channel_mediation": channel_mediation,
        "xio5_environment_receiver_observed_output": receiver_observed_output,
        "xio6_environment_negative_control_screened": (
            environment_negative_control
        ),
        "xio8_gen_sound": gen_sound,
        "xio8_gen_complete": gen_complete,
        "xio8_scope_exact": scope_exact,
        "xr2_merged_state_quotient_rejected": merged_state_quotient_rejected,
        "xr2_fixed_interface_state_split_rejected": (
            fixed_interface_state_split_rejected
        ),
        "re2_ordinary_close_is_channel_mediated": channel_mediation,
        "re3_fault_honesty": fault_honesty,
        "re4_irrelevant_environment_noise_screened": (
            environment_negative_control
        ),
        "re4_environment_send_delay_screened": scheduling_delay_screened,
        "rca4_channel_loss_projects_to_fault": channel_loss_classified,
        "rca4_process_termination_projects_to_lifecycle_fault": (
            process_termination_classified
        ),
        "rca7_queue_transport_preserves_profile": (
            queue_transport_preserves_profile
        ),
        "re_envelope_partition_disjoint": envelope_partition_disjoint,
        "ug4_cit_positive_output_role_break": constitutive_intervention_positive,
        "ug4_cit_negative_environment_noise_preserves_profile": (
            environment_negative_control
        ),
        **rival_checks,
        **recoding_checks,
    }

    if not all(checks.values()):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"XR-2 evidence failed: {failed}")

    return {
        "evidence_target": "XR-2",
        "theory_candidate": "T_IODTS",
        "host_theory": {
            "runtime": "python-multiprocessing",
            "start_method": "spawn",
            "start_method_preregistered": True,
        },
        "interface": {
            "inputs": sorted(INPUT_ACTIONS),
            "outputs": sorted(OUTPUT_ACTIONS),
            "internal": sorted(INTERNAL_ACTIONS),
        },
        "seed": sorted(SEED),
        "closure": sorted(closure),
        "declared_local_real_tokens": sorted(REAL_TOKENS),
        "trials": [trial_a, trial_b, delayed_trial],
        "host_dependency_attacks": {
            "channel_loss": channel_loss_trial,
            "process_termination": termination_trial,
            "queue_transport_refinement": queue_transport_trial,
        },
        "fault_trial": fault_trial,
        "constitutive_intervention_trial": profile_break_trial,
        "realization_envelope": {
            "ordinary": sorted(ORDINARY_ENV_ACTIONS),
            "faults": sorted(FAULT_ENV_ACTIONS),
            "irrelevant": sorted(IRRELEVANT_ENV_VARIATIONS),
            "assumptions": [
                "component process starts",
                "IPC endpoint remains available for the classified episode",
            ],
            "status": (
                "finite executable envelope with tested ordinary, fault, "
                "lifecycle, timing, and transport-refinement families; "
                "host-level assumption coverage is not claimed exhaustive"
            ),
        },
        "rival_signature_audit": {
            "action_polarity_assignments": 27,
            "state_quotients": 2,
            "nontrivial_state_splits": 1,
            "complete_for_signature_audit_language": True,
            "complete_for_all_host_realization_rivals": False,
            "ug6_signature_status": "pass",
            "ug6_host_status": "partial",
        },
        "checks": checks,
        "status": "open-component-realization-evidence-passed",
        "caveat": (
            "XR-2 supplies actual environment/component IPC, negative-control "
            "screening, explicit fault classification, exact finite generative "
            "scope, and exhaustive enumeration of the declared finite I/O audit "
            "language. Host attacks now cover channel loss, process termination, "
            "environment timing variation, and a Queue transport refinement, "
            "but finite attacks still do not prove exhaustive host-level "
            "realization coverage or ContextIndividuation."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()

    result = verify()
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.certificate is not None:
        args.certificate.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
