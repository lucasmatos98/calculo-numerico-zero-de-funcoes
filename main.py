import math
from tabulate import tabulate


n = 1000 # numero máximo de iterações
e = 10 ** (-15) # tolerância
a, b = (3, 4) # intervalo
alfa = 0.2
beta = 2

def butler_volmer(alfa, beta):
	def inner_function(x):
		primeiro_termo = math.e ** (alfa * x)
		segundo_termo = math.e ** ((alfa - 1) * x)
		return primeiro_termo - segundo_termo - beta
	return inner_function

def butler_volmer_derivada(alfa):
	def inner_function(x):
		primeiro_termo = (math.e ** (alfa * x)) * alfa
		segundo_termo = (math.e ** ((alfa - 1) * x)) * (alfa - 1)
		return primeiro_termo - segundo_termo
	return inner_function

def metodo_bisseccao(n, e, f, a, b, output, x_zero = float('-inf')):
	def inner_function(a, b, x_anterior, i):
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

		if (intervalo_suficiente or f_de_x_toleravel or diferenca_entre_x_toleravel or ultima_iteracao):
			return x
		
		eh_primeiro_intervalo = f(a) * f(x) < 0
		if eh_primeiro_intervalo:
			return inner_function(a, x, x, i + 1)
		else:
			return inner_function(x, b, x, i + 1)
	return inner_function(a, b, x_zero, 0)

def metodo_newton(n, e, f, f_linha, output, x_zero):
	def inner_function(x_anterior, i):
		x = x_anterior - (f(x_anterior) / f_linha(x_anterior))
		diferenca_entre_x_toleravel = abs(x - x_anterior) < e
		f_de_x_toleravel = abs(f(x)) < e
		ultima_iteracao = n == i
		output.append({
			"x0": x_anterior,
			"~x": x,
			"iterações": i
		})
		if (f_de_x_toleravel or diferenca_entre_x_toleravel or ultima_iteracao):
			return x
		return inner_function(x, i + 1)
	
	return inner_function(x_zero, 0)
	



f = butler_volmer(alfa, beta)
output = []
metodo_bisseccao(n, e, f, a, b, output)
print("Método da bissecção: \n" + tabulate(output, headers="keys", tablefmt="pretty"))

f_linha = butler_volmer_derivada(alfa)
output = []
newton = metodo_newton(n, e, f, f_linha, output, b)
print("Método de Newton: \n" + tabulate(output, headers="keys", tablefmt="pretty"))