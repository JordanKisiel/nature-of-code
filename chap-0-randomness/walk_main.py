from canvas import Canvas
from random_walk import *


def main():
   canvas = Canvas(800, 600) 
   walker = Walker(canvas, 1)
   walk = Guassian_Walk(walker)
   walker.set_strategy(walk)
   walker.set_stride(1)

   iterations = 0
   while is_in_bounds(walker) and iterations < 100000:
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