#frase repeticao

frase = input("digite sua frase, ")
numero = int(input("digite o numero de vezes que repetirá sua frase "))
inicio = int(0)
while inicio <= numero:
    print(inicio, frase)
    inicio += 1