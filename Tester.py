from SVD import SVD

svd = SVD()

vector = [[10,20,30,4,9],[5,6,7,8,9]]

u = []
vh = []

u, s, vh = svd.descomponer(vector, False)

print('U')
print(u)
print('S')
print(s)
print('VH')
print(vh)

original = svd.reconstruir(u,s,vh)

print('Original')
print(original)