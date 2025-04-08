# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

str = input("Digite uma palavra pra convertê-la pra maiúscula: ")

def conv_maiuscula(a):
    return  a.upper()

str_maiuscula = conv_maiuscula (str)
print(f'{str} convertido pra maíusculo é {str_maiuscula}.')
('\n')

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
str_mn = input("Digite uma palavra pra convertê-la pra minúscula: ")

def conv_minuscula(b):
    return  b.lower()

str_minuscula = conv_minuscula (str_mn)
print(f'{str_mn} convertido pra minúsculo é {str_minuscula}.')
('\n')


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input('Digite uma frase: ')
print(f'A frase sem espaço no início e no final fica assim: {frase.strip()}')
print(frase.strip())
('\n')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('Digite uma data no formato dd/mm/aaaa: ')
data_sep = data.split('/')
print(data_sep[0])
print(data_sep[1])
print(data_sep[2])
('\n')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str_1 = input('Digite uma frase: ')
str_2 = input('Digite outra frase: ')

frases_juntas = str_1 + str_2

print(f'As frases {str_1} e {str_2} juntas fica assim: {frases_juntas}')
