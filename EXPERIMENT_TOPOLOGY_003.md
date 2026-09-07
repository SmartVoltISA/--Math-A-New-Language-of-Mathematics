# Ω-Experiment TOPOLOGY-003 — Same Counts, Different Organization

## 1. Question

Can topology alone distinguish two Ω-systems when the following are held equal?

- number of entities;
- entity states;
- number of relations;
- relation-sign counts.

The purpose is to remove trivial explanations based on composition and total relation count.

## 2. Construction

Use four entities, all with state `1`:

`A=(1,1)`
`B=(2,1)`
`C=(3,1)`
`D=(4,1)`

Use four positive directed relations in each system.

### Ω₃ — two feedback pairs

`A → B`

`B → A`

`C → D`

`D → C`

### Ω₄ — one directed cycle

`A → B`

`B → C`

`C → D`

`D → A`

Both systems have:

`|E| = 4`

`|R| = 4`

`N(+1)=4`

`N(−1)=0`

and identical entity states.

## 3. Structural difference

Ω₃ contains two disconnected 2-cycles.

Ω₄ contains one connected 4-cycle.

Thus the systems have equal counts but different organization.

Their degree sequences can also be identical under the directed in/out-degree representation: every vertex has one incoming and one outgoing relation.

Therefore degree counts alone do not distinguish these two structures.

## 4. Dynamic perturbation

Use the same explicit propagation rule as in BEHAVIORAL-EQUIV-002:

> At each step, every entity directly reached by an outgoing relation from a changed entity copies that changed state at the next step.

Perturb only A:

`t0: A=0, B=1, C=1, D=1`.

### Ω₃

`t1: A=0, B=0, C=1, D=1`

`t2: A=0, B=0, C=1, D=1`

The perturbation remains confined to the A-B component.

### Ω₄

`t1: A=0, B=0, C=1, D=1`

`t2: A=0, B=0, C=0, D=1`

`t3: A=0, B=0, C=0, D=0`

The perturbation propagates through the entire connected cycle.

## 5. Result

The systems are indistinguishable by:

- entity count;
- entity-state multiset;
- relation count;
- relation-sign count;
- directed degree sequence.

Yet the same perturbation produces different trajectories.

Therefore topology/organization contains information that is not captured by these aggregate quantities.

## 6. Important qualification

This result depends on the explicitly chosen transition rule. It demonstrates existence of a transition model under which topology matters; it does not prove that topology is causally sufficient in every Ω-system.

## 7. Relation to collapse research

This experiment provides a control against a common error:

`different behavior → different number of relations`.

Here relation count is fixed.

The next question is whether a sequence of increasingly coarse quotients can erase the topological distinction while preserving some or all observable behavior.

That leads to:

`topology → behavioral equivalence → quotient → structural collapse`.

## 8. Status

`FORMALLY CONSTRUCTED`

The experiment is a mathematical counterexample/construction, not an empirical claim about nature.

## 9. Next experiment

Construct a pair with identical:

- entities;
- states;
- relation count;
- sign counts;
- degree sequence;
- component count;

but different cycle arrangement or path redundancy.

Then determine the smallest observable that still distinguishes them.
