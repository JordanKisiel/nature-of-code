import random
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
        assert(stride >= 0)
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