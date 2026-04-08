numeros = [1, 2, 3, 4]
print(numeros)

add_numeros = int(input("Digite o numero que deseja adicionar: "))
numeros.append(add_numeros)
print(numeros)

delete_numeros = int(input("Digite o numero que deseja deletar: "))
numeros.remove(delete_numeros)
print(numeros)

switch_numeros = int(input("Digite o numero que deseja substituir: "))
numeros.insert(3, switch_numeros)
print(numeros)

numeros.pop(2)
print(numeros)

numeros.sort(reverse=True)
print(numeros)