#variavel para o usuario escrever a cidade que ele quer verificar
cidade_temperatura = str(input("Digite a cidade que deseja verificar: "))
temperatura = 11 #variavel que define a temperatura do local indicado!
#schema de condições para exibir mensagens baseadas na temperatura
if temperatura >= 30.0:
    print(cidade_temperatura + " está fazendo bastante calor!")
elif 7.0 <= temperatura <= 12.0:
    print(cidade_temperatura +" está fazendo bastante frio!")
else:
    print("Está num clima normal em " + cidade_temperatura + ".")