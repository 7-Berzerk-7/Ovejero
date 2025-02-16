import pygame


class pastor():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20

    def draw(self, interfaz):
        pygame.draw.rect(interfaz, color=(255, 255, 0), rect=(self.x,self.y,self.size,self.size) )
