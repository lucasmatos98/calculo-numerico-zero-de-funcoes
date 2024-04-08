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
Definimos manualmente alfa e beta conforme instruído, e arbitrariamente um valor "n" igual a 1000 para limitar o número de iterações e um valor "e" igual a 10⁻⁷ de tolerância