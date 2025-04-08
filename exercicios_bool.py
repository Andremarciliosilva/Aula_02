# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
print('Digite False ou True pra saber o resultado de uma operação AND')
entrada1 = input('Digite False ou True: ')
entrada2 = input('Digite False ou True: ')

resultado1 = entrada1 and entrada2
print('O resultado é', resultado1)
('\n')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print('Digite False ou True pra saber o resultado de uma operação OR')
entrada1_1 = input('Digite False ou True: ')
entrada2_2 = input('Digite False ou True: ')

resultado1_2 = entrada1_1 or entrada2_2
print('O resultado da operação OR é:', resultado1_2)
('\n')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print('Digite False ou True pra saber o valor invertido')
entrada1_3 = input('Digite False ou True: ')

if entrada1_3 == 'True':
    print('O resultado é False')
          
else:
    print('O resultado é True')
('\n')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print('Digite dois números pra saber se eles são iguais:')
entrada1_4 = input('Digite o primeiro número: ')
entrada2_4 = input('Digite o segundo: ')

if entrada1_4 == entrada2_4:
    print('Os números são iguais')

else:
    print('Os números são diferentes')
('\n')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print('Digite dois números pra saber se eles são diferentes:')
entrada1_4 = input('Digite o primeiro número: ')
entrada2_4 = input('Digite o segundo número: ')

if entrada1_4 != entrada2_4:
    print('Os números são diferentes')

else:
    print('Os números são iguais')