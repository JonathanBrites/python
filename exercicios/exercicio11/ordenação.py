num1 = int(input("Digite o primeiro x do plano cartesiano: "))
num2 = int(input("Digite o segundo x do plano cartesiano: "))
num3 = int(input("Digite o primeiro y do plano cartesiano: "))
num4 = int(input("Digite o segundo y do plano cartesiano: "))

d = ((num1 - num2) ** 2) + ((num3 - num4) ** 2)

if d >= 10:
    print("Longe")
else:
    print("perto")