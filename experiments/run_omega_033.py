import numpy as np
# Ω-033: pressure work compatibility with the same cylindrical face fluxes.
nr=nz=6; dr=dz=2.0/nr
rf=np.linspace(0,2,nr+1); zf=np.linspace(0,2,nz+1)
r=(rf[:-1]+rf[1:])/2; z=(zf[:-1]+zf[1:])/2
R,Z=np.meshgrid(r,z,indexing='ij'); RV,ZV=np.meshgrid(rf,zf,indexing='ij')
psi=np.sin(np.pi*RV/2)**2*np.sin(np.pi*ZV/2)**2
Fr=np.diff(psi,axis=1)/dz; Fz=-np.diff(psi,axis=0)/dr
m=R*dr*dz
p=np.sin(np.pi*R/2)*np.cos(np.pi*Z/2)
div=(Fr[1:]-Fr[:-1]+Fz[:,1:]-Fz[:,:-1])/m
work=0.0
for i in range(1,nr):
    for j in range(nz): work += -Fr[i,j]*(p[i,j]-p[i-1,j])/dr*dz
for i in range(nr):
    for j in range(1,nz): work += -Fz[i,j]*(p[i,j]-p[i,j-1])/dz*dr
print('max_divergence =',np.max(np.abs(div)))
print('pressure_power =',work)
assert np.max(np.abs(div))<1e-12
assert abs(work)<1e-12
print('PASS OMEGA-033')
