import math

def f(x):
    return x**3 +x -1000 

def encontrar_intervalo(inicio=-100, fim=100):
    for a in range(inicio, fim):
        b = a + 1
        
        # evita log(0) ou valores inválidos
        try:
            if f(a) * f(b) < 0:
                print(f"Intervalo encontrado: [{a}, {b}]")
                print(f"f({a}) = {f(a):.6f}")
                print(f"f({b}) = {f(b):.6f}")
                return a, b
        except:
            continue

    print("Nenhum intervalo encontrado.")
    return None, None

# Executa
a, b = encontrar_intervalo()