from PPlay.window import *
from PPlay.sprite import *
from random import randint

def game():

    # Inicia recursos
    janela = Window(800, 600)
    janela.set_title("RUN")
    fundo1 = Sprite("Sprites/game/gameplay_background.jpg")
    fundo2 = Sprite("Sprites/game/gameplay_background.jpg")
    player = Sprite("Sprites/game/char_run.png", 6)
    teclado = janela.get_keyboard()
    cont = 0
    contdif = 0
    contfps = 0
    fps = 0
    timerfps = 0
    points = 0
    dificuldade = 1.0
    gameover = False
    rank = open("rank.txt", "a")
    
    # Inicia player
    player.x = janela.width/3
    player.y = janela.height - player.height
    player.set_sequence_time(0, 6, 200, True)

    jumpvel = 600

    dead = False

    # Inicia obstaculos
    vettruck = []
    vetdrone = []

    # Inicia fundo
    fundo1.x = 0
    fundo2.x = fundo1.width

    # Game Loop
    while True:

        cont += janela.delta_time()
        contdif += janela.delta_time()
        timerfps += janela.delta_time()
        fps += 1

        # Cria inimigos
        if cont > 6.0/dificuldade:
            k = randint(0, 1)
            if k == 1:
                truck = Sprite("Sprites/game/obstacle_truck.png")
                truck.x = janela.width + truck.width
                truck.y = janela.height - truck.height
                vettruck.append(truck)
                cont = 0
            else:
                drone = Sprite("Sprites/game/obstacle_drone.png", 4)
                drone.x = janela.width + drone.width
                drone.y = janela.height/1.5 - drone.height
                drone.set_sequence_time(0, 4, 300, True)
                vetdrone.append(drone)
                cont = 0

        if contdif > 15.0 * dificuldade:
            dificuldade += 0.5
            contdif
        
        if timerfps > 1.0 and gameover == False:
            contfps = fps
            points += 10 * dificuldade
            fps = 0
            timerfps = 0

        # Movimento do background
        if fundo1.x + fundo1.width <= 0:
            fundo1.x = fundo2.width
        if fundo2.x + fundo2.width <= 0:
            fundo2.x = fundo1.width
        fundo1.x -= 100* janela.delta_time() * dificuldade
        fundo2.x -= 100* janela.delta_time() * dificuldade

        # Colisão player/obstaculo

        if len(vettruck) > 0:
            for i in range(len(vettruck)):
                if player.collided(vettruck[i]) and gameover == False:
                    player.hide()
                    gameover = True
                    dead = True
                    points = str(points)
                    rank.write(points + "\n")
                    break
            if dead:
                break

        if len(vetdrone) > 0:
            for i in range(len(vetdrone)):
                if player.collided(vetdrone[i]) and gameover == False:
                    player.hide()
                    gameover = True
                    dead = True
                    points = str(points)
                    rank.write(points + "\n")
                    break
            if dead:
                break

        # Obstaculos se movem

        if len(vettruck) > 0:
            for i in range(len(vettruck)):
                if vettruck[i].x < 0 - truck.width:
                    vettruck.pop(i)
                    break

            for i in range(len(vettruck)):
                vettruck[i].x -= 200 * janela.delta_time() * dificuldade

        if len(vetdrone) > 0:
            for i in range(len(vetdrone)):
                if vetdrone[i].x < 0 - drone.width:
                    vetdrone.pop(i)
                    break

            for i in range(len(vetdrone)):
                vetdrone[i].x -= 200 * janela.delta_time() * dificuldade

        # Movimento player
        if player.x < 0:
            player.x = 0
        if player.x > janela.width - player.width:
            player.x = janela.width - player.width

        player.move_key_x(400* janela.delta_time())

        if player.y > janela.height - player.height:
            jumpvel = 600
            player.y = janela.height - player.height

        if player.y < janela.height - player.height:
            jumpvel -= 2
            player.y -= jumpvel * janela.delta_time()

        if teclado.key_pressed("space") and (player.y == janela.height - player.height):
            jumpvel = 600
            player.y -= jumpvel * janela.delta_time()



        fundo1.draw()
        fundo2.draw()
        player.update()
        player.draw()
        for i in range(len(vetdrone)):
            vetdrone[i].update()
            vetdrone[i].draw()
        for i in range(len(vettruck)):
            vettruck[i].draw()
        janela.draw_text(("FPS: %d" % contfps), janela.width - 100, 20, 16, (255, 255, 255), "Arial", True, False)
        janela.draw_text(("Points: %d" % points), 20, 20, 16, (255, 255, 255), "Arial", True, False)
        janela.update()
