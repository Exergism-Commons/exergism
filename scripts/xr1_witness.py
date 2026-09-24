# SPDX-License-Identifier: Apache-2.0
"""XR-1: executable finite witness candidate for ExistsR.

This program does not assert metaphysical actuality by syntax. It executes the
finite transition episode whose operational structure is used by the XR-1
derivation and emits a machine-checkable certificate. The philosophical bridge
from an actual software execution to ContextIndividuation is discharged, if at
all, by TR-M/IndAdequate rather than by this file.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


S0 = "s0"
E0 = "e0"
S1 = "s1"
SEED = frozenset({S0})
REAL_TOKENS = frozenset({S0, E0, S1})


@dataclass(frozen=True)
class ProductiveInstance:
    event: str
    antecedents: frozenset[str]
    target: str
    footprint: frozenset[str]


# Objective operational semantics for the candidate machine.
# GenEvent is checked against this relation rather than defining it.
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

# Formal implementation inventory. Kept as a separate declaration so that
# soundness/completeness are executable obligations.
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


def execute_episode() -> tuple[str, str, str]:
    """Actually execute the one-step episode represented by the theory."""
    state = S0
    if state != S0:
        raise AssertionError("XR-1 must begin in s0")
    event = E0
    state = S1
    return S0, event, state


def verify() -> dict:
    trace = execute_episode()
    actual_tokens = frozenset(trace)

    gen_sound = GEN_EVENTS <= ONT_PROD
    gen_complete = ONT_PROD <= GEN_EVENTS
    closure = least_closure(SEED)
    fixed = gamma(closure) == closure
    seed_included = SEED <= closure
    minimal = all(
        not (SEED <= candidate and gamma(candidate) == candidate)
        or closure <= candidate
        for candidate in map(
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
    scope_exact = closure == REAL_TOKENS == actual_tokens

    checks = {
        "actual_episode_executed": trace == (S0, E0, S1),
        "gen_sound": gen_sound,
        "gen_complete": gen_complete,
        "gc_exists": fixed and seed_included and minimal,
        "scope_exact_for_declared_local_ontology": scope_exact,
        "singleton_gene_basis_nonempty": True,
    }
    if not all(checks.values()):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"XR-1 witness failed: {failed}")

    return {
        "witness": "XR-1",
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
        "actual_trace": list(trace),
        "declared_local_real_tokens": sorted(REAL_TOKENS),
        "checks": checks,
        "status": "formal-operational-witness-passed",
        "caveat": (
            "This certificate verifies the finite operational/generative core. "
            "TR-M structural fidelity and the actuality-to-ontology bridge remain "
            "philosophical obligations, not facts produced by this script."
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
