import pygame
pygame.init()

fonte = pygame.font.Font(None, 22)
branco = (255,255,255)

tamanhoTela = (800,420)
tela = pygame.display.set_mode(tamanhoTela)
fundo = pygame.image.load("espaco.png")
tela.blit(fundo, (0,-10))
pygame.display.flip()

def menu():
    menu = fonte.render("Pressione S para Salvar os pontos [S]", True, branco)
    menu_posicao = (5,10)
    tela.blit(menu, menu_posicao)
    menu2 = fonte.render("Pressione C para Carregar os pontos [C]", True, branco)
    menu_posicao2 = (5,28)
    tela.blit(menu2, menu_posicao2)
    menu3 = fonte.render("Pressione D para Deletar os pontos [D]", True, branco)
    menu_posicao3 = (5,44)
    tela.blit(menu3, menu_posicao3)
    pygame.display.flip()