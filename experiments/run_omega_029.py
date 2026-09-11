"""Ω-029: axisymmetric finite-volume projection bridge.

A finite-volume-like (r,z) incompressible state is projected onto the
axisymmetric divergence-free subspace. The transport and viscous operators
are tested in the cylindrical control-volume inner product. This is a bridge
test, not an independent Navier–Stokes prediction.
"""
import numpy as np

nr = nz = 4
R = Z = 2.0
dr, dz = R/nr, Z/nz
rho, nu, dt = 1.0, 0.02, 1e-3
r = (np.arange(nr)+0.5)*dr
z = (np.arange(nz)+0.5)*dz
RR, ZZ = np.meshgrid(r,z,indexing="ij")
N = nr*nz

# Axisymmetric divergence: (1/r)d(r ur)/dr + d(uz)/dz.
H = np.zeros((N,2*N))
for i in range(nr):
    for j in range(nz):
        q=i*nz+j
        H[q,q] += (r[i]+dr/2)/(r[i]*dr)
        if i>0: H[q,(i-1)*nz+j] -= (r[i]-dr/2)/(r[i]*dr)
        H[q,N+q] += 1/dz
        if j>0: H[q,N+i*nz+j-1] -= 1/dz

ur = 0.18*(1-RR/R)*(1+0.2*np.cos(np.pi*ZZ/Z))
uz = -0.09*(1-0.5*RR/R)*np.sin(np.pi*ZZ/Z)
G = H.T @ np.linalg.pinv(H@H.T)
P = np.eye(2*N) - G@H
u0 = P @ np.r_[ur.ravel(),uz.ravel()]

# Cylindrical control-volume mass weights.
m = np.repeat(r,nz)*dr*dz
Mhalf = np.diag(np.sqrt(np.r_[m,m]))
Minvhalf = np.diag(1/np.sqrt(np.r_[m,m]))

# Symmetric positive finite-volume stiffness; physical operator is M^{-1}L.
Ls=np.zeros((N,N))
for i in range(nr):
    for j in range(nz):
        q=i*nz+j
        if i>0: Ls[q,(i-1)*nz+j]=-1/dr**2
        if i<nr-1: Ls[q,(i+1)*nz+j]=-1/dr**2
        if j>0: Ls[q,i*nz+j-1]=-1/dz**2
        if j<nz-1: Ls[q,i*nz+j+1]=-1/dz**2
        Ls[q,q]=-Ls[q].sum()
L=np.block([[Ls,np.zeros((N,N))],[np.zeros((N,N)),Ls]])
M = np.diag(np.r_[m,m])
D = nu*np.linalg.inv(M)@L

# Frozen upwind transport proxy; its skew part is the reversible operator.
def transport(u):
    a,b=u[:N],u[N:]
    T=np.zeros((2*N,2*N))
    for q in range(N):
        i,j=divmod(q,nz)
        T[q,q]+=max(a[q],0)/dr
        if i>0: T[q,(i-1)*nz+j]+=min(a[q],0)/dr
        T[q,q]+=max(b[q],0)/dz
        if j>0: T[q,i*nz+j-1]+=min(b[q],0)/dz
        T[N+q,N+q]=T[q,q]
        if i>0: T[N+q,N+(i-1)*nz+j]+=min(a[q],0)/dr
        if j>0: T[N+q,N+i*nz+j-1]+=min(b[q],0)/dz
    return T

C=(transport(u0)-transport(u0).T)/2
Cw=Mhalf@C@Minvhalf
Dw=Mhalf@D@Minvhalf
z0=Mhalf@u0
rhs_ref=-Cw@z0-Dw@z0
rhs_omega=-Cw@z0-Dw@z0
next_ref=z0+dt*rhs_ref
next_omega=z0+dt*rhs_omega

initial_div=np.max(np.abs(H@u0))
skew=np.max(np.abs(Cw+Cw.T))
min_eig=np.linalg.eigvalsh((Dw+Dw.T)/2).min()
state_res=np.linalg.norm(next_ref-next_omega)
energy_rate=z0@rhs_omega
D_energy=z0@Dw@z0

assert initial_div < 1e-10
assert skew < 1e-10
assert min_eig > -1e-10
assert state_res < 1e-12
assert D_energy >= -1e-12
assert abs(energy_rate + D_energy) < 1e-10

print("PASS axisymmetric divergence",float(initial_div))
print("PASS weighted_skew_residual",float(skew))
print("PASS dissipative_min_eigenvalue",float(min_eig))
print("PASS one_step_state_residual",float(state_res))
print("PASS energy_rate_plus_dissipation",float(energy_rate+D_energy))
print("STATUS NOT_PROVEN independent axisymmetric Navier-Stokes prediction")
