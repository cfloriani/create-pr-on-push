
# entrada
teste = 'refs/heads/138-alteracoes-no-docker'


nome_issue = teste[11:]

for cont in range(0,len(nome_issue)):
    if nome_issue[cont] == '-':
        num_issue = nome_issue[:cont]
        break

print(num_issue)
print(nome_issue)