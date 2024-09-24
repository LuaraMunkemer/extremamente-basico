                                                                                                     
                                          '''
Jogo do Adivinhe o Número 
2024.07.30
Luara Munkemer Fornazari
'''
# Objetivo : Desenvolver um jogo, onde o usuário deverá tentar adivinhar um número secreto sorteado pelo PC

# Módulos e Bibliotecas
from random import randint

# Variáveis
msg = '' # Variável para msg 
numeroSecreto = 0 # usado para o sorteio do numero secreto

# COSTANTES
CAR = "=" # Caractere usado para desenhar a estrutura do jogo 
TDT = 50 # Tamanho da Tela a ser desenhada 
MAR = 2  # Margem de dois caracteres 
INI = 1
FIM = 100
TVS = 3

# Listas
listasMsgs = [] #Variaveis para lista de msg 

# Funções para mostrar uma linha de caracteres 
def mostrarLinha():
  print(CAR*TDT)

# Função para mostrar um texto centralizado entre um numero de caracteres 
def msgCentro(msg):
  print(f"{CAR} {msg:^{TDT-MAR-MAR}} {CAR}")

#
def cabecalho(Msg):
  mostrarLinha()
  for msg in listaMsgs:
    msgCentro(msg)
  mostrarLinha()


# Funçao para sortear o numero secreto
def sorteiaNum():
  numeroSecreto = randint(INI,FIM)
  return numeroSecreto

# Funcao para pegar a resposta e testar se é um numero
def pegaResposta():
  resposta = input(f"{CAR} Sua resposta: ")
  while not resposta.isdigit():
    listaMsgs = ["Resposta Inválida!", "Tente um Número!"]
    cabecalho(listaMsgs)
    resposta = input(f"{CAR} Sua resposta!")
  resposta = int(resposta)
  return resposta
  
# Funçao para dar a dica 
def dica(numeroSecreto, responda):
  if numeroSecreto > resposta:
    cabecalho("Tente um Número MENOR!")
  else:
    cabecalho("Tente um Número MAIOR!")
    
# Função para Startar o jogo
def startGame():
  TVS = 3
  numeroSecreto = sorteiaNum()
  listaMsgs = [" JOGO DO ADIVINHE O NÚMERO", "Powered by Luara"]
  cabecalho(listaMsg)
  playGame(TVS, numeroSecreto)

def playGame(TVS, numeroSecreto):
  for tentativas in range (TVS):
    resposta = pegaResposta()
    testeAcerto = resposta == numeroSecreto
    if testeAcerto:
      listaMsgs = ["OLOKO BIXO!!!", "ACERTOU MEMO!!!", "PARABENS YOU WIN!"]
    cabecalho(listaMsgs)
    break
elif tentativas != 2:
  listaMsgs = ["SE É RUIM +", "NÃO É ASSIM CRIATURA!"]
  cabecalho(listaMsgs)
  dica(numeroSecreto, resposta)
else:
  cabecalho("MelDels Que Feio!!! ")
else:
  listaMsgs = ["FIM DE JOGO" , "O NUM SECRETO ERA", numeroSecreto, "PARABENS YOU LOSE!"]
  cabecalho(listaMsgs)
  listaMsgs = ["Deseja Jogar Novamente?", "[0 - NÃO]", "[1 - SIM]"]
  cabecalho(listaMsgs)
  resposta = pegaResposta()
  if responda == 1:
    startGame()
  else:
    listaMsgs = ["FOI BOM JOGAR COM VOCE!" , "ATE A PROXIMA"]
    cabecalho(listaMsgs)
  
  


# Programa Principal



