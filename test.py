#!/usr/bin/env python

# [load modules here]
import pygame

# [resource handling functions here]

class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

def main():
    # [initiate game environment here]
    pygame.init()
    display = pygame.display.set_mode((400, 300))
    pygame.display.update()
    # [create new object as instance of ball class]
    ball = Ball((1,1))

    while 1:
        # [check for user input]

        # [call ball's update function]
        ball.update()

if __name__ == "__main__": main()
