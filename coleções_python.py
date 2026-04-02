#Coleções no python são estruturas de dados que guardam mais de um valor. 
#append = adiciona o input APENAS na lista do ultimo print. Ex: frutas.append(pedido_pdt) 
#insert = adiciona o input no local escolhido na lista do ultimo print. Ex: frutas.insert(0, 3) Obs: número após a virgula sempre na lógica do posição 
#remove = remove o item mencionado na sintaxe tirando ele apenas do ultimo print. print()
#pop = usa lógica do index e retorna o item que foi removido da lista. Ex: frutas.pop()
#clear = limpa a lista por completo no ultimo print. Ex: frutas.clean()
#copy = copia a variavel indiciada;
frutas = ['Maçã', 'Melão', 'Uva', 'Maracuja', 'Mamão', 'Laranja', 'Pera']
nomes = ['Maicon', 'Milena', 'Katness', 'Gustavo', 'Bia', 'Gabriel', 'Aline']

pedido_fruta = str(input("Digite a fruta que queira adicionar na lista: "))
frutas.append(pedido_fruta)
print(frutas)