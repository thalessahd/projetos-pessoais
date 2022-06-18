# Comandos Docker
> coleção de comandos do Docker

## Docker compose
`docker-compose down` _//Stops containers and removes containers, networks, volumes, and images created by up_ 

## Gerais
`docker version`  
`docker ps` _//lista containers ativos_  
`docker ps -a` _//lista todos os containers da máquina_  
`docker start <id_container>`  
`docker start <nome_container>`  
`docker logs <nome_container>` _//comando de debug_  
`docker image ls` _//listar todas as imagens da máquina_  
`docker system prune` _//remove tudo que não está sendo utilizado_

## Run
`docker run -it <nome_imagem>` _//-it para rodar terminal_  
`docker run -d <nome_imagem>` _//executa em background_    
`docker run -p <porta_pc>:<porta_docker> <nome_imagem>` _//executar definindo a porta_  
`docker run -d -p <porta_pc>:<porta_docker> --name <nome_para_o_container> <nome_imagem>` _//--name define um nome de minha escolha_  
`docker stop <id_container>` _//parar a execução_

### Exemplos
`docker run -p 80:80 <nome_imagem>` _//primeiro 80 porta padrão de acesso web, segunda porta 80 porta do container_  
`docker run -d -p 80:80 nginx`  
`docker run -d -p 80:80 --name nginx-docker nginx`  
`docker run -p 3000:3000 -d 8b57744bf77f` _//nesse caso esse id é da imagem que acabei de criar com o Dockerfile_  
> localhost:3000 //acesso a página que criei

## Build
`docker build .` _//pode usar o ponto caso tenha um Dockerfile no diretório onde o comando foi executado. Isso serve para buildar uma imagem_  
`docker build -t <nome_para_minha_imagem> .`

### Exemplos
`docker build -t node-docker-image .`  

## Remover
`docker rm <id_container>`  
`docker rm <nome_container>`  
`docker rmi <nome_imagem>` _//remover imagem_  
`docker rmi <id_imagem>`  

### Exemplo
`docker rmi node-docker-image`

---

## Exemplo de imagens
* ubuntu
* node
