#Leia o primeiro termo de uma PA e mostre
#os 10 primeiros termos dessa progressão


primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c))
print("Fim")
