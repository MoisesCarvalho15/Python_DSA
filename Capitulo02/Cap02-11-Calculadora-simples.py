# Operações da calculadora simples
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

# Checando a entrada do usuário e fazendo as operações
def iniciar(op, num1, num2):
    if op == 1:
        print(f"\n{num1} + {num2} = {soma(num1, num2)}")
    elif op == 2:
        print(f"\n{num1} - {num2} = {subtracao(num1, num2)}")
    elif op == 3:
        print(f"\n{num1} * {num2} = {multiplicacao(num1,num2)}")
    elif op == 4:
        print(f"\n{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("\nDados incorretos. Por favor, inicie o programa novamente.")
        
# Mensagem do menu
print(f"\n{10*'='} Calculadora em Python {10*'='}")
print("\nSelecione o número da operação desejada:\n")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

# Entrada do usuário
escolha = int(input("Digite sua opção (1/2/3/4): "))
numero1 = float(input("\nDigite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chamando a função para iniciar o programa
iniciar(escolha, numero1, numero2)