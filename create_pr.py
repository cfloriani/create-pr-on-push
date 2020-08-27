from github import Github
import sys, os

# connet in repository
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

# pega o nome da issue
name_issue = os.getenv('ref')[11:]

#pega o numero da issue
for cont in range(0,len(name_issue)):
    if name_issue[cont] == '-':
        num_issue = name_issue[:cont]
        break

# cria o nome do pr
title_pr = 'WIP: ' + name_issue

# cria o pr
try:
    repo.create_pull(title=title_pr, body='#' + num_issue, head=os.getenv('user') + ':' + name_issue, base='master')
    repo.create_label(name='bug',color='#e53242')
except Exception as erro:
    print('ERRO: Aconteceu o erro abaixo')
    print(erro)    
