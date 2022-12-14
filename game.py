from PPlay.window import *
from PPlay.sprite import *

def game():

    # Inicia recursos
    janela = Window(800, 600)
    janela.set_title("RUN")
    fundo1 = Sprite("Sprites/game/gameplay_background.jpg")
    fundo2 = Sprite("Sprites/game/gameplay_background.jpg")
    player = Sprite("Sprites/game/char_run.png", 6)
    teclado = janela.get_keyboard()
    cont = 0
    
    # Inicia player
    player.x = janela.width/3
    player.y = janela.height - player.height
    player.set_sequence_time(0, 6, 2, True)

    jumpvel = 1000

    # Inicia obstaculos
    vettruck = []
    vetdrone = []

    # Inicia fundo
    fundo1.x = 0
    fundo2.x = fundo1.width

    while True:

        cont += janela.delta_time()

        if cont > 6.0:
            truck = Sprite("Sprites/game/obstacle_truck.png")
            truck.x = janela.width + truck.width
            truck.y = janela.height - truck.height
            vettruck.append(truck)
            cont = 0

        if teclado.key_pressed("ESC"):
            break

        # Movimento do background
        if fundo1.x + fundo1.width <= 0:
            fundo1.x = fundo2.width
        if fundo2.x + fundo2.width <= 0:
            fundo2.x = fundo1.width
        fundo1.x -= 100* janela.delta_time()
        fundo2.x -= 100* janela.delta_time()

        # Obstaculos se movem

        if len(vettruck) > 0:
            for i in range(len(vettruck)):
                if vettruck[i].x < 0 - truck.width:
                    vettruck.pop(i)
                    break

            for i in range(len(vettruck)):
                vettruck[i].x -= 200 * janela.delta_time()

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
        for i in range(len(vettruck)):
            vettruck[i].draw()
        janela.update()
