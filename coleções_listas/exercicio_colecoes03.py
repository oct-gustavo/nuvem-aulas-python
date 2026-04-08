#Criando um dicionario focado no tema aluno 
#nome: Maria
#idade: 20
#curso: engenharia

aluno = {

    'Nome':'Maria',
    'Idade': '20',
    'Curso':'Engenharia'
}
print(aluno)

#Agora realizando solicitações do exercicio.

aluno.setdefault('Nota', 9.5)
print(aluno)