import numpy as np
# Ω-034: geometry-derived symmetric positive viscous operator.
nr=nz=6; dr=dz=2.0/nr
rf=np.linspace(0,2,nr+1); zf=np.linspace(0,2,nz+1)
r=(rf[:-1]+rf[1:])/2; z=(zf[:-1]+zf[1:])/2
R,Z=np.meshgrid(r,z,indexing='ij'); RV,ZV=np.meshgrid(rf,zf,indexing='ij')
psi=np.sin(np.pi*RV/2)**2*np.sin(np.pi*ZV/2)**2
Fr=np.diff(psi,axis=1)/dz; Fz=-np.diff(psi,axis=0)/dr
ur=.5*(np.divide(Fr,rf[:,None],out=np.zeros_like(Fr),where=rf[:,None]!=0)[:-1]+np.divide(Fr,rf[:,None],out=np.zeros_like(Fr),where=rf[:,None]!=0)[1:])
uz=.5*(Fz/r[:,None])[:,:-1]+.5*(Fz/r[:,None])[:,1:]
uT=.4*R*np.exp(-Z)*(1-R/2)
N=nr*nz; L=np.zeros((N,N))
for i in range(1,nr):
    for j in range(nz):
        a=(i-1)*nz+j; b=i*nz+j; w=rf[i]*dz/dr
        L[a,a]+=w; L[b,b]+=w; L[a,b]-=w; L[b,a]-=w
for i in range(nr):
    for j in range(1,nz):
        a=i*nz+j-1; b=i*nz+j; w=r[i]*dr/dz
        L[a,a]+=w; L[b,b]+=w; L[a,b]-=w; L[b,a]-=w
qs=[ur.ravel(),uz.ravel(),uT.ravel()]
lam=float(np.linalg.eigvalsh(L).min())
diss=sum(float(q@L@q) for q in qs)
nu=.05
print('symmetry_residual =',np.linalg.norm(L-L.T,np.inf))
print('min_eigenvalue =',lam)
print('raw_dissipation =',diss)
print('viscous_power =',-nu*diss)
assert np.linalg.norm(L-L.T,np.inf)<1e-12
assert lam>-1e-12
assert diss>=-1e-12
print('PASS OMEGA-034')
