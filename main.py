from canvas import Canvas
from random_walk import *


def main():
   canvas = Canvas(800, 600) 
   walker = Walker(canvas)
   random_walk = Random_Walk(walker)
   random_walk.set_stride(1)
   down_right_walk = Weighted_Walk(walker)
   down_right_walk.set_weights([0.1, 0.4, 0.4, 0.1])
   walker.set_strategy(random_walk)

   while is_in_bounds(walker):
      walker.walk()
      walker.draw()
   
   canvas.write("test")

def is_in_bounds(walker):
   in_bounds_x = walker.x > 0 and walker.x < walker.canvas.width
   in_bounds_y = walker.y > 0 and walker.y < walker.canvas.height

   return in_bounds_x and in_bounds_y

if __name__ == "__main__":
    main()