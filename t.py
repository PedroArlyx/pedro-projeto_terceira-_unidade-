alunos=[['pedro','arlyx'],['jose','antonio']]
file= open ('inscrito','w')
for c in range(len(alunos)):
    nome = input('digite')
    alunos.append([nome])
    file.write(nome+ '\n')
print(alunos)
file.close()