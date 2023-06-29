import os
import pygame
from tkinter import simpledialog
from funcoes import menu

pygame.init()

branco = (255,255,255)
fonte = pygame.font.Font(None, 22)
fonte2 = pygame.font.Font(None, 25)

tamanhoTela = (800,420)
tela = pygame.display.set_mode(tamanhoTela)
fundo = pygame.image.load("espaco.png")
tela.blit(fundo, (0,-10))
pygame.display.flip()

pygame.display.set_caption("Space Marker")

icone = pygame.image.load("foguete.png")
pygame.display.set_icon( icone )

pygame.mixer.music.load("musicaFundo.mp3")
pygame.mixer.music.play(-1)

menu()

listaEstrelas = []

dicionario = {}

running = True

while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arquivo = open("estrelas.txt", "w")
            arquivo.write(str(dicionario))
            arquivo.close()
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            arquivo = open("estrelas.txt", "w")
            arquivo.write(str(dicionario))
            arquivo.close()
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            posicao = pygame.mouse.get_pos()
            item = simpledialog.askstring("Estrela", "Nome da estrela:")
            estrela = (item , posicao)
            #print(estrela) para ver no cmd#
          
            if item == '':
                posicaoParaTexto = [str(elemento) for elemento in posicao]
                texto = ', '.join(posicaoParaTexto)
                item = "Desconhecido (" + texto + ")"
                #print(item) ver no cmd#
                itemTela = fonte.render(item, True, branco)
                tela.blit(itemTela , posicao)
                pygame.display.flip()
                
            elif item == None:
                pass

            else:
                estrelaTela = fonte.render(item, True, branco)
                tela.blit(estrelaTela, posicao)
                pygame.draw.circle(tela, branco, posicao, 3)
                    
            pygame.display.flip()
            
            if item != None:
                listaEstrelas.append(item)
                listaEstrelas.append(posicao)
                #print(listaEstrelas) para visualização no cmd#

            estrella = listaEstrelas[0::2]
            posiccao = listaEstrelas[1::2]
            dicionario = dict(zip(estrella, posiccao))
            print(dicionario)

        elif len(dicionario) >= 2:
                
            posicaoInicial = list(dicionario.values())[-2]
            posicaoFinal = list(dicionario.values())[-1]

            # Desenha uma linha entre os dois pontos
            pygame.draw.line(tela, branco, posicaoInicial, posicaoFinal, 1)
            pygame.display.flip()
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            arquivo = open("estrelas.txt", "w")
            arquivo.write(str(dicionario))
            arquivo.close()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            try:
                arquivo = open("estrelas.txt", "r")
                conteudo = arquivo.read()
                arquivo.close()
                dicionario = eval(conteudo)
            except:
                naoCarregou = fonte2.render("Não foi possível carregar :c", True, branco)
                tela.blit(naoCarregou, (100,100))
                pygame.display.flip()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            try:
                if os.path.exists("estrelas.txt"):
                    os.remove("estrelas.txt")
                    listaEstrelas = []
                    dicionario = {}
                    tela.blit(fundo, (0,-10))
                    menu()
                    pygame.display.flip()

            except:
                naoDeletou = fonte2.render("Não há progresso salvo!", True, branco)
                tela.blit(naoDeletou, (100,100))
                pygame.display.flip()
        

        
