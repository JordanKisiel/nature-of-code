import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, 
                 position, 
                 velocity,
                 acceleration, 
                 radius, 
                 color):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.color = color
        self.bounds = None

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           self.position,
                           self.radius,
                           2)
        
    def update(self, dt):
        bounce_vec = pygame.Vector2(1, 1)
        if self.bounds != None:
            bounce_vec = self._get_bounce_vec()

        self.velocity = (self.velocity.elementwise() * 
                         bounce_vec.elementwise())
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    def set_bounds(self, bounds):
        self.bounds = bounds

    def _get_bounce_vec(self):
        assert(self.bounds != None)

        x_bounce = 1
        y_bounce = 1
        if not self.bounds.in_bounds_x(self.position.x):
            x_bounce = -1
        if not self.bounds.in_bounds_y(self.position.y):
            y_bounce = -1
        return pygame.Vector2(x_bounce, y_bounce)