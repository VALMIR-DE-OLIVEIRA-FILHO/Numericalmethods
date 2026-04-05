# Métodos Numéricos em Python

## 📊 Descrição

Este projeto é uma coleção abrangente de implementações de métodos numéricos clássicos em Python. Desenvolvido como material didático e de referência, o repositório cobre algoritmos fundamentais para resolução de equações não-lineares, sistemas lineares e análise de funções.

Os métodos implementados incluem técnicas de busca de raízes (bisseção, falsa posição, Newton-Raphson, secante), resolução de sistemas lineares (Gauss-Jordan, Gauss-Seidel) e análise numérica (derivação, pontos de inflexão).

## ✨ Funcionalidades

- **Métodos de Raízes**: Bisseção, Falsa Posição, Newton-Raphson (analítico e numérico), Secante
- **Sistemas Lineares**: Eliminação de Gauss-Jordan, Método Iterativo de Gauss-Seidel
- **Análise Numérica**: Derivação simbólica e numérica, detecção de pontos de inflexão
- **Utilitários**: Busca automática de intervalos contendo raízes
- **Saídas Detalhadas**: Logs de iteração com critérios de convergência

## 🛠️ Pré-requisitos

- Python 3.7+
- Bibliotecas: NumPy, SymPy, Matplotlib

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/numerical-methods.git
   cd numerical-methods
   ```

2. Instale as dependências:
   ```bash
   pip install numpy sympy matplotlib
   ```

## 🚀 Como Usar

Cada método está implementado em sua própria pasta. Navegue até a pasta desejada e execute o script Python:

### Exemplos de Uso

#### Método da Bisseção
```bash
cd bisection
python bisectionMethods.py
```

#### Método de Newton-Raphson
```bash
cd newtonRaphson
python newtonRaphson.py
```

#### Resolução de Sistemas Lineares (Gauss-Jordan)
```bash
cd GaussJordan
python GaussJordan.py
```

Os resultados são exibidos no terminal e salvos em arquivos `resultado.txt` quando aplicável.

## 📁 Estrutura do Projeto

```
numerical-methods/
├── bisection/
│   ├── bisectionMethods.py      # Método da bisseção
│   ├── searchInterval.py        # Busca de intervalos
│   └── resultado.txt            # Resultados da bisseção
├── derivative/
│   └── derivative.py            # Derivação simbólica
├── falsePosition/
│   ├── falsePosition.py         # Método da falsa posição
│   └── resultado.txt            # Resultados da falsa posição
├── GaussJordan/
│   └── GaussJordan.py           # Eliminação de Gauss-Jordan
├── GaussSeidel/
│   └── GaussSeidel.py           # Método de Gauss-Seidel
├── inflections/
│   └── inflections.py           # Análise de pontos de inflexão
├── newtonRaphson/
│   ├── newtonRaphson.py         # Newton-Raphson analítico
│   └── newtonRaphsonDiscret.py  # Newton-Raphson numérico
└── secantMethod/
    └── secant.py                # Método da secante
```

## 📚 Métodos Implementados

Abaixo está uma tabela detalhada dos métodos numéricos implementados neste repositório, incluindo uma breve descrição de cada um e sua importância na computação numérica:

| Método | Pasta | Descrição | Importância |
|--------|-------|-----------|-------------|
| **Bisseção** | `bisection/` | Busca de raízes por divisão sucessiva de intervalo | Método robusto e sempre convergente quando há mudança de sinal na função. Ideal para funções contínuas onde a convergência é garantida, embora seja mais lento que métodos iterativos. |
| **Falsa Posição** | `falsePosition/` | Raízes por interpolação linear entre pontos | Combina robustez da bisseção com velocidade maior através de interpolação. Útil quando um lado do intervalo converge mais lentamente. |
| **Newton-Raphson** | `newtonRaphson/` | Raízes usando derivada analítica/numérica | Convergência quadrática muito rápida quando próximo da raiz. Essencial para problemas onde alta precisão é necessária, mas requer cuidado com pontos onde a derivada é zero. |
| **Secante** | `secantMethod/` | Raízes sem necessidade de derivada explícita | Aproxima a derivada numericamente, evitando cálculo analítico. Útil para funções complexas ou quando a derivada é difícil de obter. |
| **Gauss-Jordan** | `GaussJordan/` | Resolução direta de sistemas lineares | Método exato para sistemas pequenos, transforma a matriz em forma reduzida. Fundamental para validação de soluções e problemas de pequena escala. |
| **Gauss-Seidel** | `GaussSeidel/` | Resolução iterativa de sistemas lineares | Eficiente para sistemas grandes e esparsos, comuns em engenharia e física. Permite soluções aproximadas com menos memória que métodos diretos. |
| **Derivação** | `derivative/` | Cálculo simbólico de derivadas | Base para muitos algoritmos numéricos, incluindo otimização e análise de estabilidade. Essencial para entender o comportamento de funções. |
| **Pontos de Inflexão** | `inflections/` | Detecção de inflexões usando método da secante | Importante para análise de curvas em economia, física e engenharia, identificando pontos onde a concavidade muda, crucial para modelagem e otimização. |

## 🔧 Configuração

Os parâmetros de tolerância e critérios de parada podem ser ajustados diretamente nos arquivos Python:

- `eps1`: Tolerância para diferença entre iterações
- `eps2`: Tolerância para valor da função
- `max_iter`: Número máximo de iterações

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novos métodos
- Melhorar implementações existentes
- Adicionar documentação

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.</content>
<parameter name="filePath">c:\Numericalmethods\README.md