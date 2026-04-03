import math

# Função f(x)
def f(x):
    return 2**x - 3*x - 40
    # return math.exp(-x/7 - 4) + x/5 + math.exp(x/4 - 5)

# Derivada f'(x)
def df(x):
    return 2**x*math.log(2) -3
    # return -math.exp(-x/7 - 4)/7 + 1/5 + math.exp(x/4 - 5)/4

def newton_raphson():
    a = -14
    b = -13
    x0 = (a+b)/2
    eps1 = 1e-5
    eps2 = 3e-4

    for k in range(1, 101):
        x1 = x0 - f(x0) / df(x0)

        # critério de parada
        if abs(x1 - x0) < eps1 or abs(f(x1)) < eps2:
            break

        print(f"Passo k = {k:2d}, raiz x = {x1:14.10f}")

        x0 = x1

    print(f"\nA raiz vale {x1:14.10f} com {k} passos.")

# Executar
newton_raphson()