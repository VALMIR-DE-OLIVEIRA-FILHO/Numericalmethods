import math

def f(x):
    return 2**x - 3*x - 40

def bissecao():
    a = -14
    b = -13
    #error tolerance
    eps1 = 1e-4
    eps2 = 2e-4


    # 📂 file path to save the response
    caminho_arquivo = "bisection/resultado.txt"

    with open(caminho_arquivo, "w") as arquivo:

        if f(a) * f(b) > 0:
            msg = "Erro: não há troca de sinal no intervalo.\n"
            print(msg)
            arquivo.write(msg)
            return

        for k in range(1, 101):
            x = (a + b) / 2

            if f(a) * f(x) > 0:
                a = x
            else:
                b = x

            linha = f"k = {k:2d} | x = {x:14.10f} | f(x) = {f(x):.6f} | intervalo = [{a:.6f}, {b:.6f}]\n"

            print(linha, end="")
            arquivo.write(linha)
            #observe the stopping criterion
            if abs(b - a) < eps2 or abs(f(x)) < eps1:
                break

        resultado = "\n====================================\n"
        resultado += f"Raiz aproximada: {x:.10f}\n"
        resultado += f"Numero  de iteracoes: {k}\n"
        resultado += "====================================\n"

        print(resultado)
        arquivo.write(resultado)

# Execute
bissecao()