# Release process

Exergism releases are immutable snapshots of the canonical repository lineage.

## Preconditions

A release may be published only when:

1. `python scripts/validate_repository.py` passes;
2. `ontology.owl` regenerates byte-for-byte from canonical content;
3. canonical IDs and `concept_ref` targets are valid;
4. licensing and governance documents are present;
5. known formal ambiguities are documented rather than silently guessed;
6. adversarial review of the candidate is complete; and
7. `manifest.json` marks the release candidate as `ready`.

## Release identity

A release is identified by all of the following:

- semantic version, e.g. `0.1.0`;
- immutable Git tag, e.g. `v0.1.0`;
- exact Git commit SHA;
- generated `release-manifest.json` containing canonical artifact hashes; and
- source archive checksum.

The Git tag must never be force-moved to different content.

## Release manifest

Generate a manifest from the exact release checkout:

```bash
python scripts/build_release_manifest.py \
  --version 0.1.0 \
  --git-commit "$(git rev-parse HEAD)" \
  --output release-manifest.json
```

The generated manifest is intentionally a release artifact rather than a tracked file because embedding the commit that contains the manifest would create a self-reference problem.

## Automated publication

`.github/workflows/release.yml` runs on `main`. It only publishes when `manifest.json` declares a release `ready` and the corresponding tag does not already exist. It validates the exact commit, generates the release manifest, archives the source tree, creates the immutable tag and publishes the GitHub release assets.

Later changes to `main` do not alter an existing release.
