# crie um programa que verifique se a idade digitado pode ou nao tirar habilitacao


idade = int(input("digite sua idade "))
print(type(idade))

if idade > 18:
    print("voce ja pode iniciar as etapas de credenciamento habilitacional")
elif idade < 18:
    print("espere e logo voce podera comecar suas etapas ")
else:
    print("voce tem 18 anos e imginamos que esta querendo muito isso... parabens!!!")


