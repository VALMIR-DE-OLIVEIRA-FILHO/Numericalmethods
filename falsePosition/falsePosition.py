import math
import os

# Function
def f(x):
    return 36*x - math.exp(x-8)

def false_position():
    a = 14
    b = 15
    eps1 = 1e-6
    eps2 = 1e-6

    caminho = os.path.join(os.path.dirname(__file__), "resultado.txt")

    with open(caminho, "w", encoding="utf-8") as file:

        for k in range(1, 101):
            x = (a * f(b) - b * f(a)) / (f(b) - f(a))
            fx = f(x)
            linha = f"Passo k = {k:2d}, raiz x = {x:14.10f}"
            print(linha)
            file.write(linha + "\n")

            # stopping criterion
            if (b - a) < eps1 or abs(fx) < eps2:
                break

            if f(a) * fx > 0:
                a = x
            else:
                b = x

        resultado = f"\nA raiz vale {x:14.10f} com {k} passos."
        print(resultado)
        file.write(resultado)

# Execute
false_position()