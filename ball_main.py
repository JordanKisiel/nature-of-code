import pygame
from utils.bounds import *
from vectors.ball import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BG_COLOR = (40, 40, 40)
FG_COLOR = (230, 230, 230)
GRAVITY = 980
INITIAL_POS = pygame.Vector2(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
INITIAL_VEL = pygame.Vector2(0, 0)
INITIAL_ACCELERATION = pygame.Vector2(0, GRAVITY)
BALL_RADIUS = 20

def main():
    pygame.init() 
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball(INITIAL_POS, 
                INITIAL_VEL, 
                INITIAL_ACCELERATION, 
                BALL_RADIUS, 
                FG_COLOR)
    bounds = Bounds(BALL_RADIUS, 
                    BALL_RADIUS, 
                    CANVAS_HEIGHT - BALL_RADIUS, 
                    CANVAS_WIDTH - BALL_RADIUS)
    ball.set_bounds(bounds)

    dt = 0

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BG_COLOR)

        ball.update(dt)
        ball.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()