import math

# Função f(x)
def f(x):
    return 1-x * math.log(x)
    # return 3.453*x**7 - 2.0975*x**6 - 120.5323*x**5 - 1989.34*x**3 + 12003

def metodo_secante():
    x0 = 1
    x1 = 2
    eps1 = 4e-5
    eps2 = 2e-5

    for k in range(1, 101):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))

        if abs(x2 - x1) < eps1 or abs(f(x2)) < eps2:
            break

        print(f"Passo k = {k:2d}, raiz x = {x1:14.10f}")

        x0 = x1
        x1 = x2

    print(f"\nA raiz vale {x2:14.10f} com {k} passos.")

# Executa
metodo_secante()

# equivalente ao system("PAUSE")
input("\nPressione ENTER para sair...")