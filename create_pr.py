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

# # cria o pr
try:
    repo.create_pull(title=title_pr, body='#' + num_issue, head=os.getenv('user') + ':' + name_issue, base='master')
    for pull_request in repo.get_pulls(state='open'):
        if pull_request.title == title_pr:
            pr = repo.get_pull(pull_request.number)
            pr.add_to_labels('pr: em andamento')
            break
except Exception as erro:
    print('ERRO: Aconteceu o erro abaixo')
    print(erro)


pr = repo.get_pulls()
pr.add_to_labels('pr-teste')
print(pr.labels)
for label in pr.get_labels():
    print(label.name)