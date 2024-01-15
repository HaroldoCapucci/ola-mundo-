# faca um programa que calcule o Indice de Massa Corporea

peso = float (input ("Digite qual o seu peso, "))
altura = float (input("Digite qual a sua altura, "))


IMC = peso / (altura**2)

print(f"seu IMC é {IMC}")
