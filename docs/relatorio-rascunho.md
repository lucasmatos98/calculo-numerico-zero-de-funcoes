# Zero de funções
Considere α = 0.2 e β = 2 e o problema de encontrar f(x) = 0.

## Encontre um intervalo que contenha uma raíz de f(x)
Utilizamos o web software [Desmos](https://www.desmos.com/calculator) para plotar o gráfico.
Com o seguinte resultado: [gráfico da função](grafico-funcao.png)
Determinando o intervalo: [3,4]

## Implemente os métodos da Bissecção, de Newton e da Secante utilizando um software de preferência. Utilize como critério de parada uma tolerância e número máximo de iterações.
Utlizando a linguagem Python, lingua franca entre os integrates do grupo.
Criamos uma função que retorna o valor da equação de Butler-Volmer.

Criamos um função recursiva para determinar o x aproximado usando a função de bissecção
Definimos manualmente alfa e beta conforme instruído, e arbitrariamente um valor "n" igual a 1000 para limitar o número de iterações e um valor "e" igual a 10⁻⁴ de tolerância. A função Secante calcula iterativamente novas estimativas da raiz usando uma fórmula que aproxima a derivada da função entre dois pontos. Ele continua atualizando as estimativas até que uma das condições de parada seja atendida: a diferença entre as estimativas é menor que a tolerância, o valor da função na estimativa é menor que a tolerância ou o número máximo de iterações é atingido. A função metodo_secante adiciona os resultados de cada iteração à lista de saída, incluindo os valores das estimativas anteriores e a próxima estimativa, juntamente com o número da iteração.





