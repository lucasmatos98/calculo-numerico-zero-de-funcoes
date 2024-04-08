import math


n = 1000 # numero máximo de iterações
e = 10 ** (-7) # tolerância
a, b = (3, 4) # intervalo

def butler_volmer(alfa, beta):
    def inner_function(x):
        primeiro_termo = math.e ** (alfa * x)
        segundo_termo = math.e ** ((alfa - 1) * x)
        return primeiro_termo - segundo_termo - beta
    return inner_function

def metodo_bisseccao(n, e, f, a, b, x_anterior = float('-inf')):
  x = (a + b) / 2
  intervalo_suficiente = b - a < e
  f_de_x_toleravel = abs(f(x)) < e
  diferenca_entre_x_toleravel = abs(x - x_anterior) < e
  ultima_iteracao = n == 0
  if (intervalo_suficiente or f_de_x_toleravel or diferenca_entre_x_toleravel or ultima_iteracao) :
    print(intervalo_suficiente, f_de_x_toleravel, diferenca_entre_x_toleravel, ultima_iteracao)
    print(n)
    print(x_anterior)
    return x
  
  eh_primeiro_intervalo = f(a) * f(x) < 0
  if eh_primeiro_intervalo:
    return metodo_bisseccao(n - 1, e, f, a, x, x)
  else:
    return metodo_bisseccao(n - 1, e, f, x, b, x)

f = butler_volmer(0.2,2)
x = metodo_bisseccao(n, e, f, a, b)
print('método da bisseccao: ' + str(x))