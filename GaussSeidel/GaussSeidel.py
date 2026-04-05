import numpy as np

def gauss_seidel(A, b, eps3=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    ne = len(b)

    xk = np.zeros(ne)
    xk1 = np.zeros(ne)
    d = np.zeros(ne)

    print("\nValores iniciais:")
    for i in range(ne):
        xk[i] = b[i] / A[i][i]
        print(f"x{i+1}^(0) = {xk[i]:.12f}")

    for k in range(max_iter):
        print(f"\n-------------- Passo {k+1:2d} --------------")

        for i in range(ne):
            xk1[i] = b[i]

            for j in range(ne):
                if i != j:
                    if i > j:
                        xk1[i] -= A[i][j] * xk1[j]
                    else:
                        xk1[i] -= A[i][j] * xk[j]

            xk1[i] /= A[i][i]
            print(f"x{i+1}^({k+1}) = {xk1[i]:.12f}")

        dmax = 0
        print()

        for i in range(ne):
            d[i] = abs(xk1[i] - xk[i])
            print(f"d[{i}] = {d[i]:.12f}")
            dmax = max(dmax, d[i])

        if dmax < eps3:
            break

        print(f"\n{dmax:.12f} > {eps3:.12f} ---> continuar\n")

        xk = xk1.copy()

    print(f"\n{dmax:.12f} < {eps3:.12f} ---> convergiu\n")

    print(f"\nVetor final (passo {k+1}):")
    for i in range(ne):
        print(f"x{i+1} = {xk1[i]:.12f}")

    return xk1


if __name__ == "__main__":
    # No forget change the system for the new order
    A = [
    [4, -2],
    [-5, 4],
    
]

    b = [10,-2]
    resultado = gauss_seidel(A, b)