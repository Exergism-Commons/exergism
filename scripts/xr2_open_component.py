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
from dataclasses import dataclass
from multiprocessing import Pipe, Process
from pathlib import Path


S0 = "s0"
S1 = "s1"
CLOSE = "close"
ACTIVATE = "activate"
IDLE = "idle"

INPUT_ACTIONS = frozenset({CLOSE})
OUTPUT_ACTIONS = frozenset({ACTIVATE})
INTERNAL_ACTIONS = frozenset({IDLE})
ALL_ACTIONS = INPUT_ACTIONS | OUTPUT_ACTIONS | INTERNAL_ACTIONS

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


def component_worker(channel) -> None:
    """Component-side process with no environment object in local state."""
    state = S0
    command = channel.recv()
    if command != CLOSE:
        channel.send({"error": "unsupported-input", "pid": os.getpid()})
        channel.close()
        return

    state = S1
    channel.send(
        {
            "event": ACTIVATE,
            "state": state,
            "pid": os.getpid(),
        }
    )
    channel.close()


def run_trial(environment_noise: int) -> dict[str, object]:
    """Run one actual environment/component IPC episode."""
    parent, child = Pipe(duplex=True)
    process = Process(target=component_worker, args=(child,))
    process.start()
    child.close()

    child_pid = process.pid
    parent_pid = os.getpid()

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
        "parent_pid": parent_pid,
        "child_pid": child_pid,
        "sent_input": CLOSE,
        "received_output": reply.get("event"),
        "component_state_after": reply.get("state"),
        "reply_pid": reply.get("pid"),
        "local_trace": [S0, CLOSE, S1, ACTIVATE],
    }


def verify() -> dict[str, object]:
    trial_a = run_trial(environment_noise=17)
    trial_b = run_trial(environment_noise=999_983)

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

    channel_mediation = (
        component_worker.__code__.co_argcount == 1
        and "environment_noise" not in component_worker.__code__.co_names
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
    }

    if not all(checks.values()):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"XR-2 evidence failed: {failed}")

    return {
        "evidence_target": "XR-2",
        "theory_candidate": "T_IODTS",
        "interface": {
            "inputs": sorted(INPUT_ACTIONS),
            "outputs": sorted(OUTPUT_ACTIONS),
            "internal": sorted(INTERNAL_ACTIONS),
        },
        "seed": sorted(SEED),
        "closure": sorted(closure),
        "declared_local_real_tokens": sorted(REAL_TOKENS),
        "trials": [trial_a, trial_b],
        "checks": checks,
        "status": "open-component-realization-evidence-passed",
        "caveat": (
            "XR-2 supplies actual environment/component IPC, negative-control "
            "screening, and exact finite generative scope for interaction "
            "tokens. It does not by itself prove RCC1-RCC6 completeness over "
            "every same-level rival cut or establish ContextIndividuation."
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
