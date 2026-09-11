import numpy as np
# Ω-036: grid-family robustness of the direct vector cylindrical flux law.
def run(n):
    dr=dz=2.0/n; rf=np.linspace(0,2,n+1); zf=np.linspace(0,2,n+1)
    r=(rf[:-1]+rf[1:])/2; z=(zf[:-1]+zf[1:])/2
    R,Z=np.meshgrid(r,z,indexing='ij'); RV,ZV=np.meshgrid(rf,zf,indexing='ij')
    psi=np.sin(np.pi*RV/2)**2*np.sin(np.pi*ZV/2)**2
    Fr=np.diff(psi,axis=1)/dz; Fz=-np.diff(psi,axis=0)/dr
    urf=np.divide(Fr,rf[:,None],out=np.zeros_like(Fr),where=rf[:,None]!=0)
    uzf=Fz/r[:,None]; ur=.5*(urf[:-1]+urf[1:]); uz=.5*(uzf[:,:-1]+uzf[:,1:])
    ut=.4*R*np.exp(-Z)*(1-R/2); m=R*dr*dz
    def adv(q):
        out=np.zeros_like(q)
        for i in range(1,n):
            F=Fr[i]; qf=.5*(q[i-1]+q[i]); out[i-1]-=F*qf/(r[i-1]*dr*dz); out[i]+=F*qf/(r[i]*dr*dz)
        for j in range(1,n):
            F=Fz[:,j]; qf=.5*(q[:,j-1]+q[:,j]); out[:,j-1]-=F*qf/(r*dr*dz); out[:,j]+=F*qf/(r*dr*dz)
        return out
    ar=-adv(ur)+ut**2/R; az=-adv(uz); at=-adv(ut)-ur*ut/R
    div=(Fr[1:]-Fr[:-1]+Fz[:,1:]-Fz[:,:-1])/m
    power=np.sum(m*(ur*ar+uz*az+ut*at))
    return np.max(abs(div)),power
for n in (4,6,8,10,12):
    d,p=run(n); print(n,d,p); assert d<1e-12 and abs(p)<1e-12
print('PASS OMEGA-036')
