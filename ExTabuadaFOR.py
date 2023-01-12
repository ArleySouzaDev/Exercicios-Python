#Tabuada usando for

num = int(input("Digite um número pra ver a tabuada: "))
print("======" *2)
for num2 in range(0,11):
    print("{} x {} = {}".format(num, num2, num*num2))
print("======" *2)