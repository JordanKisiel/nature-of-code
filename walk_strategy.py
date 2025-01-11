from abc import abstractmethod, ABC
import random

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
                self.x += 1
            case 1:
                print("right")
                self.x -= 1
            case 2:
                print("up")
                self.y += 1
            case 3:
                print("down")
                self.y -= 1