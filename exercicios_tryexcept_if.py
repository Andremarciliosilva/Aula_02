# 21. Conversor de Temperatura

'''
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
'''

'''
print("Digite uma temperatura em Celsius pra converter pra Farenheit")
try:
    temp_celsius = float(input("Digite a temperatura em Celsius:"))
    conv_farenheit = (temp_celsius * 9/5) + 32
    print(f"A temperatura convertida pra Farenheit é {conv_farenheit:.2f} °F.")

except ValueError:
    print('Por favor, digite apenas números')
'''


# 22. Verificador de Palíndromo
'''Crie um programa que verifica se uma palavra ou frase é um palíndromo 
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize if para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''
'''
entrada = input('Digite uma palavra pra verificar se é um palíndromo: ')

if (isinstance(entrada, str)) and not entrada.isnumeric():
    entrada_rev = entrada [::-1]
    if entrada == entrada_rev:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
else:
    print('Digite apenas palavras.')

'''

# 23. Calculadora Simples
'''Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
Use try-except para lidar com divisões por zero e entradas não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
Imprima o resultado ou uma mensagem de erro apropriada.'''


try: 
    numero_1 = int(input('Digite o primeiro número: '))
        
except ValueError:
    print('Digite apenas números')
    teste = True

try: 
    numero_2 = int(input('Digite o segundo número: '))

except ValueError:
    print('Digite apenas números')

operador = input('Digite a operação que deseja fazer (+ = soma / - = subtração / / = divisão ou * = multiplicação): ')


if operador == '+':
    soma = numero_1 + numero_2
    print('O resultado da soma é: ', soma)

elif operador == '-':
    subtracao = numero_1 - numero_2
    print('O resultado da subtração é: ', subtracao)

elif operador == '*':
    multiplicacao = numero_1 * numero_2
    print('O resultado da multiplicação é: ', multiplicacao )

try:
 operador == '/'
 divisao = numero_1 / numero_2
 print('O resultado é: ', divisao)
except ZeroDivisionError:
    print('Não se pode dividir por 0')

    








# 24. Classificador de Números
# 25. Conversão de Tipo com Validação
