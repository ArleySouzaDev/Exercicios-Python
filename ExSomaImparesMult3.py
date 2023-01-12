#Programa que calcule todos números impare
#divisivos por 3 no intervalo de 1 a 500.

soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 ==0:
        soma = soma + n
        cont = cont + 1
print("A soma de todos os {}  valores solicitados é {} ".format(cont, soma))