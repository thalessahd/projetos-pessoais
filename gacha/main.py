# -*- coding: utf-8 -*-
# Protótipo Gacha de Boku no Hero by Thalessa.

# Imports.
import random # Para gerar números aleatórios.
import os # Para usar limpa tela.

# Funções.
# Carrega linhas de um arquivo para uma lista.
def carrega_personagens(nome_arq,grau):
    arquivo = open(nome_arq)
    personagens = arquivo.readlines()
    aux = [] # Variável auxiliar.
    for p in personagens: # Remover os '\n' das palavras.
        aux.append(grau+"-"+p.strip())
    arquivo.close()
    return aux # Lista dos personagens sem '\n'.
# Dado um número, retorna um personagem de alguma lista dependendo desse número.   
def roleta(numero):
    if(numero<=3):
        resu = random.choice(ssr) # 3% [1,3]
    elif(numero>=4 and numero <=30): # 27% [4,30]
        resu = random.choice(sr)
    else: # 70% [31,100]
        resu = random.choice(r)
    return resu
# Adiciona personagem no dicionário, caso já exista incrementa a quantidade.
def adiciona_adquirido(dict,chave_adc):
    if chave_adc not in dict.keys():
        dict[chave_adc] = 1
    else:
        dict[chave_adc] = dict[chave_adc] + 1

def enter():
    input("Pressione ENTER para voltar.")
# Printa na tela os heróis já sorteados de forma ordenada SSR>SR>R.
def exibe_herois(dict):
    if len(dict)==0:
        print("Nenhum herói adquirido.")
    else:
        lista_chaves =[]
        chaves = dict.keys()
        for c in chaves:
            lista_chaves.append(c)
        lista_chaves.sort(reverse=True)
        
        for i, key in enumerate(lista_chaves):
            print("["+str(i+1)+"] "+key+" : "+str(dict[key]))
 
# Carregar personagens.
ssr = carrega_personagens("ssr.txt","SSR") 
sr = carrega_personagens("sr.txt","SR")
r = carrega_personagens("r.txt","R")
personagens_adquiridos = {} # Cria dicionário heróis adquiridos 

# Menu
while(1):
    os.system('cls') or None # Limpa tela.
    print("--Gacha de Boku no Hero--")
    print("1: Invocar 1x")
    print("2: Invocar 11x")
    print("3: Visualizar heróis adquiridos")
    print("0: Sair")
    op = input("Opção: ")
    os.system('cls') or None # Limpa tela
    if(op=="1"):
        sorteio = random.randint(1,100)
        sorteado = roleta(sorteio)
        adiciona_adquirido(personagens_adquiridos,sorteado)
        print("**Herói invocado**")
        print("[1] "+sorteado)
        enter()
    elif(op=="2"):
        print("**Heróis invocados**")
        for i in range(1,12,1):
            sorteio = random.randint(1,100)
            sorteado = roleta(sorteio)
            adiciona_adquirido(personagens_adquiridos,sorteado)
            print("["+str(i)+"] "+sorteado)
        enter()       
    elif(op=="3"):
        print("**Heróis adquiridos**")
        exibe_herois(personagens_adquiridos)
        enter()
    elif(op=="0"):
        print("Saindo..")
        break;
    else:
       print("Opção inválida!")
       enter()