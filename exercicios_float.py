# #### Números de Ponto Flutuante ('float')

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
print("Digite dois números com casas decimais após a vírgula para realizar uma soma.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: " ))

soma = num1 + num2
resultado = print(f"A soma dos dois números é {soma}. ")

print(type(soma)) 
print('\n')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

print("Digite dois números com casas decimais após a vírgula para obter a média dos dois.")

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: " ))

soma = float(num_1 + num_2)
media = soma / 2 
resultado = print(f"A média dos dois números é {media:.2f}. ")
print('\n')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

print("Digite a base e o expoente pra saber o resultado da potência.")

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

potencia = base ** expoente

print(f"A potenciação dos números digitados é: {potencia:.2f}")
print('\n')


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print("Digite uma temperatura em Celsius pra converter pra Farenheit")

temp_celsius = float(input("Digite a temperatura em Celsius:"))

conv_farenheit = (temp_celsius * 9/5) + 32

print(f"A temperatura convertida pra Farenheit é {conv_farenheit:.2f} °F.")
print('\n')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print("Digite o raio pra calcular a área do circulo")

raio = float(input("Digite o a medida do raio:"))

area_circulo = 3.14 * (raio * raio)

print (f'A área do círculo é { area_circulo:.2f}.')


