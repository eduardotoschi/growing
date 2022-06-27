print('Selecione o número da operação desejada:')


print('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')

tipo = int(input('Digite sua opção(1/2/3/4): '))


 

a=int(input("Digite o primeiro número:"))
b=int(input("Digite o segundo número:"))

if tipo == 1:
    print ( a + b)
elif tipo == 2:
    print ( a - b)
elif tipo == 3:
    print ( a * b)
elif tipo == 4:
    print ( a / b)
else:
    print("operação não suportada")