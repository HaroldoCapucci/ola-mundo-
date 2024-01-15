#desenvolva um programa que tranforme a distancia digitada em quilomentros em metros.

from cgi import print_arguments


quilometro = float(input("digite a distancia em km: "))
print(f"vou converter a distacia {quilometro}, km em metros")

# desenvolvimento


calculo =(quilometro * 1000)

print(f"essa distancia é {calculo}, metros.")

