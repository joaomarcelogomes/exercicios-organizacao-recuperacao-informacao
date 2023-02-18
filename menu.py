import solutions


def start():
    print("Olá!")
    print_menu()

    while True:
        action = input("Insira o número da ação desejada (Pressione 6 para visualizar a lista de ações novamente): ")
        execute_action(action)

def print_menu():
    print("Lista de ações disponíveis:")
    print("""
        1. Calcular a soma do intervalo entre 0 e um número informado.
        2. Encontrar o menor número de um vetor, juntamente com seu tamanho lógico.
        3. Encontrar uma potência.
        4. Encontrar o máximo divisor comum entre dois números.
        5. Converter um número decimal para binário.
        6. Imprimir a lista de ações novamente
        7. Sair do programa.
    """)


def execute_action(action):
    match action:
        case "1":
            number = int(input("Insira o número limite ao intervalo a ser somado: "))
            sum = solutions.sum_between_zero_and(number)
            print(sum)
        case "2":
            vector = input("Insira um vetor de números, separados por ',' para encontro do menor valor: ")
            vector = vector.split(",")
            vector = [int(x) for x in vector]
            result = solutions.find_least_element(vector)
            print(result)
        case "3":
            number = int(input("Insira o número base da potência: "))
            exponent = int(input("Insira o número expoente da potência: "))
            result = solutions.power(number, exponent)
            print(result)
        case "4":
            first_number = int(input("Insira o primeiro número para cálculo do mdc: "))
            second_number = int(input("Insira o segundo número para cálculo do mdc: "))
            result = solutions.mdc(first_number, second_number)
            print(result)
        case "5":
            number = int(input("Insira o número que seja converter para binário: "))
            result = solutions.bin_to_dec(number)
            print(result)
        case "6":
            print_menu()
        case "7":
            raise SystemExit
        case _:
            print("Ação inválida!")
            print_menu()