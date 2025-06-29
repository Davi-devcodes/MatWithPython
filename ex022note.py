f = "Curso em vídeo Python"

# Conta as quantidades de caracteres
print(len(f))

# Conta as quantidades de vezes que aparece a letra digitada
print(f.count("o"))

# Conta as quantidades de vezes que aparece a letra digitada no espaço escolhido
print(f.count("o",0,13))

# Procura onde está a palavra digitada
print(f.find("deo"))

# Mesma coisa, porém se não achar, retorna o valor -1
print(f.find("Android"))

# Ver se a palavra digitada existe na frase
print("Curso" in f)

# Transforma uma palavra existente na frase por outra digitada
print(f.replace("Python","Android"))

# Transforma as palavras minúsculas em maiúsculas
print(f.upper())

# O contrário do upper
print(f.lower())

# Tirar espaços inúteis
print(f.strip())

# Se quiser tirar só o da direita
print(f.rstrip())

# O da esquerda
print(f.lstrip())

# Dividir uma string
print(f.split())

# Junta a frase
print("-".join(f))


























