from canvas import Canvas
from random_walk import *


def main():
   canvas = Canvas(800, 600) 
   walker = Walker(canvas, 1)
   walker.set_stride(2)
   walk = Weighted_Walk(walker)
   walk.set_weights([0.25, 0.25, 0.25, 0.25])
   walker.set_strategy(walk)
   weights_lst = [
      [0.75, 0.15, 0.09, 0.01],
      [0.01, 0.75, 0.15, 0.09],
      [0.09, 0.01, 0.75, 0.15],
      [0.15, 0.09, 0.01, 0.75],
   ]

   iterations = 0
   while is_in_bounds(walker) and iterations < 100000:
      divisor = iterations % 4
      weights = [divisor / 4, divisor / 4, divisor / 4, divisor / 4] 
      stride = iterations % 8
      walk.set_weights(weights)
      # walker.set_stride(stride)
      walker.walk()
      walker.draw()
      iterations += 1
   
   canvas.write("test")

def is_in_bounds(walker):
   in_bounds_x = walker.x > 0 and walker.x < walker.canvas.width
   in_bounds_y = walker.y > 0 and walker.y < walker.canvas.height

   return in_bounds_x and in_bounds_y

if __name__ == "__main__":
    main()