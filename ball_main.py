import pygame
from vectors.ball import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BG_COLOR = (40, 40, 40)
FG_COLOR = (230, 230, 230)
INITIAL_POS = pygame.Vector2(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
INITIAL_VEL = pygame.Vector2(100, 100)
BALL_RADIUS = 20

def main():
    pygame.init() 
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball(INITIAL_POS, INITIAL_VEL, BALL_RADIUS, FG_COLOR)

    dt = 0

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BG_COLOR)

        in_left_bound = ball.position.x > 0 + BALL_RADIUS
        in_right_bound = ball.position.x < CANVAS_WIDTH - BALL_RADIUS
        in_top_bound = ball.position.y > 0 + BALL_RADIUS
        in_bottom_bound = ball.position.y < CANVAS_HEIGHT - BALL_RADIUS
        in_x_bounds = in_left_bound and in_right_bound
        in_y_bounds = in_top_bound and in_bottom_bound 

        if not in_x_bounds:
            ball.velocity.x *= -1
        if not in_y_bounds:
            ball.velocity.y *= -1

        ball.update(dt)
        ball.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()