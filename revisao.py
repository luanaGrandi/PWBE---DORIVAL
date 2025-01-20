#Exercicio 1
'''num1 = 10
num2 = 10

soma = num1 + num2
print(f"A soma de {num1} + {num2} é igual a: {soma} ")'''


# Exercicio 2
'''nome = str(input("Digite seu nome: "))
ano = int(input("Digite seu ano de nascimento: "))

idade = 2025 - ano
print(f"Olá {nome}, sua idade é: {idade} anos")
'''
#################################################################

# exercicio de IF, ELSE E ELIF

# Exercicio 1
'''num = int(input("Digite um numero: "))

if num % 2 == 0:
    print(f"O numero {num} é par")
else:
    print(f"O numero {num} é impar")'''

# Exercicio 2

'''nota1 = float(input("Digite sua 1 nota: "))
nota2 = float(input("Digite sua 2 nota: "))
nota3 = float(input("Digite sua 3 nota: "))
nota4 = float(input("Digite sua 4 nota: "))
nota5 = float(input("Digite sua 5 nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(F"\nSua media é: {media}")

if media >= 5:
    print("APROVADO")
elif media >= 2.5 and media < 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")'''


###################################################################

# Exercicio de FOR E WHILE

# Exercicio 1
'''num = int(input("Digite um numero: "))

for i in range(0 ,num + 1):
    print(i)'''

# Exercicio 2
'''maior = 0
num = 0
while num >= 0:
    num = int(input("Digite um numero: "))
    if num > maior:
        maior = num
print(f"O numero maior é: {maior}")   
'''
########################################################################

# Exercicio de FUNÇÕES DEF

# Exercicio 1

'''def  inverter_string(s):
    invertido = ''
    for i in s:
      invertido = i + invertido
      #(ou invertido += s[i])
    print(invertido)
   
inverter_string("Luana")'''


# Exercicio 2

def contar_caracteres(s):
    dicionario = {}
    for i in s:
        if i  in dicionario:
            dicionario[i] += 1
        else: 
            dicionario[i] = 1
    print(dicionario)

contar_caracteres("banana")
