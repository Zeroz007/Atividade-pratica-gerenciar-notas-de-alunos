alunos = []

notas = []

alunos.append("Ana")
alunos.append("Bruno")
alunos.append("Carla")
alunos.append("Daniel")

notas.append([8, 7, 9])
notas.append([6, 8, 7])
notas.append([9, 10, 8])
notas.append([5, 6, 7]) 

print("=== NOTAS DOS ALUNOS ===")
for i in range(len(alunos)):
    print(f"Aluno: {alunos[i]}")
    print(f"Notas: {notas[i]}")
    print("-" * 20)

indice_aluno = 0 
nome_aluno = alunos[indice_aluno]
notas_aluno = notas[indice_aluno]

quantidade_notas = len(notas_aluno)
soma_notas = sum(notas_aluno)
media = soma_notas / quantidade_notas

print(f"\nMédia do aluno {nome_aluno}:")
print(f"Notas: {notas_aluno}")
print(f"Soma das notas: {soma_notas}")
print(f"Quantidade de notas: {quantidade_notas}")
print(f"Média: {media:.2f}")

print("\n=== MÉDIAS DE TODOS OS ALUNOS ===")
for i in range(len(alunos)):
    media_aluno = sum(notas[i]) / len(notas[i])
    print(f"{alunos[i]}: {media_aluno:.2f}")
