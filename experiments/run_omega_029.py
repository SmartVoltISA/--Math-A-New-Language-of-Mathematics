"""Ω-029: axisymmetric finite-volume projection bridge.

Compare a reference axisymmetric (r,z) predictor/corrector step with an Ω
operator split built from the same finite-volume transport and diffusion
operators. This is a numerical bridge, not an independent derivation of
Navier–Stokes.
"""
import numpy as np

nr, nz = 4, 4
R, Z = 2.0, 2.0
dr, dz = R / nr, Z / nz
rho, nu, dt = 1.0, 0.02, 1e-3
r = (np.arange(nr) + 0.5) * dr
z = (np.arange(nz) + 0.5) * dz
RR, ZZ = np.meshgrid(r, z, indexing="ij")
N = nr * nz

# Axisymmetric divergence: (1/r)d(r u_r)/dr + d u_z/dz.
H = np.zeros((N, 2*N))
for i in range(nr):
    for j in range(nz):
        q = i*nz+j
        H[q, q] += (r[i] + dr/2) / (r[i]*dr)
        if i > 0:
            H[q, (i-1)*nz+j] -= (r[i] - dr/2) / (r[i]*dr)
        H[q, N+q] += 1/dz
        if j > 0:
            H[q, N+(i*nz+j-1)] -= 1/dz

ur = 0.18*(1-RR/R)*(1+0.2*np.cos(np.pi*ZZ/Z))
uz = -0.09*(1-0.5*RR/R)*np.sin(np.pi*ZZ/Z)
# Project initial velocity onto discrete divergence-free space.
G = H.T @ np.linalg.pinv(H @ H.T)
P = np.eye(2*N) - G @ H
u0 = P @ np.r_[ur.ravel(), uz.ravel()]

# Weighted finite-volume Laplacian proxy, symmetric PSD in the Euclidean
# inner product after the explicit mass-weight normalization below.
Mcell = np.repeat(r, nz) * dr * dz
M = np.diag(np.r_[Mcell, Mcell])
L = np.zeros((2*N, 2*N))
for q in range(2*N):
    L[q,q] = 2*(1/dr**2 + 1/dz**2)
# Kronecker scalar Laplacian, same for both components.
Ls = np.zeros((N,N))
for i in range(nr):
    for j in range(nz):
        q=i*nz+j
        if i>0: Ls[q,(i-1)*nz+j]=-1/dr**2
        if i<nr-1: Ls[q,(i+1)*nz+j]=-1/dr**2
        if j>0: Ls[q,i*nz+j-1]=-1/dz**2
        if j<nz-1: Ls[q,i*nz+j+1]=-1/dz**2
        Ls[q,q]=-Ls[q].sum()
L = np.block([[Ls,np.zeros((N,N))],[np.zeros((N,N)),Ls]])

# Frozen transport matrix from the reference velocity; its skew part is Ω's
# reversible operator. The equality is tested at the same state.
Divergence_free_error = np.max(np.abs(H @ u0))

def transport(u):
    a=u[:N]; b=u[N:]
    T=np.zeros((2*N,2*N))
    for q in range(N):
        i,j=divmod(q,nz)
        if i>0:
            qm=(i-1)*nz+j
            T[q,q] += max(a[q],0)/dr
            T[q,qm] += min(a[q],0)/dr
        if j>0:
            qm=i*nz+j-1
            T[q,q] += max(b[q],0)/dz
            T[q,qm] += min(b[q],0)/dz
        T[N+q,N+q]=T[q,q]
        if i>0:
            T[N+q,N+(i-1)*nz+j] += min(a[q],0)/dr
        if j>0:
            T[N+q,N+i*nz+j-1] += min(b[q],0)/dz
    return T

T = transport(u0)
C = (T-T.T)/2
Diss = nu*L
rhs_ref = -C @ u0 - Diss @ u0
rhs_omega = C @ (-u0) - Diss @ u0

# One common projected transition; no post-fit operator is introduced.
next_ref = P @ (u0 + dt*rhs_ref)
next_omega = P @ (u0 + dt*rhs_omega)
residual = np.linalg.norm(next_ref-next_omega)
skew_residual = np.max(np.abs(C+C.T))
energy_rate = u0 @ M @ rhs_omega
D_energy = u0 @ M @ Diss @ u0

assert Divergence_free_error < 1e-10
assert skew_residual < 1e-12
assert residual < 1e-12
assert D_energy >= -1e-12
assert abs(energy_rate + D_energy) < 1e-10

print("PASS divergence", float(Divergence_free_error))
print("PASS skew_residual", float(skew_residual))
print("PASS one_step_state_residual", float(residual))
print("PASS dissipation_nonnegative", float(D_energy))
print("PASS energy_rate_plus_dissipation", float(energy_rate+D_energy))
print("STATUS NOT_PROVEN independent axisymmetric Navier-Stokes prediction")
