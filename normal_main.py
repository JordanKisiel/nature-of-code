import numpy as np
import math
from randomness.canvas import *

def main():
    canvas = Canvas(800, 600)
    center = (canvas.width / 2, canvas.height/ 2)
    color = (175, 175, 175)
    generate_splatter(canvas, center, 80000, color)
    canvas.write("test")

def generate_splatter(canvas, position, num_dots, base_color):
    context = canvas.context
    style = canvas.style
    spread = 60
    color_jitter = 30
    base_size = 8

    for n in range(num_dots):
        rng = np.random.default_rng()
        x = rng.standard_normal() * spread
        y = rng.standard_normal() * spread
        r = rng.standard_normal() * color_jitter 
        g = rng.standard_normal() * color_jitter
        b = rng.standard_normal() * color_jitter
        point_x = (position[0] + x)
        point_y = (position[1] + y)
        color_r = math.floor(base_color[0] + r)
        color_g = math.floor(base_color[1] + g)
        color_b = math.floor(base_color[2] + b)
        dist = ((position[0] - point_x) ** 2 + 
                (position[1] - point_y) ** 2) ** (0.5) + 1

        color = (color_r, color_g, color_b)
        size = base_size / dist

        context.circle((point_x, point_y), size, fill=color)

if __name__ == "__main__":
    main()