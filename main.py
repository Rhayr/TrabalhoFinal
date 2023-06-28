import pygame
from tkinter import simpledialog
from funcoes import menu

pygame.init()

branco = (255,255,255)
fonte = pygame.font.Font(None, 22)
fonte2 = pygame.font.Font(None, 25)

#tela/fundo
tamanhoTela = (800,420)
tela = pygame.display.set_mode(tamanhoTela)
fundo = pygame.image.load("espaco.png")
tela.blit(fundo, (0,-10))
pygame.display.flip()

#nome
pygame.display.set_caption("Space Marker")

#icone
icone = pygame.image.load("foguete.png")
pygame.display.set_icon( icone )

#música de fundo 
pygame.mixer.music.load("musicaFundo.mp3")
pygame.mixer.music.play(-1)

#menu
menu()

#lista estrelas

listaEstrelas = []

#Dicionário para guardar a lista das estrelas

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
                #de tupla para lista, de lista para string
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
            #Adicionando à lista
            if item != None:
                listaEstrelas.append(item)
                listaEstrelas.append(posicao)
                print(listaEstrelas) #para visualização no cmd#

            #adicionando ao dicionário, após adicionar na lista#
            estrella = listaEstrelas[0::2]
            posiccao = listaEstrelas[1::2]
            dicionario = dict(zip(estrella, posiccao))
            print(dicionario)

        if len(dicionario) >= 2:
                
            posicaoInicial = list(dicionario.values())[-2]
            posicaoFinal = list(dicionario.values())[-1]

                # Desenha uma linha entre os dois pontos
            pygame.draw.line(tela, branco, posicaoInicial, posicaoFinal, 1)
            pygame.display.flip()
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            try:
                arquivo = open("estrelas.txt", "w")
                arquivo.write(str(dicionario))
                arquivo.close()
            except:
                naoSalvou = fonte2.render("Não foi possível salvar :c", True, branco)
                tela.blit(naoSalvou, (100,100))
                pygame.display.flip()
        

        
