import numpy as np

# Ω-031: conservative cylindrical face-flux transport.
# A divergence-free face flux is generated from a vertex streamfunction.
# Central face interpolation is then tested directly against the cylindrical
# kinetic-energy inner product M = diag(r dr dz).

nr = nz = 4
dr = dz = 0.5
rf = np.arange(nr + 1) * dr
zf = np.arange(nz + 1) * dz
r = (rf[:-1] + rf[1:]) / 2
z = (zf[:-1] + zf[1:]) / 2
R, Z = np.meshgrid(r, z, indexing="ij")
N = nr * nz

def idx(i, j):
    return i * nz + j

# Streamfunction vanishes on every boundary, so the resulting face flux
# has zero boundary transport and is discretely divergence-free.
RV, ZV = np.meshgrid(rf, zf, indexing="ij")
psi = np.sin(np.pi * RV / 2.0) * np.sin(np.pi * ZV / 2.0)

# Cylindrical volume fluxes per unit azimuth:
#   F_r = r u_r = d psi / dz
#   F_z = r u_z = -d psi / dr
Fr = np.diff(psi, axis=1) / dz
Fz = -np.diff(psi, axis=0) / dr

div = (Fr[1:] - Fr[:-1] + Fz[:, 1:] - Fz[:, :-1]) / (R * dr * dz)
assert np.max(np.abs(div)) < 1e-12

m = (R * dr * dz).ravel()
M = np.diag(m)
T = np.zeros((N, N))

# Conservative central face-flux operator for a transported scalar q:
# dq_i/dt = -(1/m_i) sum_faces F_face (q_i+q_j)/2.
for i in range(nr):
    for j in range(nz):
        k = idx(i, j)
        if i > 0:
            F = -Fr[i, j]
            kn = idx(i - 1, j)
            T[k, k] += -F / (2 * m[k])
            T[k, kn] += -F / (2 * m[k])
        if i < nr - 1:
            F = Fr[i + 1, j]
            kn = idx(i + 1, j)
            T[k, k] += -F / (2 * m[k])
            T[k, kn] += -F / (2 * m[k])
        if j > 0:
            F = -Fz[i, j]
            kn = idx(i, j - 1)
            T[k, k] += -F / (2 * m[k])
            T[k, kn] += -F / (2 * m[k])
        if j < nz - 1:
            F = Fz[i, j + 1]
            kn = idx(i, j + 1)
            T[k, k] += -F / (2 * m[k])
            T[k, kn] += -F / (2 * m[k])

weighted_skew = np.linalg.norm(T.T @ M + M @ T, ord=np.inf)
q = (np.sin(R) * np.cos(Z)).ravel()
power = float(q @ M @ (T @ q))

print("max_divergence =", np.max(np.abs(div)))
print("weighted_skew_residual =", weighted_skew)
print("kinetic_power =", power)

assert weighted_skew < 1e-12
assert abs(power) < 1e-12
print("PASS OMEGA-031")
