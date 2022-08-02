import math

xb = float(input("Digite o primeiro x de b plano cartesiano: "))
xa = float(input("Digite o segundo x de a plano cartesiano: "))
yb = float(input("Digite o primeiro y do b plano cartesiano: "))
ya = float(input("Digite o segundo y do a plano cartesiano: "))

d = ((xb - xa) ** 2 + (yb - ya) ** 2)**0.5

if d >=10:
    print("Longe")
else:
    print("perto")