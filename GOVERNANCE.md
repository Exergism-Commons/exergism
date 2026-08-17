# Exergism governance

## 1. Purpose

Exergism Commons maintains the canonical public development lineage of the **Metafísica emergentista de la liberación (Exergism)**. Governance exists to preserve inspectability, contestability, continuity and freedom to fork; it is not a mechanism for converting administrative control into permanent philosophical authority.

## 2. Canonicality is procedural, not a monopoly on truth

"Canonical" means that a revision belongs to the lineage maintained by this repository. It does not mean that a proposition is true because a maintainer merged it, that forks are illegitimate, or that historical authorship grants perpetual normative authority.

The philosophical system remains open to criticism, falsification attempts, reinterpretation and competing forks under the applicable license.

## 3. Change classes

Changes are reviewed according to their effect:

1. **Mechanical/editorial** — formatting, spelling, metadata, build tooling or representation changes that do not alter philosophical meaning.
2. **Structural/semantic-preserving** — schema, ontology, identifiers, cross-references or publication structure intended to preserve the same philosophical meaning.
3. **Doctrinal/formal** — changes to propositions, definitions, axioms, normative claims, formal variables, formulas, parameter semantics, book architecture or other substantive meaning.

A change must be treated as the higher class whenever reasonable reviewers disagree about whether meaning changes.

## 4. Requirements for doctrinal/formal changes

A doctrinal/formal pull request must make the proposed semantic delta explicit and include:

- the proposition, definition or formal element being changed;
- the reason for the change;
- material arguments or evidence supporting it;
- serious known objections or counterarguments;
- affected canonical nodes/files and downstream dependencies where known; and
- whether the change supersedes, narrows, expands or merely clarifies the prior position.

Hidden doctrinal changes inside migration, formatting, generated output or bulk refactors are not acceptable.

## 5. Anti-capture rules

Repository administrators and maintainers are custodians of this lineage, not owners of the community's ability to study or continue the work.

Accordingly:

- no contribution requires copyright assignment merely to participate;
- public releases remain available under the license under which they were released;
- release tags are immutable records and must not be force-moved to different content;
- the project should remain clonable and reconstructable with open, documented formats;
- no maintainer may use repository control to represent an independently maintained fork as technically invalid merely because it is a fork;
- conflicts of interest relevant to a substantive change should be disclosed in the review record; and
- governance should reduce single-person dependency as independent maintainers emerge rather than entrench it.

## 6. Maintainers

Maintainers may review and merge changes, manage releases and maintain infrastructure. Those operational permissions do not constitute a philosophical veto or a grant of permanent doctrinal authority.

At the initial public stage, administrative access may be concentrated for practical reasons. This is an implementation constraint to be reduced over time, not a normative property of Exergism.

## 7. Releases

A release is an immutable snapshot of the canonical lineage at a particular commit. A later release may revise doctrine, but must not silently rewrite what an earlier release contained.

Every release must pass repository validation and follow `docs/release-process.md`.

## 8. Relationship to downstream applications

Downstream projects such as ECL may pin a specific Exergism release. No downstream legal, political or governance outcome is inferred solely because Exergism contains a concept, relation or numerical analytical result.

ECL governance remains autonomous under ECL's own operative artifacts and procedures.
