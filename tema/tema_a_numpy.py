import numpy as np

# 1. Setam seed pentru reproductibilitate
np.random.seed(42)

# Generam matricele A (4x3) si B (3x5) cu valori intre 1 si 10
A = np.random.randint(1, 11, (4, 3))
B = np.random.randint(1, 11, (3, 5))

print("Matricea A (4x3):")
print(A)

print("\nMatricea B (3x5):")
print(B)

# 2. Calculam produsul matriceal
C = A @ B

print("\nProdusul matriceal C = A @ B:")
print(C)

# 3. Operatii pe matricea C
suma_totala = np.sum(C)
media_coloane = np.mean(C, axis=0)
max_global = np.max(C)

print("\nSuma tuturor elementelor din C:")
print(suma_totala)

print("\nMedia pe fiecare coloana din C:")
print(media_coloane)

print("\nValoarea maxima globala din C:")
print(max_global)

# 4. BONUS
print("\n--- BONUS ---")

# Generam matrice patratica 3x3
M = np.random.randint(1, 11, (3, 3))

print("\nMatricea M:")
print(M)

# Determinant
det_M = np.linalg.det(M)
print("\nDeterminantul lui M:")
print(det_M)

# Inversa
inv_M = np.linalg.inv(M)
print("\nInversa lui M:")
print(inv_M)

# Verificare matrice identitate
identitate = M @ inv_M
print("\nM @ inv(M):")
print(identitate)

print("\nEste aproape matrice identitate?")
print(np.allclose(identitate, np.eye(3)))