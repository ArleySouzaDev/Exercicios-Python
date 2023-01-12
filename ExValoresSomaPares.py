#Numeros pares somaos e impares ignorados

cont=0
soma=0
for num in range(0,7):
    num = int(input("Digite um número: "))
    if num % 2==0:
        soma += num
        cont += 1
print("Você informou {} números e a soma foi {}".format(cont, soma))
    
        