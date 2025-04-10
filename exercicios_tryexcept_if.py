# 21. Conversor de Temperatura
'''
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
'''

print("Digite uma temperatura em Celsius pra converter pra Farenheit")
try:
    temp_celsius = float(input("Digite a temperatura em Celsius:"))
    conv_farenheit = (temp_celsius * 9/5) + 32
    print(f"A temperatura convertida pra Farenheit é {conv_farenheit:.2f} °F.")

except ValueError:
    print('Por favor, digite apenas números')

# 22. Verificador de Palíndromo
'''Crie um programa que verifica se uma palavra ou frase é um palíndromo 
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize if para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''
while True:

    entrada = input('Digite uma palavra pra verificar se é um palíndromo: ')

    if not entrada.isnumeric():
        entrada_rev = entrada [::-1]
        if entrada == entrada_rev:
            print('É um palíndromo')
        else:
            print('Não é um palíndromo')
        break
    else:
        print('Digite apenas palavras.')

# 23. Calculadora Simples
'''Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
Use try-except para lidar com divisões por zero e entradas não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
Imprima o resultado ou uma mensagem de erro apropriada.'''

while True:
    try: 
        numero_1 = int(input('Digite o primeiro número: '))
        numero_2 = int(input('Digite o segundo número: ')) 
        operador = input('Digite a operação que deseja fazer (+ = soma / - = subtração / / = divisão ou * = multiplicação): ')
        if operador not in '+-*/':
             print('Digite um operador permitido')
             print('\n')

    except ValueError:
        print('Digite apenas números')

    if operador == '+':
        soma = numero_1 + numero_2
        print('O resultado da soma é: ', soma)

    elif operador == '-':
        subtracao = numero_1 - numero_2
        print('O resultado da subtração é: ', subtracao)

    elif operador == '*':
        multiplicacao = numero_1 * numero_2
        print('O resultado da multiplicação é: ', multiplicacao )

    elif operador == '/':
        try:
            divisao = numero_1 / numero_2
            print('O resultado da divisão é: ', divisao)

        except ZeroDivisionError:
            print('Não é possível fazer uma divisão por 0')
    print('Programa finalizado!')
    break

# 24. Classificador de Números
'''Escreva um programa que solicite ao usuário para digitar um número. 
Utilize try-except para assegurar que a entrada seja numérica 
e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar".'''

try:
    entrada = int(input('Digite um número: '))
except ValueError:
    print('Digite apenas números')

if entrada > 0:
    print('O número é positivo!')

elif entrada < 0:
    print('O número é negativo! ')

else:
    print('O número é 0!')

if entrada % 2 == 0:
    print('Este é um número par!')
else:
    print('Este número é ímpar')

# 25. Conversão de Tipo com Validação
'''
Crie um script que solicite ao usuário uma lista de números separados por vírgula. 

O programa deve converter a string de entrada em uma lista de números inteiros. 

Utilize try-except para tratar a conversão de cada número e validar que cada 
elemento da lista convertida é um inteiro. 

Se a conversão falhar ou um elemento
não for um inteiro, imprima uma mensagem de erro. 

Se a conversão for bem-sucedida 
para todos os elementos, imprima a lista de inteiros.
'''
entrada = input('Digite uma lista(ex. 1,34,67,89):')
lista = list(entrada.split(','))
lista_int = []

try:
    for n in lista:
        lista_int.append(int(n))
    print('A lista convertida pra inteiros é:',lista_int)
except ValueError:
    print('Digite apenas números')

