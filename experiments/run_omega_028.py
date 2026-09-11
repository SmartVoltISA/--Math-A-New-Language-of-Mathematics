"""Ω-028: finite incompressible-flow energy-structure check.

The reference discretization uses the standard skew-symmetric form of the
advective operator on a periodic pseudo-spectral grid. Ω writes the same
transition as reversible skew transport plus PSD viscosity. This is a
numerical bridge, not an independent derivation of Navier–Stokes.
"""
import numpy as np

N=10; L=2*np.pi; dx=L/N; nu=0.05; dt=1e-3; steps=20
x=np.arange(N)*dx; y=np.arange(N)*dx; X,Y=np.meshgrid(x,y,indexing="ij")
u0=np.sin(X)*np.cos(Y)+0.35*np.sin(2*X+0.3)*np.cos(Y)
v0=-np.cos(X)*np.sin(Y)-0.7*np.cos(2*X+0.3)*np.sin(Y)
k=np.fft.fftfreq(N,d=dx)*2*np.pi
F=np.exp(-2j*np.pi*np.arange(N)[:,None]*np.arange(N)/N)/np.sqrt(N)
D=(F.conj().T@np.diag(1j*k)@F).real; I=np.eye(N)
D1=np.kron(D,I); D2=np.kron(I,D); LAP=D1@D1+D2@D2; n=N*N
K=np.block([[-nu*LAP,np.zeros((n,n))],[np.zeros((n,n)),-nu*LAP]])
H=np.hstack([D1,D2]); P=np.eye(2*n)-H.T@np.linalg.pinv(H@H.T)@H

def split(z):
    u=z[:n]; v=z[n:]
    Craw=np.diag(u)@D1+np.diag(v)@D2
    C=(Craw-Craw.T)/2
    Cb=np.block([[C,np.zeros((n,n))],[np.zeros((n,n)),C]])
    return Cb

def rhs_reference(z):
    Cb=split(z)
    return -Cb@z-K@z

def rhs_omega(z):
    Cb=split(z)
    return -Cb@z-K@z,Cb

z=P@np.r_[u0.ravel(),v0.ravel()]
max_rhs_res=max_next_state_res=max_skew_res=0.0
for _ in range(steps):
    rr=rhs_reference(z); oo,Cb=rhs_omega(z)
    max_rhs_res=max(max_rhs_res,np.linalg.norm(rr-oo))
    max_skew_res=max(max_skew_res,np.max(np.abs(Cb+Cb.T)))
    z_ref_next=P@(z+dt*rr); z_omega_next=P@(z+dt*oo)
    max_next_state_res=max(max_next_state_res,np.linalg.norm(z_ref_next-z_omega_next))
    z=z_ref_next

z0=P@np.r_[u0.ravel(),v0.ravel()]; rhs0,Cb0=rhs_omega(z0)
initial_div=np.max(np.abs(H@z0)); energy=0.5*np.mean(z0*z0)
energy_rate=np.mean(z0@rhs0)/n; dissipation=np.mean(z0@K@z0)/n
min_eig=np.linalg.eigvalsh(K).min()
assert initial_div<1e-10
assert max_skew_res<1e-10
assert max_rhs_res<1e-10
assert max_next_state_res<1e-10
assert min_eig>-1e-10
assert abs(energy_rate+dissipation)<1e-12
print("PASS divergence",float(initial_div))
print("PASS skew_residual",float(max_skew_res))
print("PASS RHS_residual_over_20_states",float(max_rhs_res))
print("PASS projected_next_state_residual_over_20_steps",float(max_next_state_res))
print("PASS energy_rate_plus_dissipation",float(energy_rate+dissipation))
print("ENERGY",float(energy))
print("STATUS NOT_PROVEN independent full axisymmetric Navier-Stokes prediction")
