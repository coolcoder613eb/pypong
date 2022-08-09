import pygame as pg
from paddle import Paddle
from ball import Ball

pg.init()

black = (0,0,0)
white = (255,255,255)

screen = pg.display.set_mode((700,500))
pg.display.set_caption('Pong')

paddleA = Paddle(white, 10, 100)
paddleA.rect.x = 5
paddleA.rect.y = 200

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = 685
paddleB.rect.y = 200

ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

asl = pg.sprite.Group()

asl.add(paddleA)
asl.add(paddleB)
asl.add(ball)

carryon = True

clock = pg.time.Clock()

sa = 0
sb = 0

while carryon:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            carryon = False
        elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_x: #Pressing the x Key will quit the game
                         carryOn=False  

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        paddleA.moveup(5)
    if keys[pg.K_s]:
        paddleA.movedown(5)
    if keys[pg.K_UP]:
        paddleB.moveup(5)
    if keys[pg.K_DOWN]:
        paddleB.movedown(5)  

    asl.update()

     #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        sa += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        sb += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    if pg.sprite.collide_mask(ball, paddleA) or pg.sprite.collide_mask(ball, paddleB):
        ball.bounce()        

    screen.fill(black)
    pg.draw.line(screen, white, [349, 0], [349, 500], 5)
    asl.draw(screen)

    #Display scores:
    font = pg.font.Font('slkscr.ttf', 78)
    text = font.render(str(sa), 1, white)
    screen.blit(text, (250,10))
    text = font.render(str(sb), 1, white)
    screen.blit(text, (420,10))
    
    pg.display.flip()
    clock.tick(60)

pg.quit()
