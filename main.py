import math
from tabulate import tabulate


n = 1000 # numero máximo de iterações
e = 10 ** (-4) # tolerância
a, b = (3, 4) # intervalo

def butler_volmer(alfa, beta):
    def inner_function(x):
        primeiro_termo = math.e ** (alfa * x)
        segundo_termo = math.e ** ((alfa - 1) * x)
        return primeiro_termo - segundo_termo - beta
    return inner_function

def metodo_bisseccao(n, i, e, f, a, b, output, x_anterior = float('-inf'), ):
  x = (a + b) / 2
  intervalo_suficiente = b - a < e
  f_de_x_toleravel = abs(f(x)) < e
  diferenca_entre_x_toleravel = abs(x - x_anterior) < e
  ultima_iteracao = n == i
  output.append({
      "a": a,
      "b": b,
      "~x": x,
      "iterações": i
    })

  if (intervalo_suficiente or f_de_x_toleravel or diferenca_entre_x_toleravel or ultima_iteracao) :
    return x
  
  eh_primeiro_intervalo = f(a) * f(x) < 0
  if eh_primeiro_intervalo:
    return metodo_bisseccao(n, i + 1, e, f, a, x, output, x)
  else:
    return metodo_bisseccao(n, i + 1, e, f, x, b, output, x)



f = butler_volmer(0.2,2)
output = []
metodo_bisseccao(n, 0, e, f, a, b, output)
print("Método da bissecção: \n" + tabulate(output, headers="keys", tablefmt="pretty"))