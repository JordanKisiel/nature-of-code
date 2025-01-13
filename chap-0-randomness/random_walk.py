import random
import math
import numpy as np
from abc import abstractmethod, ABC

class Walker:
    def __init__(self, canvas, size):
        self.canvas = canvas
        self.size = size
        self.x = canvas.width / 2
        self.y = canvas.height / 2
        self.stride = 0
        self.walk_strategy = None

    def center(self):
        self.x = self.canvas.width / 2
        self.y = self.canvas.height / 2

    def set_stride(self, stride):
        self.stride = stride

    def walk(self):
        self.walk_strategy.walk() 

    def set_strategy(self, walk_strategy):
        self.walk_strategy = walk_strategy

    def draw(self):
        context = self.canvas.context
        style = self.canvas.style
        context.circle((self.x, self.y),
                       self.size,
                       fill=style["fg"],
                       width=style["stroke_width"])


class Walk_Strategy(ABC):
    @abstractmethod
    def walk():
        pass

class Random_Walk(Walk_Strategy):
    def __init__(self, walker):
        self.walker = walker

    def walk(self):
        choice = random.randint(0, 3)

        match choice:
            case 0:
                print("left")
                self.walker.x += self.walker.stride
            case 1:
                print("right")
                self.walker.x -= self.walker.stride
            case 2:
                print("up")
                self.walker.y += self.walker.stride
            case 3:
                print("down")
                self.walker.y -= self.walker.stride


class Weighted_Walk(Walk_Strategy):
    def __init__(self, walker):
        self.walker = walker
        self.weights = None

    def walk(self):
        assert(self.weights != None)

        choice = random.random()

        if choice < self.weights[0]:
            print("up")
            self.walker.y -= self.walker.stride 
        elif choice < sum(self.weights[0:2]):
            print("right")
            self.walker.x += self.walker.stride
        elif choice < sum(self.weights[0:3]):
            print("down")
            self.walker.y += self.walker.stride
        else:
            print("left")
            self.walker.x -= self.walker.stride

    # order of weights starts with up and goes
    # clockwise (up, left, down, right)
    def set_weights(self, weights):
        assert(len(weights) == 4)

        self.weights = weights

class Guassian_Walk(Walk_Strategy):
    def __init__(self, walker):
        self.walker = walker
        self.rng = np.random.default_rng()
        self.directions = [-1, 0, 1]

    def walk(self):
        guass_step = math.floor((self.rng.standard_normal() * 
                                 self.walker.stride) + 1)

        x_step = random.randint(0, 2) 
        y_step = random.randint(0, 2) 
        
        self.walker.set_stride(guass_step)

        self.walker.x += self.walker.stride * self.directions[x_step]
        self.walker.y += self.walker.stride * self.directions[y_step]

class Qualifying_Walk(Walk_Strategy):
    def __init__(self, walker):
        self.walker = walker
        self.directions = [-1, 0, 1]

    def walk(self):
        x_step = math.floor(self.walker.stride * self._accept_reject())
        y_step = math.floor(self.walker.stride * self._accept_reject())
        x_dir = random.randint(0, 2)
        y_dir = random.randint(0, 2)

        self.walker.x += self.directions[x_dir] * x_step
        self.walker.y += self.directions[y_dir] * y_step
        

    def _accept_reject(self):
        while True:
            r1 = random.random()
            r2 = random.random()

            if r2 < 1 / (r1 ** 2):
                return r1
        
