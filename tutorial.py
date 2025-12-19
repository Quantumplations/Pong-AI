import pygame
from pong import Game

class PongGame:
    def __init__(self, win, width, height):
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paaddle
        self.right_paddle = self.game.right_paddle
        self.ball =  self.game.ball

width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)
    if keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)

    game.loop()
    game.draw()
    pygame.display.update()

pygame.quit()