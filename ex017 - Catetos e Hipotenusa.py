import math
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hip = math.hypot(co, ca)
print(f"A hipotenusa é {hip:.2f}")
