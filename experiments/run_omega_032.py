import numpy as np
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
div=(Fr[1:]-Fr[:-1]+Fz[:,1:]-Fz[:,:-1])/m
power=np.sum(m*(ur*ar+uz*az+uT*aT))
curv=np.sum(m*(ur*uT*uT/R-uT*ur*uT/R))
print('max_divergence =',np.max(np.abs(div)))
print('convective_power =',power)
print('curvature_power =',curv)
assert np.max(np.abs(div))<1e-12
assert abs(power)<1e-12
assert abs(curv)<1e-12
print('PASS OMEGA-032')
