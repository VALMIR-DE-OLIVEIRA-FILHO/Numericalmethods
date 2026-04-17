import numpy as np
import math
import matplotlib.pyplot as plt

# =========================================
# 🔧 FUNÇÃO
# =========================================
def f(x):
    return  100 / ( 1 + 99 * math.exp(-0.319 * x))

# =========================================
# 🔧 DERIVADAS NUMÉRICAS (h FIXO)
# =========================================
def fl(x):
    h = 1e-2
    return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12*h)

def fll(x):
    h = 1e-2
    return (-f(x - 2*h) + 16*f(x - h) - 30*f(x) + 16*f(x + h) - f(x + 2*h)) / (12 * h**2)


# =========================================
# 🔧 MÉTODO DA SECANTE
# =========================================
def secante(func, x0, x1, eps1=1e-6, eps2=1e-6, max_iter=100):
    for _ in range(max_iter):
        f0 = func(x0)
        f1 = func(x1)

        if abs(f1 - f0) < 1e-12:
            return None

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if abs(x2 - x1) < eps1 or abs(func(x2)) < eps2:
            return x2

        x0, x1 = x1, x2

    return None


# =========================================
# 🔧 BUSCA AUTOMÁTICA (MELHORADA)
# =========================================
def encontrar_intervalos(func, a, b, n=300):
    xs = np.linspace(a, b, n)
    intervalos = []

    for i in range(len(xs)-1):
        if func(xs[i]) * func(xs[i+1]) < 0:
            intervalos.append((xs[i], xs[i+1]))

    return intervalos


# =========================================
# 🔧 REMOVER DUPLICADOS
# =========================================
def remover_repetidos(lista, tol=1e-4):
    resultado = []
    for x in lista:
        if not any(abs(x - y) < tol for y in resultado):
            resultado.append(x)
    return resultado


# =========================================
# 🔧 CLASSIFICAÇÃO
# =========================================
def classificar_critico(x):
    f2 = fll(x)
    if f2 > 0:
        return "MÍNIMO"
    elif f2 < 0:
        return "MÁXIMO"
    else:
        return "INDEFINIDO"


def eh_inflexao(x):
    eps = 1e-4
    return fll(x - eps) * fll(x + eps) < 0


# =========================================
# 🚀 EXECUÇÃO TOTAL AUTOMÁTICA
# =========================================
print("\n=== RESULTADOS ===")

# 🔹 RAÍZES
intervalos_raizes = encontrar_intervalos(f, -20, 20)
raizes = []

for x0, x1 in intervalos_raizes:
    r = secante(f, x0, x1)
    if r is not None and abs(f(r)) < 1e-4:
        raizes.append(r)

raizes = remover_repetidos(raizes)

print("\nRaízes:")
for r in raizes:
    print(f"x = {r:.6f}")


# 🔹 PONTOS CRÍTICOS
intervalos_criticos = encontrar_intervalos(fl, -20, 20)
criticos = []

for x0, x1 in intervalos_criticos:
    c = secante(fl, x0, x1)
    if c is not None and abs(fl(c)) < 1e-4:
        criticos.append(c)

criticos = remover_repetidos(criticos)

print("\nPontos críticos:")
for c in criticos:
    tipo = classificar_critico(c)
    print(f"{tipo} em x = {c:.6f} | f(x) = {f(c):.6f}")


# 🔹 INFLEXÃO
intervalos_inflexao = encontrar_intervalos(fll, -20, 20)
inflexoes = []

for x0, x1 in intervalos_inflexao:
    inf = secante(fll, x0, x1)
    if inf is not None and abs(fll(inf)) < 1e-4 and eh_inflexao(inf):
        inflexoes.append(inf)

inflexoes = remover_repetidos(inflexoes)

print("\nPontos de inflexão:")
if inflexoes:
    for i in inflexoes:
        print(f"x = {i:.6f} | f(x) = {f(i):.6f}")
else:
    print("Nenhum encontrado")


# =========================================
# 📊 GRÁFICO
# =========================================
x = np.linspace(-20, 20, 500)
y = [f(i) for i in x]

plt.figure()
plt.plot(x, y, label="f(x)")

for r in raizes:
    plt.scatter(r, f(r))
    plt.text(r, f(r), f"{r:.2f}")

for c in criticos:
    plt.scatter(c, f(c))
    plt.text(c, f(c), f"{c:.2f}")

for i in inflexoes:
    plt.scatter(i, f(i))
    plt.text(i, f(i), f"{i:.2f}")

plt.axhline(0)
plt.grid()
plt.legend()
plt.title("Análise completa automática")
plt.show()