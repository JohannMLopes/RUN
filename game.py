from PPlay.window import *
from PPlay.sprite import *

def game():

    # Inicia recursos
    janela = Window(800, 600)
    janela.set_title("RUN")
    fundo1 = Sprite("Sprites/game/gameplay_background.jpg")
    fundo2 = Sprite("Sprites/game/gameplay_background.jpg")
    player = Sprite("Sprites/game/char_run.png", 7)
    teclado = janela.get_keyboard()
    
    # Inicia player
    player.x = janela.width/3
    player.y = janela.height - player.height
    player.set_sequence_time(0, 5, 3, True)

    jumpvel = 1000

    # Inicia obstaculos
    vettruck = []
    vetdrone = []

    # Inicia fundo
    fundo1.x = 0
    fundo2.x = fundo1.width

    while True:
        print("Altura do player: ", player.y + player.height)
        if teclado.key_pressed("ESC"):
            break

        if fundo1.x + fundo1.width <= 0:
            fundo1.x = fundo2.width
        if fundo2.x + fundo2.width <= 0:
            fundo2.x = fundo1.width
        fundo1.x -= 100* janela.delta_time()
        fundo2.x -= 100* janela.delta_time()

        if player.x < 0:
            player.x = 0
        if player.x > janela.width - player.width:
            player.x = janela.width - player.width

        player.move_key_x(400* janela.delta_time())

        if player.y > janela.height - player.height:
            jumpvel = 1000
            player.y = janela.height - player.height

        if player.y < janela.height - player.height:
            jumpvel -= 2
            player.y -= jumpvel * janela.delta_time()

        if teclado.key_pressed("space") and (player.y == janela.height - player.height):
            jumpvel = 1000
            player.y -= jumpvel * janela.delta_time()



        fundo1.draw()
        fundo2.draw()
        player.update()
        player.draw()
        janela.update()
