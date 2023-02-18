"""
    Exercício 1	- Escreva uma função recursiva que receba, como parâmetro,
    um número inteiro positivo, e retorne a soma de todos os números inteiros
    entre 0 e o número recebido.
"""


def sum_between_zero_and(target):
    if target == 0:
        return target

    if target < 0:
        return target + sum_between_zero_and(target + 1)

    return target + sum_between_zero_and(target - 1)


"""
    Exercício 2 - Desenvolva uma função recursiva que identifique e retorne
    o menor elemento de um vetor de números inteiros recebido por parâmetro, juntamente, com o seu tamanho lógico.
"""


def find_least_element(vector, size=None, actual_index=0):
    size = len(vector) if size is None else size

    if size == 0:
        return "Menor número do vetor: {} | Tamanho lógico do vetor: {}".format(vector[actual_index], len(vector))

    new_size = size - 1
    if vector[new_size] < vector[actual_index]:
        return find_least_element(vector, new_size, new_size)

    return find_least_element(vector, new_size, actual_index)


"""
    Exercício 3 - A operação de potencialização pode ser representada por X elevado a Y. 
    Crie uma função recursiva que execute esta operação, recebendo dois números inteiros positivos, 
    um representando a base (X) e o outro, o expoente (Y)
"""


def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


"""
    Exercício 4 - O Algoritmo de Euclides é um método simples e eficiente para encontrar o Máximo Divisor Comum (MDC) 
    entre dois números inteiros (A e B diferentes de zero). 
    Tomando como base A>B, siga o roteiro abaixo, até que o resto R seja igual a zero.
        a.	Divida A por B, obtendo o resto R1. Se R1 for zero, o MDC entre A e B é B;
        b.	Se R1 não for zero, divida B por R1, obtendo o resto R2. Se R2 for zero, o MDC entre A e B é R1;
        c.	Se R2 não for zero, divida R1 por R2. Obtendo o resto R3. Se R3 for zero, o MDC entre A e B é R2.
    Com base nos passos apresentados, elabore uma função recursiva que calcule o MDC entre dois números inteiros digitados.
"""


def mdc(a, b):
    r1 = a % b
    if r1 == 0:
        return b

    return mdc(b, r1)


"""
    Exercício 5 - Escreva um algoritmo recursivo que receba um número decimal e faça a sua conversão 
    para o seu correspondente em binário.
"""


def bin_to_dec(number):
    if number == 0:
        return ""

    binary = number % 2
    return "{}{}".format(binary, bin_to_dec(int(number / 2)))
