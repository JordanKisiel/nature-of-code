import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, 
                 position, 
                 velocity, 
                 radius, 
                 color):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           self.position,
                           self.radius,
                           2)
        
    def update(self, dt):
        self.position += self.velocity * dt