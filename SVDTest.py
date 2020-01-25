import numpy as np

a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
u, s, vh = np.linalg.svd(a, full_matrices=True)

verify1 = np.allclose(a, np.dot(u[:, :6] * s, vh))

smat = np.zeros((9, 6), dtype=complex)
smat[:6, :6] = np.diag(s)

verify2 = np.allclose(a, np.dot(u, np.dot(smat, vh)))

result = np.dot(u, np.dot(smat, vh))

print(a)
print("---asd-")
print(u)
print('----')
print(s)
print('----')
print(vh)
print('----')
print(smat.shape)