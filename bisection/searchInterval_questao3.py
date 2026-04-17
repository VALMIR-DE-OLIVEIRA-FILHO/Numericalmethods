import math


def f(x):
    return 100 / ( 1 + 99 * math.exp(-0.319 * x))

def searchIntervals(inicio=-200, fim=200):
    intervalos = []

    for a in range(inicio, fim):
        b = a + 1

        try:
            if f(a) * f(b) < 0:
                intervalos.append((a, b))
        except:
            continue

    if intervalos:
        print("Intervalos onde há raiz:\n")
        for i, (a, b) in enumerate(intervalos, 1):
            print(f"{i}. [{a}, {b}]")
            print(f"   f({a}) = {f(a):.6f}")
            print(f"   f({b}) = {f(b):.6f}\n")
    else:
        print("Nenhum intervalo encontrado.")

    return intervalos

# Executa
intervalos = searchIntervals()