# Operações

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Não foi possível divisão por 0. Tente novamente!"
    return a / b

# Menu
def exibir_menu():
    print("\n\nMenu da Calculadora") 
    print("----------------------")
    print("| Operações disponíveis: |")
    print("| 1- Soma (+)            |")
    print("| 2- Subtração (-)       |")
    print("| 3- Multiplicação (*)   |")
    print("| 4- Divisão (/)         |")
    print("| 5- Exibir Histórico    |")
    print("| 6- Sair                |")
    print("------------------------")

# Histórico
historico = [] 

# Loop
while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-6): ")

# Caso o usuário escolha '6', o programa é encerrado

    if escolha == "6":
        print("Encerrando o programa...")
        break
    
# Exibir o histórico de operações

    elif escolha == "5":
        if not historico:
            print("Nenhuma operação realizada ainda.")
        else:
            print("\nHistórico:")
            for item in historico:
                print(item)
        continue  

    else:  
        if escolha not in ["1", "2", "3", "4"]:  # Verifica se a escolha é inválida
            print("Opção inválida. Tente novamente.")
            continue  

        try:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
        except ValueError:
            print("Por favor, digite novamente apenas números válidos.")
            continue  # Retorna ao início do loop para a próxima interação

        if escolha == "1":
            resultado = somar(a, b)
            operacao = f"{a} + {b} = {resultado}"

        elif escolha == "2":
            resultado = subtrair(a, b)
            operacao = f"{a} - {b} = {resultado}"

        elif escolha == "3":
            resultado = multiplicar(a, b)
            operacao = f"{a} * {b} = {resultado}"

        elif escolha == "4":
            resultado = dividir(a, b)
            operacao = f"{a} / {b} = {resultado}"

        print(f"Resultado: {resultado}")
        historico.append(operacao)  # Adiciona a operação ao histórico
