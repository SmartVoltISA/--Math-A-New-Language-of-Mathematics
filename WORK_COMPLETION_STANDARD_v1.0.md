# Ω-Math — Work Completion Standard v1.0

## Purpose

This standard defines when a piece of work may be declared complete. It applies to research, mathematics, code, experiments, documentation, synchronization, and repository maintenance.

## Completion rule

Work is **not DONE** merely because the main task has been implemented.

The required sequence is:

`make → write → reread → verify → synchronize → validate → self-contain → declare DONE`

## Mandatory completion checks

After every substantive change:

1. **Make** — perform the requested change.
2. **Write** — persist the actual result in the authoritative artifact.
3. **Reread** — reopen the written artifact after saving.
4. **Verify** — check formulas, definitions, parameters, claims, code paths, and stated results.
5. **Synchronize** — update directly affected indexes, changelogs, references, schemas, and status records.
6. **Validate** — run the relevant tests, consistency checks, or reproducibility checks.
7. **Self-contain** — ensure the result can be understood and reproduced from the artifact itself without relying on the previous conversation.
8. **Declare DONE** — only after all applicable checks pass.

## Hard rule

`DONE = IMPLEMENTED + WRITTEN + VERIFIED + SYNCHRONIZED + SELF-CONTAINED`

If any required component is missing, the status is **NOT DONE**.

## No hidden incompleteness

A result must not contain:

- empty or placeholder definitions;
- missing symbols or unexplained notation;
- broken internal references;
- stale index or changelog entries;
- undocumented assumptions required to understand the result;
- claims that were not checked after the final write;
- a conclusion that depends on information available only in the conversation.

## Final-read rule

The final artifact must be read **after** the last write. The check must be performed on the actual stored artifact, not only on the content prepared before committing it.

## Research-specific rule

For experiments and mathematical research records, the artifact must separately state:

- definitions;
- assumptions;
- derivation;
- execution/test procedure;
- observed result;
- verification status;
- limitations and boundary conditions;
- what is and is not established.

## Status vocabulary

`DRAFT` — incomplete.

`IMPLEMENTED` — change exists, but final verification is pending.

`VERIFIED` — required checks pass.

`SYNCHRONIZED` — dependent canonical records are updated.

`DONE` — all applicable completion requirements pass.

## Governing principle

**“Done” means checked after writing, not merely completed during work.**

This standard is process infrastructure. It does not change the Ω-Math primitive language or physical claims.
