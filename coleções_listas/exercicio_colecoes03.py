#Criando um dicionario focado no tema aluno 
#nome: Maria
#idade: 20
#curso: engenharia

aluno = {'Nome':'Maria','Idade':'20','Curso':'Engenharia'}
print(aluno)

#Agora realizando solicitações do exercicio.

aluno['Nota'] = '9,5'
print()
print(aluno)

aluno['Idade'] = '21'
print()
print(aluno)

aluno.pop('Curso')
print()
print(aluno)

aluno['Cursos'] = ['Engenharia de Software' , 'Engenharia de Computação', 'Ciência da Computação']
print()
print(aluno)

print()
print('Fim')