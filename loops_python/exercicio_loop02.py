#Exercicio 02 - Crie um simulador de tabuada, onde o jogador digita um número, e a tabuada desse número é exibida.

numero = int(input('Digite um valor para ver a tabuada: ')) #variavel para receber o valor do input que o usuario deseja.
numero_tabuada = 0 #variavel para receber o valor do numero da tabuada, que vai iniciar com 0 e ir aumentando ate chegar a 10.
while numero_tabuada <= 9:
    numero_tabuada += 1
    resultado = numero * numero_tabuada
    print(f'{numero} x {numero_tabuada} é igual a: {resultado}')