# EXPERIMENT Ω-034 — Geometry-derived viscous dissipation

## Status
EXECUTED / FINITE NUMERICAL VERIFICATION

## Question
Can the dissipative part be generated independently from cylindrical geometry as a symmetric positive-semidefinite operator, rather than being defined as the remainder of a physical operator?

## Construction
The 6×6 cylindrical control-volume geometry is used with `m = r dr dz`.

A graph stiffness `L` is assembled directly from internal radial and axial faces. Each face contributes a standard two-point difference term with the cylindrical face measure. Therefore `L` is symmetric by construction and its quadratic form is a sum of nonnegative squared jumps.

The same independently generated vector field from Ω-032 is used only as the state on which dissipation is evaluated. The viscosity coefficient is `ν = 0.05`.

## Results
Symmetry residual:

`||L-L^T||∞ = 0`

Minimum eigenvalue:

`-5.492325789159323e-16`

The tiny negative value is numerical roundoff; it is far below the verification tolerance `1e-12`.

Raw positive quadratic dissipation:

`Σ q^T L q = 34.46686039067989`

Corresponding viscous power for `ν=0.05`:

`-1.7233430195339945 W`

## Result
**PASS — SYMMETRIC POSITIVE DISSIPATIVE OPERATOR.**

The dissipative operator can be obtained independently from geometry and face differences. Its positivity is not obtained by taking a symmetric remainder of the convective operator.

## Boundary
NOT_PROVEN — this is the complete cylindrical vector Laplacian/strain-rate tensor of Navier–Stokes. The present operator is a componentwise geometry-derived diffusion operator and does not yet include every cylindrical vector-viscous curvature coupling.

NOT_PROVEN — physical viscosity prediction from microscopic parameters.

## Consequence
The Ω flow construction now has independently generated reversible transport, pressure work, and dissipative structure. The remaining major gap is to combine them into one transient vector step and compare against an independently implemented axisymmetric incompressible reference solver, including pressure and viscous terms without copying the Ω operator.
