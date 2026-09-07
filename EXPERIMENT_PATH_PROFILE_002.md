# Ω-Experiment PATH-PROFILE-002 — Equal Source Distance Profiles, Different Organization

## Status

`FORMAL COUNTEREXAMPLE / DECLARED FINITE MODEL`

## 1. Question

Can two relational systems have the same shortest-path distance profile from a source while still differing in relational organization and controlled future behavior?

If yes, source-distance geometry is not a complete description of organization.

## 2. Construction

Use six entities, all initially in state `1`:

`A,B,C,D,E,F`.

Treat structural adjacencies as bidirectional (`+1` in both directions) for this experiment.

Construct two systems with the same number of vertices and edges and the same distance multiset from source `A`.

### ΩP₂-A — path with terminal branch

`A-B, B-C, C-D, D-E, E-F`

This is a six-vertex chain.

Distance multiset from `A`:

`{0,1,2,3,4,5}`.

### ΩP₂-B — path with different labeled organization

`A-B, B-C, C-D, D-F, F-E`

This is again a six-vertex chain, with the same source-distance multiset:

`{0,1,2,3,4,5}`.

The two systems are related by a label permutation, so this pair alone is **not** sufficient to establish label-independent structural difference.

Therefore the chain pair is retained only as a control demonstrating that a distance profile is label-blind only after an explicit quotient.

## 3. Stronger construction

Use the following non-isomorphic six-vertex trees, both rooted at `A`, with identical distance counts from `A`:

### ΩP₂-C — balanced branching

`A-B, A-C, B-D, C-E, C-F`

Source distances:

`{0,1,1,2,2,2}`.

### ΩP₂-D — unbalanced branching

`A-B, A-C, B-D, B-E, C-F`

Source distances:

`{0,1,1,2,2,2}`.

Both have:

- 6 entities;
- 5 structural edges;
- one connected component;
- all `+1` relations;
- identical source-distance histogram from `A`.

Yet their rooted degree organizations differ:

ΩP₂-C: `deg(A)=2, deg(B)=2, deg(C)=3, deg(D)=1, deg(E)=1, deg(F)=1`.

ΩP₂-D: `deg(A)=2, deg(B)=3, deg(C)=2, deg(D)=1, deg(E)=1, deg(F)=1`.

The two are actually isomorphic under swapping `B↔C` together with corresponding leaves, so this pair is also rejected as a non-isomorphic witness.

## 4. Decision

The attempted constructions show an important methodological point: matching a source-distance histogram is too weak to prove structural distinction, but producing a valid counterexample requires controlling graph isomorphism explicitly.

Therefore no universal claim is promoted from this experiment.

## 5. Required computational search

The next valid test must enumerate small unlabeled graphs and search for pairs that satisfy:

1. identical source-distance profiles;
2. non-isomorphism;
3. identical declared aggregate controls where required;
4. a deterministic transition rule producing different observations.

For each candidate pair, graph isomorphism must be checked before acceptance.

## 6. Research consequence

A scalar or histogram distance profile cannot be assumed sufficient merely because it contains more information than a single distance.

But insufficiency must be established by a genuine non-isomorphic counterexample, not by relabeling the same structure.

This reinforces the Ω rule:

`similar summary ≠ distinct structure`

and

`compressed ≠ equivalent`.

## 7. Status

`SEARCH SPECIFICATION — NOT A POSITIVE RESULT`

No claim of path-profile insufficiency is made by this document itself.
