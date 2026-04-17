# number of equations
ne = 5

# augmented matrix [A|b]
A = [
    #[x, y, z, w, v] importante a ordem 
    [1, -2, -2, -8, 2, -3],
    [6, 2, -2, -1, 0, 0],
    [-1, 2, 2, -1, 7, 0],
    [2, -1, 7, 2, -1, 36],
    [-1, -5, -2, 0, 1, 2]
]

# =========================
# Gauss-Jordan com pivotamento
# =========================
for k in range(ne):

    # 🔁 Pivotamento parcial
    max_row = k
    for i in range(k + 1, ne):
        if abs(A[i][k]) > abs(A[max_row][k]):
            max_row = i

    # troca de linhas
    A[k], A[max_row] = A[max_row], A[k]

    # pivô
    piv = A[k][k]

    # verificação de segurança
    if abs(piv) < 1e-10:
        raise ValueError("Sistema sem solução única ou mal condicionado")

    # 🔧 normaliza linha do pivô
    for j in range(ne + 1):
        A[k][j] /= piv

    # 🔧 zera outras linhas
    for i in range(ne):
        if i != k:
            fator = A[i][k]
            for j in range(ne + 1):
                A[i][j] -= fator * A[k][j]

# =========================
# Resultado
# =========================
print("\nSolução:")
for i in range(ne):
    print(f"x{i+1} = {A[i][ne]:.9f}")