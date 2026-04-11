atletas = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
permissao_medica = True
condicionamento_fisico = True

if idade >= 18 and idade <= 35 and permissao_medica == True and condicionamento_fisico == True or idade >= 18 and idade <= 35 and permissao_medica == True and condicionamento_fisico == False:
    print("Usuario apto as atividades da competição!. ")
else:
    print("Usuario inapto as atividades.")