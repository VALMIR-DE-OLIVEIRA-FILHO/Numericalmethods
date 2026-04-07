import numpy as np

# =========================================
# RAIZ QUINTA REAL
# =========================================
def raiz5(x):
    return np.sign(x) * (abs(x)**(1/5))

# =========================================
# FUNÇÃO
# =========================================
def f(x):
    return (2*x**3 - 89*x**2 + 6*x - 1054) / raiz5(2*x - 6)

# =========================================
# DERIVADAS (5 PONTOS - IGUAL PROFESSOR)
# =========================================
def derivada1(f, x, h=1e-2):
    return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12*h)

def derivada2(f, x, h=1e-2):
    return (-f(x - 2*h) + 16*f(x - h) - 30*f(x) +
            16*f(x + h) - f(x + 2*h)) / (12*h**2)

# =========================================
# SECANTE
# =========================================
def secante(g, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        g_x0 = g(x0)
        g_x1 = g(x1)

        if abs(g_x1 - g_x0) < 1e-12:
            break

        x2 = x1 - g_x1 * (x1 - x0) / (g_x1 - g_x0)

        if abs(x2 - x1) < tol or abs(g(x2)) < tol:
            return x2, i+1

        x0, x1 = x1, x2

    return x1, max_iter

# =========================================
# TABELA (igual Excel)
# =========================================
print("\n📊 Tabela f''(x):\n")

g = lambda x: derivada2(f, x)

for x in range(10, 15):
    print(f"x={x}, f''(x)={g(x):.6f}")

# =========================================
# INTERVALO CORRETO
# =========================================
a, b = None, None

for x in range(10, 20):
    if g(x) < 0 and g(x+1) > 0:
        a, b = x, x+1
        break

# =========================================
# RESULTADO
# =========================================
if a is not None:
    raiz, passos = secante(g, a, b)
    
    print("\n✅ RESULTADO:")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Ponto de inflexão ≈ {raiz:.6f}")
    print(f"Iterações: {passos}")