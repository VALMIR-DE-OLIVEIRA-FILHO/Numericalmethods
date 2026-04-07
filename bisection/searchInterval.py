import math

def raiz5(x):
    return abs(x)**(1/5) * (1 if x >= 0 else -1)
def f(x):
    return (2*x**3 - 84*x**2 +6*x -1048)/ raiz5(2*x - 6)

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