alunos = {
    "João": [8, 7, 9],
    "Maria": [16, 19, 18],
    "Ana": [19, 18, 20]
}

alunoPesquisar = input("Aluno para pesquisar a média: ")

if alunoPesquisar in alunos:
    somaNotas = sum(alunos[alunoPesquisar])
    quantidadeNotas = len(alunos[alunoPesquisar])
    mediaNotas = somaNotas / quantidadeNotas

    print("Média:", mediaNotas)

else:
    print("Aluno não encontrado")