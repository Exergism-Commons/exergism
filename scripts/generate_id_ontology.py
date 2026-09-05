#!/usr/bin/env python3
"""Generate the next Exergism ontology projection under id.exergism.org.

This entrypoint deliberately leaves the historical generator implementation and
released artifacts untouched. It reuses the canonical generator with the
namespace selected for the next canonical Exergism release.
"""

from __future__ import annotations

import generate_ontology


ID_NAMESPACE = "https://id.exergism.org/exergism#"


def main() -> None:
    generate_ontology.BASE_IRI = ID_NAMESPACE
    generate_ontology.main()


if __name__ == "__main__":
    main()
