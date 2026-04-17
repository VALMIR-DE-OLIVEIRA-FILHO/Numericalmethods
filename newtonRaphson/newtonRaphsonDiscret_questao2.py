import math

# Função f(x)
def f(x):
   return (30/(x+8))**3 - (19 - x)

# Derivada numérica (diferença central de ordem 4)
def fld(x):
    h = 1e-2
    return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12*h)

def newton():
    a= 4
    b= 5
    x0 = (a+ b)/2
    eps1 = 1e-6
    eps2 = 1e-6

    for k in range(1, 101):
        x1 = x0 - f(x0) / fld(x0)

        # Critérios de parada
        if abs(x1 - x0) < eps1 or abs(f(x1)) < eps2:
            break

        print(f"Passo k = {k:2d}, raiz x = {x1:14.10f}")

        x0 = x1

    print(f"\nA raiz vale {x1:14.10f} com {k} passos.")

# Executa
newton()