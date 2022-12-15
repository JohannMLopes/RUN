from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from game import game


# Inicia recursos

janela = Window(800, 600)
janela.set_title("RUN")
fundo = GameImage("Sprites/menu/menu_backscreen.jpg")
play = Sprite("Sprites/menu/play.jpg")
ranking = Sprite("Sprites/menu/ranking.jpg")
sair = Sprite("Sprites/menu/sair.jpg")
rank = open("rank.txt", "a")
mouse = janela.get_mouse()

play.x = janela.width/2 - play.width/2
play.y = janela.height/2 - play.height/2

ranking.x = janela.width/2 - ranking.width/2
ranking.y = play.y + ranking.height/2 + play.height

sair.x = janela.width/2 - sair.width/2
sair.y = ranking.y + sair.height/2 + ranking.height

while True:

    if mouse.is_over_area((sair.x, sair.y), (sair.x + sair.width, sair.y + sair.height)) and mouse.is_button_pressed(1):
        break

    if mouse.is_over_area((play.x, play.y), (play.x + play.width, play.y + play.height)) and mouse.is_button_pressed(1):
        game()

    fundo.draw()
    play.draw()
    ranking.draw()
    sair.draw()
    janela.update()