import random
from abc import abstractmethod, ABC

class Walker:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = canvas.width / 2
        self.y = canvas.height / 2
        self.walk_strategy = None

    def center(self):
        self.x = self.canvas.width / 2
        self.y = self.canvas.height / 2

    def walk(self):
        self.walk_strategy.walk() 

    def set_strategy(self, walk_strategy):
        self.walk_strategy = walk_strategy

    def draw(self):
        context = self.canvas.context
        style = self.canvas.style
        context.circle((self.x, self.y),
                       1,
                       fill=style["fg"],
                       width=style["stroke_width"])


class Walk_Strategy(ABC):
    @abstractmethod
    def walk():
        pass

class Random_Walk(Walk_Strategy):
    def __init__(self, walker):
        self.walker = walker
        self.stride_length = None

    def walk(self):
        assert(self.stride_length != None)

        choice = random.randint(0, 3)

        match choice:
            case 0:
                print("left")
                self.walker.x += self.stride_length
            case 1:
                print("right")
                self.walker.x -= self.stride_length
            case 2:
                print("up")
                self.walker.y += self.stride_length
            case 3:
                print("down")
                self.walker.y -= self.stride_length

    def set_stride(self, stride_length):
        self.stride_length = stride_length

class Weighted_Walk(Walk_Strategy):
    def __init__(self, walker):
        self.walker = walker
        self.weights = None

    def walk(self):
        assert(self.weights != None)

        choice = random.random()

        if choice < self.weights[0]:
            print("up")
            self.walker.y -= 1
        elif choice < sum(self.weights[0:2]):
            print("right")
            self.walker.x += 1
        elif choice < sum(self.weights[0:3]):
            print("down")
            self.walker.y += 1
        else:
            print("left")
            self.walker.x -= 1

    # order of weights starts with up and goes
    # clockwise (up, left, down, right)
    def set_weights(self, weights):
        assert(sum(weights) == 1)
        assert(len(weights) == 4)

        self.weights = weights