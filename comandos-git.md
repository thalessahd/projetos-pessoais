# Comandos Git
> coleção de comandos do Git

## Gerais
`git init` _//iniciar git_  
`git add <file_name>`  
`git add *` _//todos os arquivos_  
`git rm <file_name>`  
`git diff <codigo_versão>`  
`git reset <codigo_versão>`  
`git status`  

## Commit
`git commit -m "msg"`  
`git commit --amend ` _//editar msg do commit mais recente (abre um editor)_  
`git commit --amend -m "msg"` _//editar msg do commit mais recente_  
`git commit --amend --no-edit` _//O sinalizador --no-edit permitirá que você faça a emenda no seu commit sem alterar a mensagem do commit dele. (usado quando faz commit mas esqueceu de add algum arquivo. Então faz o add do arquivo que falta e dá esse comando)_  

## Checkout/Branchs
`git checkout -- <file_name>`  
`git checkout <nome_branch>`  
`git checkout <codigo_commit>`  
`git checkout <codigo_commit> -b <nome_branch>`  
`git branch` _//listar branchs_  
`git branch -d <nome_local_branch>` _//deletar local branch_  

## Log
`git log`  
`git log --graph` _//git log com pipe vermelho do ladinho_  
`git log --graph --all` _//mostra todos os commits_  

## Stash
`git stash` _//pra fazer o stash_  
`git stash list` _//pra listas os stashs feitos_  
`git stash apply` _//recuperar TODOS stash_  
`git stash apply stash@{<id>}` _//recuperar stash pelo id_  
`git stash drop stash@{<id>}` _//dropar stash pelo id_  

## GitHub
`git remote add <nome> <link_repositorio>` _//conectar git local com git remoto_  
`git push -u origin <nome_branch>`  
`git push origin master`  
`git pull origin master`  
`git clone <link_repositorio>`  


