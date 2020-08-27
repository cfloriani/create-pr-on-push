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
title_pr = 'WIP: ' + num_issue + ' - ' + name_issue

print(title_pr)
print(name_issue)
print(num_issue)


# cria o pr
repo.create_pull(title='teste pr', body='teste', head='cfloriani:138-alteracoes-no-docker', base='master')

#repo.create_pull(title=title_pr, body='#' + num_issue, head=os.getenv('user') + ':' + name_issue, base='master')





# Titulo-> WIP: 5 Relatório saindo com caracteres inválidos
# Label -> pr: em andamento

# # creade a branch for issue
# branch_issue = os.getenv('issue_num') + '-' + slugify(os.getenv('issue'))
# repo.create_git_ref('refs/heads/{branch_issue}'.format(**locals()),repo.get_branch('master').commit.sha)

# # create extra branch for milestone feature:
# if str(os.getenv('milestone'))[0:7].lower() == "feature":
#     branch_milestone = slugify(os.getenv('milestone'))
#     repo.create_git_ref('refs/heads/{branch_milestone}'.format(**locals()),repo.get_branch('master').commit.sha)
