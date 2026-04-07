import numpy as np
import math
import matplotlib.pyplot as plt

# =========================================
# 🔧 FUNÇÃO
# =========================================
def raiz5(x):
    return np.sign(x) * (abs(x)**(1/5))

# =========================================
# FUNÇÃO
# =========================================
def f(x):
    return (2*x**3 - 84*x**2 + 6*x - 1048) / raiz5(2*x - 6)

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
def secante(func, x0, x1, eps1=1e-5, eps2=1e-5, max_iter=100):
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
# 📊 GRÁFICO TOP (COM VALORES VISÍVEIS)
# =========================================
x_vals = np.linspace(-20, 20, 500)
y_vals = [f(i) for i in x_vals]

plt.figure(figsize=(12, 7))

# Curva
plt.plot(x_vals, y_vals, linewidth=2, label="f(x)")

# Função auxiliar pra anotar bonito
def anotar(x, y, texto):
    plt.annotate(
        texto,
        (x, y),
        textcoords="offset points",
        xytext=(8, 8),
        arrowprops=dict(arrowstyle="->"),
        fontsize=9
    )

# =====================
# RAÍZES
# =====================
# Junta todas as raízes
rx = [r for r in raizes]
ry = [f(r) for r in raizes]

# Plota tudo de uma vez
plt.scatter(rx, ry, s=80, color='red', label="Raízes")

# Anota cada uma
for r in raizes:
    anotar(r, f(r), f"{r:.3f}")
# =====================
# CRÍTICOS
# =====================
for c in criticos:
    y = f(c)
    tipo = classificar_critico(c)

    if tipo == "MÁXIMO":
        plt.scatter(c, y, s=100, marker='^', label="Máximo")
    elif tipo == "MÍNIMO":
        plt.scatter(c, y, s=100, marker='v', label="Mínimo")

    anotar(c, y, f"{c:.3f}")

# =====================
# INFLEXÃO
# =====================
for i in inflexoes:
    y = f(i)
    plt.scatter(i, y, s=100, marker='D', label="Inflexão")
    anotar(i, y, f"{i:.3f}")

# Eixos
plt.axhline(0, linestyle='--')
plt.axvline(0, linestyle='--')

# Grid
plt.grid(alpha=0.3)

# Remove legenda duplicada
handles, labels = plt.gca().get_legend_handles_labels()
unique = dict(zip(labels, handles))
plt.legend(unique.values(), unique.keys())

plt.title("Análise completa da função", fontsize=14)
plt.tight_layout()

plt.show()