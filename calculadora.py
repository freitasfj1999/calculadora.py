
# Calculadora básica

#Script das operações

#Soma
def soma(num1, num2):
    return num1 + num2

#Subtração
def sub(num1, num2):
    return num1 - num2

#Multiplicação
def mult(num1, num2):
    return num1 * num2

#Divisão
def div(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    return num1 / num2

#Porcentagem
def porcentagem(num1, num2):
    return (num1 * num2) / 100

# O Código para cada operação está sendo representado pelas caractérias: + = Soma | - = Subtração |  / = Divisão | * = Maultiplicação | % = Porcentagem.

# Boas-vindas / Solicitação do nome
print("Bem-vindo à sua calculadora!")

nome = input("Qual o seu nome? ")

while True:
    print(f"\nOlá, {nome}! Vamos fazer uma operação.")

    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite o sinal da operação (+, -, *, /, %): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = soma(num1, num2)
        elif operacao == '-':
            resultado = sub(num1, num2)
        elif operacao == '*':
            resultado = mult(num1, num2)
        elif operacao == '/':
            resultado = div(num1, num2)
        elif operacao == '%':
            resultado = porcentagem(num1, num2)
        else:
            print("Operação inválida. Tente novamente.")
            continue

        print(f"Resultado da operação: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
    if continuar != 's':
        print(f"Obrigado por usar a calculadora, {nome}! Até a próxima!")
        break

# O código está em Python, usando a função de loop para que o usuário possa fazer mais de uma operação sem ter a necessidade de rodar o código novamente.