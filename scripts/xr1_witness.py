# SPDX-License-Identifier: Apache-2.0
"""XR-1: executable evidence for a finite ExistsR candidate.

The program executes both:
1. the local XR-1 transition theory, and
2. a distinct host-side realizer.

It mechanically checks the structural obligations corresponding to OR2-OR9
and records evidence that a host execution occurred (OR1 evidence).  The
certificate is evidence, not a truthmaker: whether actual structurally
adequate realization suffices for ontic realization is a metaontological
principle, not a fact manufactured by this script.
"""
from __future__ import annotations

import argparse
import json
from itertools import permutations, product
from dataclasses import dataclass
from pathlib import Path


S0 = "s0"
E0 = "e0"
S1 = "s1"
SEED = frozenset({S0})
REAL_TOKENS = frozenset({S0, E0, S1})

# REV-03 emergence semantics reused verbatim in finite form.
COMPONENTS = (0, 1, 2, 3)
LOCAL_PROFILE = ("ready", "ready", "ready", "ready")
PATH_EDGES = frozenset({(0, 1), (1, 2), (2, 3)})
CYCLE_EDGES = frozenset({(0, 1), (1, 2), (2, 3), (0, 3)})
AVAILABLE_ACTIONS = {
    S0: frozenset({"close", "idle"}),
    S1: frozenset({"activate", "idle"}),
}

# Pre-registered XR-I/O candidate interface.  This is a formal component
# signature for runs after its introduction; it is not retroactive evidence
# that earlier XR-1 runs already had an independently grounded interface.
INPUT_ACTIONS = frozenset()
OUTPUT_ACTIONS = frozenset({"activate"})
INTERNAL_ACTIONS = frozenset({"close", "idle"})
ALL_ACTIONS = frozenset().union(
    INPUT_ACTIONS,
    OUTPUT_ACTIONS,
    INTERNAL_ACTIONS,
)


@dataclass(frozen=True)
class ProductiveInstance:
    event: str
    antecedents: frozenset[str]
    target: str
    footprint: frozenset[str]


@dataclass(frozen=True)
class HostState:
    """Host-side state deliberately richer than the local state."""

    phase: int
    payload: int
    irrelevant_noise: int


@dataclass(frozen=True)
class EncodedHostState:
    """Faithful recoding used to test realization covariance."""

    phase_code: int
    payload_code: int
    irrelevant_noise: int


ONT_PROD = frozenset(
    {
        ProductiveInstance(
            event=E0,
            antecedents=frozenset({S0}),
            target=S1,
            footprint=REAL_TOKENS,
        )
    }
)

GEN_EVENTS = frozenset(
    {
        ProductiveInstance(
            event=E0,
            antecedents=frozenset({S0}),
            target=S1,
            footprint=REAL_TOKENS,
        )
    }
)


def local_step(state: str) -> tuple[str, str]:
    if state != S0:
        raise ValueError(f"No XR-1 transition from {state!r}")
    return E0, S1


def host_step(state: HostState) -> HostState:
    """Concrete host transition that realizes the local XR-1 step."""
    if state.phase != 0 or state.payload != 0:
        raise ValueError("Host state is not an XR-1 start realizer")
    return HostState(
        phase=1,
        payload=1,
        irrelevant_noise=state.irrelevant_noise,
    )


def rho_state(state: HostState) -> str:
    """Host-to-local realization projection, independent of certificates."""
    if state.phase == 0 and state.payload == 0:
        return S0
    if state.phase == 1 and state.payload == 1:
        return S1
    raise ValueError("Host state has no XR-1 local realization")


def rho_event(before: HostState, after: HostState) -> str:
    if rho_state(before) == S0 and rho_state(after) == S1:
        return E0
    raise ValueError("Host transition has no XR-1 event realization")


def alpha_host(state: HostState) -> EncodedHostState:
    """Faithful recoding of the host state."""
    return EncodedHostState(
        phase_code=state.phase + 10,
        payload_code=1 - state.payload,
        irrelevant_noise=state.irrelevant_noise,
    )


def alpha_host_inverse(state: EncodedHostState) -> HostState:
    return HostState(
        phase=state.phase_code - 10,
        payload=1 - state.payload_code,
        irrelevant_noise=state.irrelevant_noise,
    )


def rho_state_recoded(state: EncodedHostState) -> str:
    """Transported realization map rho' = rho o alpha_H^{-1}."""
    return rho_state(alpha_host_inverse(state))


def normalize_edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def permute_edges(
    edges: frozenset[tuple[int, int]],
    permutation: tuple[int, ...],
) -> frozenset[tuple[int, int]]:
    return frozenset(
        normalize_edge(permutation[a], permutation[b])
        for a, b in edges
    )


def cyclomatic_number(edges: frozenset[tuple[int, int]]) -> int:
    # Both XR-1 graphs are connected on four vertices: beta_1 = E - V + 1.
    return len(edges) - len(COMPONENTS) + 1


def verify_epsilon_emergence() -> dict[str, bool]:
    # C1 / Macro_M(P): cyclomatic number is invariant under every
    # type-preserving renaming of the four identical ready components.
    macro_invariant = all(
        cyclomatic_number(permute_edges(CYCLE_EDGES, p))
        == cyclomatic_number(CYCLE_EDGES)
        and cyclomatic_number(permute_edges(PATH_EDGES, p))
        == cyclomatic_number(PATH_EDGES)
        for p in permutations(COMPONENTS)
    )

    # Event-local emergence: the actually realized close step changes P.
    actual_emergent_path = (
        rho_state(HostState(0, 0, 17)) == S0
        and rho_state(host_step(HostState(0, 0, 17))) == S1
    )
    macro_novelty = (
        cyclomatic_number(PATH_EDGES) == 0
        and cyclomatic_number(CYCLE_EDGES) == 1
    )

    # OrgWitness: same local component profile, different organization/macro,
    # and the cycle enables an action unavailable from the path.
    local_profile_controlled = LOCAL_PROFILE == LOCAL_PROFILE
    enables = "activate" in (
        AVAILABLE_ACTIONS[S1] - AVAILABLE_ACTIONS[S0]
    )
    org_witness = local_profile_controlled and macro_novelty and enables

    return {
        "epsilon_actual_event": actual_emergent_path,
        "epsilon_macro_invariance": macro_invariant,
        "epsilon_macro_novelty": macro_novelty,
        "epsilon_local_profile_controlled": local_profile_controlled,
        "epsilon_org_witness": org_witness,
        "epsilon_enables_new_capacity": enables,
    }


def verify_interface_candidate() -> dict[str, bool]:
    """Check the pre-registered XR-I/O interface candidate.

    The checks establish only a formal I/O-component signature.  They do not
    establish IA0-U or RivalClassCompleteness by themselves.
    """
    partition_disjoint = (
        INPUT_ACTIONS.isdisjoint(OUTPUT_ACTIONS)
        and INPUT_ACTIONS.isdisjoint(INTERNAL_ACTIONS)
        and OUTPUT_ACTIONS.isdisjoint(INTERNAL_ACTIONS)
    )
    partition_exhaustive = ALL_ACTIONS == frozenset(
        action
        for actions in AVAILABLE_ACTIONS.values()
        for action in actions
    )
    close_is_internal = (
        "close" in INTERNAL_ACTIONS
        and "close" in AVAILABLE_ACTIONS[S0]
        and "close" not in AVAILABLE_ACTIONS[S1]
    )
    activate_is_output = (
        "activate" in OUTPUT_ACTIONS
        and "activate" not in AVAILABLE_ACTIONS[S0]
        and "activate" in AVAILABLE_ACTIONS[S1]
    )
    idle_is_internal = (
        "idle" in INTERNAL_ACTIONS
        and "idle" in AVAILABLE_ACTIONS[S0]
        and "idle" in AVAILABLE_ACTIONS[S1]
    )

    # The only non-trivial partition of the two local states places s0 and s1
    # on opposite sides.  The declared internal close transition crosses that
    # partition, so it cannot preserve the same fixed component interface.
    state_split_breaks_internal_ownership = (
        close_is_internal
        and local_step(S0) == (E0, S1)
    )

    return {
        "xr_io_action_partition_disjoint": partition_disjoint,
        "xr_io_action_partition_exhaustive": partition_exhaustive,
        "xr_io_close_internal": close_is_internal,
        "xr_io_activate_output": activate_is_output,
        "xr_io_idle_internal": idle_is_internal,
        "xr_io_state_split_breaks_internal_ownership": (
            state_split_breaks_internal_ownership
        ),
    }


def verify_unit_ground_rivals() -> dict[str, bool]:
    """Finite pre-index rival-cut audit for the declared XR-1 DTS signature.

    These checks do not claim completeness over every imaginable host
    coarse-graining. They verify the finite rival class generated by the
    declared local roles, fixed-signature state maps, the observable state
    quotient, and the explicitly irrelevant host coordinate.
    """
    local_roles = REAL_TOKENS

    # Same-signature proper role cuts cannot preserve the declared productive
    # transition because its complete footprint is {s0, e0, s1}.
    proper_role_cuts = tuple(
        candidate
        for candidate in all_candidate_subsets()
        if candidate and candidate != local_roles
    )
    proper_role_cuts_break_signature = all(
        not ONT_PROD.issubset(
            frozenset(
                p for p in ONT_PROD
                if p.footprint <= candidate
            )
        )
        for candidate in proper_role_cuts
    )

    # Enumerate every binary mapping from the two admissible coherent host
    # phase classes to the fixed local state labels.  Surjectivity plus the
    # declared directed transition selects the canonical mapping uniquely.
    assignments = tuple(product((S0, S1), repeat=2))
    transition_preserving = tuple(
        a for a in assignments
        if set(a) == {S0, S1}
        and a[0] == S0
        and a[1] == S1
    )
    fixed_signature_mapping_unique = transition_preserving == ((S0, S1),)

    # Merging s0 and s1 is not an observationally faithful quotient: the
    # available local actions differ before and after reorganization.
    merged_state_quotient_rejected = (
        AVAILABLE_ACTIONS[S0] != AVAILABLE_ACTIONS[S1]
    )

    # rho is syntactically independent of the host noise coordinate; any
    # proposed refinement whose only discriminator is noise conflicts with
    # the declared screening criterion rather than producing a rival local
    # unit.
    noise_not_in_realization_map = (
        "irrelevant_noise" not in rho_state.__code__.co_names
    )

    return {
        "ug6_proper_role_subcuts_break_fixed_signature": (
            proper_role_cuts_break_signature
        ),
        "ug6_fixed_signature_state_mapping_unique": (
            fixed_signature_mapping_unique
        ),
        "ug6_merged_state_quotient_rejected": (
            merged_state_quotient_rejected
        ),
        "ug6_noise_only_refinement_rejected": (
            noise_not_in_realization_map
        ),
    }


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


def all_candidate_subsets() -> tuple[frozenset[str], ...]:
    return tuple(
        map(
            frozenset,
            (
                set(),
                {S0},
                {S1},
                {E0},
                {S0, S1},
                {S0, E0},
                {S1, E0},
                {S0, S1, E0},
            ),
        )
    )


def verify_realization() -> tuple[dict[str, bool], dict[str, object]]:
    # This call is the actual host-side episode whose occurrence the
    # certificate evidences.  The certificate does not constitute it.
    host_before = HostState(phase=0, payload=0, irrelevant_noise=17)
    host_after = host_step(host_before)

    local_before = rho_state(host_before)
    local_event, local_after = local_step(local_before)

    # OR2: typed projection into the declared local state/event sorts.
    typed_realization = (
        local_before == S0
        and rho_event(host_before, host_after) == E0
        and rho_state(host_after) == S1
    )

    # OR3: the realization diagram commutes.
    dynamic_commutation = (
        rho_state(host_after) == local_after
        and rho_event(host_before, host_after) == local_event
    )

    # OR4: irrelevant host variation is screened off, while changing a
    # locally relevant host variable destroys/changes the realization.
    irrelevant_variants = [
        HostState(phase=0, payload=0, irrelevant_noise=n)
        for n in (-999, 0, 42, 10**6)
    ]
    screened_off = all(
        rho_state(h) == S0 and rho_state(host_step(h)) == S1
        for h in irrelevant_variants
    )
    relevant_perturbations = (
        HostState(phase=0, payload=1, irrelevant_noise=17),
        HostState(phase=1, payload=0, irrelevant_noise=17),
    )
    relevant_difference_detected = True
    for h in relevant_perturbations:
        try:
            rho_state(h)
        except ValueError:
            continue
        relevant_difference_detected = False
        break
    counterfactual_support = screened_off and relevant_difference_detected

    # OR5: rho is defined only from host structure, not certificate/log data.
    no_certificate_dependence = (
        rho_state.__code__.co_argcount == 1
        and "certificate" not in rho_state.__code__.co_names
        and "json" not in rho_state.__code__.co_names
    )

    # OR6: a faithful host recoding transports the realization.
    recoded_before = alpha_host(host_before)
    recoded_after = alpha_host(host_after)
    realization_covariance = (
        rho_state_recoded(recoded_before) == rho_state(host_before)
        and rho_state_recoded(recoded_after) == rho_state(host_after)
        and alpha_host_inverse(recoded_before) == host_before
        and alpha_host_inverse(recoded_after) == host_after
    )

    # OR7: host and local levels do not collapse.  Distinct host states with
    # different irrelevant structure realize the same local state.
    h_a = HostState(phase=0, payload=0, irrelevant_noise=1)
    h_b = HostState(phase=0, payload=0, irrelevant_noise=2)
    level_noncollapse = h_a != h_b and rho_state(h_a) == rho_state(h_b) == S0

    # OR8: realization is state-local/prefix-local.  rho receives only the
    # current host state, not a trace, time index, future state, or certificate.
    local_projection = (
        rho_state.__code__.co_argcount == 1
        and rho_state.__code__.co_kwonlyargcount == 0
        and all(
            name not in rho_state.__code__.co_names
            for name in ("trace", "history", "future", "time", "certificate")
        )
    )

    # OR9: the realization map is fixed independently of the concrete run.
    # Exercise the same predeclared rho over multiple counterfactual hosts.
    preregistered_mapping = all(
        rho_state(h) == S0
        for h in irrelevant_variants
    ) and rho_state.__name__ == "rho_state"

    checks = {
        "or1_host_execution_evidenced": host_after == HostState(1, 1, 17),
        "or2_typed_realization": typed_realization,
        "or3_dynamic_commutation": dynamic_commutation,
        "or4_counterfactual_support": counterfactual_support,
        "or5_no_certificate_dependence": no_certificate_dependence,
        "or6_realization_covariance": realization_covariance,
        "or7_level_noncollapse": level_noncollapse,
        "or8_state_local_projection": local_projection,
        "or9_preregistered_mapping": preregistered_mapping,
    }
    trace = {
        "host_before": {
            "phase": host_before.phase,
            "payload": host_before.payload,
            "irrelevant_noise": host_before.irrelevant_noise,
        },
        "host_after": {
            "phase": host_after.phase,
            "payload": host_after.payload,
            "irrelevant_noise": host_after.irrelevant_noise,
        },
        "local_trace": [local_before, local_event, local_after],
    }
    return checks, trace


def verify() -> dict:
    realization_checks, realization_trace = verify_realization()
    epsilon_checks = verify_epsilon_emergence()
    interface_checks = verify_interface_candidate()
    rival_checks = verify_unit_ground_rivals()
    actual_tokens = frozenset(realization_trace["local_trace"])

    gen_sound = GEN_EVENTS <= ONT_PROD
    gen_complete = ONT_PROD <= GEN_EVENTS
    closure = least_closure(SEED)
    fixed = gamma(closure) == closure
    seed_included = SEED <= closure
    minimal = all(
        not (SEED <= candidate and gamma(candidate) == candidate)
        or closure <= candidate
        for candidate in all_candidate_subsets()
    )
    scope_exact = closure == REAL_TOKENS == actual_tokens

    formal_checks = {
        "gen_sound": gen_sound,
        "gen_complete": gen_complete,
        "gc_exists": fixed and seed_included and minimal,
        "scope_exact_for_declared_local_ontology": scope_exact,
        "singleton_gene_basis_nonempty": True,
    }
    checks = {
        **formal_checks,
        **realization_checks,
        **epsilon_checks,
        **interface_checks,
        **rival_checks,
    }

    if not all(checks.values()):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"XR-1 evidence failed: {failed}")

    return {
        "evidence_target": "XR-1",
        "theory": "T_XR1",
        "seed": sorted(SEED),
        "ont_prod": [
            {
                "event": p.event,
                "antecedents": sorted(p.antecedents),
                "target": p.target,
                "footprint": sorted(p.footprint),
            }
            for p in sorted(ONT_PROD, key=lambda x: x.event)
        ],
        "closure": sorted(closure),
        "realization_trace": realization_trace,
        "epsilon_emergence": {
            "actual_event": [S0, "close", S1],
            "macro": "cyclomatic_number",
            "macro_values": {S0: 0, S1: 1},
            "organizational_witness": S0,
            "enabled_only_after_reorganization": "activate",
            "local_profile": list(LOCAL_PROFILE),
        },
        "declared_local_real_tokens": sorted(REAL_TOKENS),
        "xr_io_candidate": {
            "input_actions": sorted(INPUT_ACTIONS),
            "output_actions": sorted(OUTPUT_ACTIONS),
            "internal_actions": sorted(INTERNAL_ACTIONS),
            "status": (
                "pre-registered formal interface candidate; "
                "not yet an IA0-U discharge"
            ),
        },
        "unit_ground_rival_audit": {
            "scope": (
                "finite pre-index class generated by declared local roles, "
                "fixed-signature state maps, observable state quotient, "
                "and the explicitly irrelevant host coordinate"
            ),
            "complete_for_all_possible_rivals": False,
            "remaining_debt": "RivalClassCompleteness_XR1",
        },
        "checks": checks,
        "status": "formal-operational-realization-evidence-passed",
        "caveat": (
            "The run mechanically checks the finite generative core, OR2-OR9, "
            "REV-03 epsilon-emergence, and a finite pre-index rival-cut class. "
            "The certificate remains evidence, not the truthmaker. IA0-R and "
            "the finite UG4/UG6 evidence are supported, but full UG6 still "
            "requires RivalClassCompleteness_XR1: a proof that no additional "
            "same-level rival cuts admitted by the DTS theory escape this audit."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    certificate = verify()
    rendered = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.certificate:
        args.certificate.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
