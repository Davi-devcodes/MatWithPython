import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
l = [n1, n2, n3, n4]
random.shuffle(l)
print(f"A ordem da apresentação será:{l}")
