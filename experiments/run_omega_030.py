import numpy as np

# Ω-030: independent axisymmetric convection falsification.
# The nonlinear pointwise convective operator is constructed independently;
# only afterwards is its linearized operator projected to the metric-skew part.

N = 4
R = Z = 2.0
dr = dz = 0.5
r = (np.arange(N) + 0.5) * dr
zgrid = (np.arange(N) + 0.5) * dz
Rr, Zz = np.meshgrid(r, zgrid, indexing="ij")

# Periodic/spectral derivatives in the local r,z grid are used only to build
# a smooth divergence-free test field. The comparison is between independently
# defined convection and its metric-skew projection.
Lr = N * dr
k = 2 * np.pi * np.fft.fftfreq(N, d=dr)

def d(a, axis):
    A = np.fft.fft(a, axis=axis)
    shape = [1, 1]
    shape[axis] = N
    return np.fft.ifft(1j * k.reshape(shape) * A, axis=axis).real

psi = np.sin(np.pi * Rr / R) * np.sin(np.pi * Zz / Z)
ur = d(psi, 1) / Rr
uz = -d(psi, 0)

# Cylindrical divergence residual.
div = (1.0 / Rr) * d(Rr * ur, 0) + d(uz, 1)
assert np.max(np.abs(div)) < 1e-12

n = N * N
Mdiag = np.r_[Rr.ravel(), Rr.ravel()] * dr * dz
M = np.diag(Mdiag)
zstate = np.r_[ur.ravel(), uz.ravel()]

# Linearization of the independent pointwise convective operator:
# N(u) = (ur d_r + uz d_z) u.
Dx = np.zeros((n, n))
Dz = np.zeros((n, n))
for j in range(n):
    e = np.zeros(n)
    e[j] = 1.0
    E = e.reshape(N, N)
    Dx[:, j] = d(E, 0).ravel()
    Dz[:, j] = d(E, 1).ravel()

urv, uzv = ur.ravel(), uz.ravel()
U = np.diag(urv)
W = np.diag(uzv)

ur_r = Dx @ urv
ur_z = Dz @ urv
uz_r = Dx @ uzv
uz_z = Dz @ uzv

T = np.block([
    [U @ Dx + W @ Dz + np.diag(ur_r), np.diag(ur_z)],
    [np.diag(uz_r), U @ Dx + W @ Dz + np.diag(uz_z)],
])

# Independent nonlinear convection evaluated directly from the field.
Nu = ur * d(ur, 0) + uz * d(ur, 1)
Nz = ur * d(uz, 0) + uz * d(uz, 1)
Nstate = np.r_[Nu.ravel(), Nz.ravel()]

# Ω candidate: metric-weighted skew projection, applied only after T exists.
Minv = np.diag(1.0 / Mdiag)
C = 0.5 * (T - Minv @ T.T @ M)
S = 0.5 * (T + Minv @ T.T @ M)

weighted_skew = np.max(np.abs(C.T @ M + M @ C))
mismatch = np.linalg.norm(Nstate - C @ zstate)
norm_N = np.linalg.norm(Nstate)
independent_power = float(zstate @ M @ Nstate)
omega_power = float(zstate @ M @ (C @ zstate))
symmetric_power = float(zstate @ M @ (S @ zstate))

print("divergence_residual", np.max(np.abs(div)))
print("weighted_skew_residual", weighted_skew)
print("independent_convective_power", independent_power)
print("omega_skew_power", omega_power)
print("symmetric_remainder_power", symmetric_power)
print("operator_mismatch", mismatch)
print("independent_operator_norm", norm_N)

assert weighted_skew < 1e-10
assert abs(independent_power) < 1e-10
assert abs(omega_power) < 1e-10
assert mismatch > 0.1
assert mismatch / norm_N > 0.5

print("PASS — divergence constraint")
print("PASS — metric-weighted Ω skew structure")
print("PASS — independent convection is energy-neutral in this test")
print("FAIL — Ω skew projection does not reproduce independent convection")
