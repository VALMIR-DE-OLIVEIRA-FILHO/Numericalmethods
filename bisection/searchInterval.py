import math

def f(x):
    return 1-x * math.log(x)

def searchIntervals(inicio=-100, fim=100):
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