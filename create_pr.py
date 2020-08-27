from github import Github
from slugify import slugify
import sys, os

# connet in repository
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

title_pr = os.getenv('issue_num') + ' - ' + os.getenv('issue')

repo.create_pull(title='WIP: ' + title_pr, body='#' + os.getenv('issue_num'), head=os.getenv('user') + ':' + os.getenv('issue_num') + '-' + slugify(os.getenv('issue')), base='master')



# Titulo-> WIP: 5 Relatório saindo com caracteres inválidos
# Label -> pr: em andamento

# # creade a branch for issue
# branch_issue = os.getenv('issue_num') + '-' + slugify(os.getenv('issue'))
# repo.create_git_ref('refs/heads/{branch_issue}'.format(**locals()),repo.get_branch('master').commit.sha)

# # create extra branch for milestone feature:
# if str(os.getenv('milestone'))[0:7].lower() == "feature":
#     branch_milestone = slugify(os.getenv('milestone'))
#     repo.create_git_ref('refs/heads/{branch_milestone}'.format(**locals()),repo.get_branch('master').commit.sha)
