import numpy as np
# Ω-035: combined discrete kinetic-energy accounting.
nr=nz=6; dr=dz=2.0/nr
rf=np.linspace(0,2,nr+1); zf=np.linspace(0,2,nz+1)
r=(rf[:-1]+rf[1:])/2; z=(zf[:-1]+zf[1:])/2
R,Z=np.meshgrid(r,z,indexing='ij'); RV,ZV=np.meshgrid(rf,zf,indexing='ij')
psi=np.sin(np.pi*RV/2)**2*np.sin(np.pi*ZV/2)**2
Fr=np.diff(psi,axis=1)/dz; Fz=-np.diff(psi,axis=0)/dr
ur_face=np.divide(Fr,rf[:,None],out=np.zeros_like(Fr),where=rf[:,None]!=0)
uz_face=Fz/r[:,None]
ur=.5*(ur_face[:-1]+ur_face[1:]); uz=.5*(uz_face[:,:-1]+uz_face[:,1:])
uT=.4*R*np.exp(-Z)*(1-R/2); m=R*dr*dz

def adv(q):
    out=np.zeros_like(q)
    for i in range(1,nr):
        for j in range(nz):
            F=Fr[i,j]; qf=.5*(q[i-1,j]+q[i,j]); out[i-1,j]-=F*qf/(r[i-1]*dr*dz); out[i,j]+=F*qf/(r[i]*dr*dz)
    for i in range(nr):
        for j in range(1,nz):
            F=Fz[i,j]; qf=.5*(q[i,j-1]+q[i,j]); out[i,j-1]-=F*qf/(r[i]*dr*dz); out[i,j]+=F*qf/(r[i]*dr*dz)
    return out
ar=-adv(ur)+uT*uT/R; az=-adv(uz); aT=-adv(uT)-ur*uT/R
conv=float(np.sum(m*(ur*ar+uz*az+uT*aT)))
p=np.sin(np.pi*R/2)*np.cos(np.pi*Z/2); pw=0.0
for i in range(1,nr):
    for j in range(nz): pw += -Fr[i,j]*(p[i,j]-p[i-1,j])/dr*dz
for i in range(nr):
    for j in range(1,nz): pw += -Fz[i,j]*(p[i,j]-p[i,j-1])/dz*dr
N=nr*nz; L=np.zeros((N,N))
for i in range(1,nr):
    for j in range(nz):
        a=(i-1)*nz+j;b=i*nz+j;w=rf[i]*dz/dr;L[a,a]+=w;L[b,b]+=w;L[a,b]-=w;L[b,a]-=w
for i in range(nr):
    for j in range(1,nz):
        a=i*nz+j-1;b=i*nz+j;w=r[i]*dr/dz;L[a,a]+=w;L[b,b]+=w;L[a,b]-=w;L[b,a]-=w
raw=sum(q.ravel()@L@q.ravel() for q in (ur,uz,uT)); nu=.05; visc=-nu*raw
print('convective_power =',conv); print('pressure_power =',pw); print('viscous_power =',visc)
print('total_power =',conv+pw+visc)
assert abs(conv)<1e-12 and abs(pw)<1e-12 and raw>=-1e-12
print('PASS OMEGA-035')
