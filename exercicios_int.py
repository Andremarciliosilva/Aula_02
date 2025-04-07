# #### Inteiros ('int')

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

print("Digite dois números para realizar uma soma.")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: " ))

soma = num1 + num2
resultado = print(f"A soma dos dois números é {soma}. ")

print(type(soma)) 
print('\n')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

print("Digite um número pra calcular o resto o resto da divisão por 5.")

numero = int(input("Digite o número: "))

resto = numero % 5

print(f"O resto da divisão do número digitado por 5 é {resto}.")
print('\n')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

print("Digite 2 números pra saber o resultado da multpiplicação deles.")
numero_digitado1 = int(input("Digite o primeiro número: "))
numero_digitado2 = int(input("Digite o segundo número: "))

multiplicacao = numero_digitado1 * numero_digitado2

print(f"O resultado da multiplicação dos dois números é: {multiplicacao}")
print('\n')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print("Digite dois números para realizar a divisão do primeiro pelo segundo.")

num_1 = int(input("Digite o primeiro número inteiro: "))
num_2 = int(input("Digite o segundo número inteiro: " ))

divisao = num1 // num2
resultado = print(f"A divisão inteira {num_1} por {num_2} é {soma}. ")
print('\n')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print("Digite um número para saber o resultado da elevação dele ao quadrado.")

numero_dig = int(input("Digite o número: "))

quadrado = numero_dig * numero_dig

print(f"{numero_dig} elevado ao quadrado é {quadrado}")