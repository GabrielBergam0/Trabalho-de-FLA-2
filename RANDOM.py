import random
#importando funcoes prontas

#------------------------------------------------------------------------------------------------------------------

contador = 0
#definindo uma variavel para marcar as 10 jogadas

#------------------------------------------------------------------------------------------------------------------

print("Seja bem vindo ao jogo...voce tem 10 chances para acertar uma senha de 5 digitos...boa sorte...")
#introducao

#------------------------------------------------------------------------------------------------------------------

while contador < 10:
    jogada1 = int(input("Digite o primeiro numero: "))
    while jogada1 < 1 or jogada1 > 9:
        print("numero invalido...")
        jogada1 = int(input("Digite o primeiro numero: "))

    jogada2 = int(input("Digite o segundo numero: "))
    while jogada2 < 1 or jogada2 > 9:
        print("numero invalido...")
        jogada2 = int(input("Digite o segundo numero: "))

    jogada3 = int(input("Digite o terceiro numero: "))
    while jogada3 < 1 or jogada3 > 9:
        print("numero invalido...")
        jogada3 = int(input("Digite o terceiro numero: "))

    jogada4 = int(input("Digite o quarto numero: "))
    while jogada4 < 1 or jogada4 > 9:
        print("numero invalido...")
        jogada4 = int(input("Digite o quarto numero: "))

    jogada5 = int(input("Digite o quinto numero: "))
    while jogada5 < 1 or jogada5 > 9:
        print("numero invalido...")
        jogada5 = int(input("Digite o quinta numero: "))
    #pedindo os digitos para o usuario

#------------------------------------------------------------------------------------------------------------------

    n1 = (random.randrange(1, 9))
    n2 = (random.randrange(1, 9))
    n3 = (random.randrange(1, 9))
    n4 = (random.randrange(1, 9))
    n5 = (random.randrange(1, 9))
    #inportando valores aleatorios ultilizando as funcoes importadas anteriormente

#------------------------------------------------------------------------------------------------------------------

    print ("seus numeros foram: ",jogada1,",",jogada2,",",jogada3,",",jogada4,",",jogada5,"...")
    print("ja os sorteados foram: ",n1,",",n2,",",n3,",",n4,",",n5,"...")
    #mostrando ao usuario os numeros gerados e digitados

#------------------------------------------------------------------------------------------------------------------

    if jogada1 == n1:
        print("+1")
    elif jogada1 == n2 or jogada1 == n3 or jogada1 == n4 or jogada1 == n5:
        print("+0")
    else:
        print("-1")
       
    if jogada2 == n2:
        print("+1")
    elif jogada2 == n1 or jogada2 == n3 or jogada2 == n4 or jogada2 == n5:
        print("+0")
    else:
        print("-1")

    if jogada3 == n3:
        print("+1")
    elif jogada3 == n1 or jogada3 == n2 or jogada3 == n4 or jogada3 == n5:
        print("+0")
    else:
        print("-1")

    if jogada4 == n4:
        print("+1")
    elif jogada4 == n1 or jogada4 == n3 or jogada4 == n2 or jogada4 == n5:
        print("+0")    
    else:
        print("-1")

    if jogada5 == n5:
        print("+1")
    elif jogada5 == n1 or jogada5 == n3 or jogada5 == n4 or jogada5 == n2:
        print("+0")
    else:
        print("-1")
    #checando os resultados

#------------------------------------------------------------------------------------------------------------------

    contador = contador + 1
    #mecanismo para controlar o numero de tentativas
