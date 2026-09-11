"""Ω-028: finite incompressible-flow operator split check.

Compares a standard pseudo-spectral incompressible velocity RHS with the
Ω reversible-skew + dissipative-PSD decomposition. This is a discretization
bridge, not a claim of a full physical Navier–Stokes derivation.
"""
import numpy as np

N = 10
L = 2 * np.pi
dx = L / N
nu = 0.05
dt = 1e-3
steps = 20
x = np.arange(N) * dx
y = np.arange(N) * dx
X, Y = np.meshgrid(x, y, indexing="ij")
u0 = np.sin(X) * np.cos(Y) + 0.35 * np.sin(2 * X + 0.3) * np.cos(Y)
v0 = -np.cos(X) * np.sin(Y) - 0.7 * np.cos(2 * X + 0.3) * np.sin(Y)

k = np.fft.fftfreq(N, d=dx) * 2 * np.pi
F = np.exp(-2j * np.pi * np.arange(N)[:, None] * np.arange(N) / N) / np.sqrt(N)
D = (F.conj().T @ np.diag(1j * k) @ F).real
I = np.eye(N)
D1 = np.kron(D, I)
D2 = np.kron(I, D)
LAP = D1 @ D1 + D2 @ D2
n = N * N
K = np.block([[-nu * LAP, np.zeros((n, n))], [np.zeros((n, n)), -nu * LAP]])

def rhs_reference(z):
    u = z[:n].reshape(N, N); v = z[n:].reshape(N, N)
    dux = (D1 @ u.ravel()).reshape(N, N); duy = (D2 @ u.ravel()).reshape(N, N)
    dvx = (D1 @ v.ravel()).reshape(N, N); dvy = (D2 @ v.ravel()).reshape(N, N)
    conv = np.r_[(u * dux + v * duy).ravel(), (u * dvx + v * dvy).ravel()]
    return -conv - K @ z

def rhs_omega(z):
    u = z[:n]; v = z[n:]
    C1 = np.diag(u) @ D1 + np.diag(v) @ D2
    C = (C1 - C1.T) / 2
    Cb = np.block([[C, np.zeros((n, n))], [np.zeros((n, n)), C]])
    return -Cb @ z - K @ z, Cb

z_ref = np.r_[u0.ravel(), v0.ravel()]
z_omega = z_ref.copy()
max_rhs_res = 0.0
max_state_res = 0.0
max_skew_res = 0.0
for _ in range(steps):
    rr = rhs_reference(z_ref)
    oo, Cb = rhs_omega(z_omega)
    max_rhs_res = max(max_rhs_res, np.linalg.norm(rr - oo))
    max_skew_res = max(max_skew_res, np.max(np.abs(Cb + Cb.T)))
    z_ref = z_ref + dt * rr
    z_omega = z_omega + dt * oo
    max_state_res = max(max_state_res, np.linalg.norm(z_ref - z_omega))

initial_div = np.max(np.abs(D1 @ z_ref[:n] + D2 @ z_ref[n:]))
_, Cb0 = rhs_omega(np.r_[u0.ravel(), v0.ravel()])
z0 = np.r_[u0.ravel(), v0.ravel()]
rhs0, _ = rhs_omega(z0)
energy = 0.5 * np.mean(z0 * z0)
energy_rate = np.mean(z0 @ rhs0) / n
dissipation = np.mean(z0 @ K @ z0) / n

assert initial_div < 1e-10
assert max_skew_res < 1e-10
assert max_rhs_res < 1e-10
assert max_state_res < 1e-10
assert np.linalg.eigvalsh(K).min() > -1e-10
assert abs(energy_rate + dissipation) < 1e-12

print("PASS divergence", float(initial_div))
print("PASS skew_residual", float(max_skew_res))
print("PASS one_step_operator_residual", float(max_rhs_res))
print("PASS multi_step_state_residual", float(max_state_res))
print("PASS energy_rate_plus_dissipation", float(energy_rate + dissipation))
print("ENERGY", float(energy))
print("STATUS NOT_PROVEN full axisymmetric Navier-Stokes derivation")
