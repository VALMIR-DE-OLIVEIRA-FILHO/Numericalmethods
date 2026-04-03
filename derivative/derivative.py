import sympy as sp

# variável simbólica
x = sp.symbols('x')

# função
f = 2**x -3*x -40 

# derivada
df = sp.diff(f, x)

print("f(x) =", f)
print("f'(x) =", df)