import random

class Walker:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = canvas.width / 2
        self.y = canvas.height / 2

    def center(self):
        self.x = self.canvas.width / 2
        self.y = self.canvas.height / 2

    def walk(self, walk_method):
        walk_method()

    def random_walk(self):
        choice = random.randint(0, 3)

        match choice:
            case 0:
                print("left")
                self.x -= 1
            case 1:
                print("right")
                self.x += 1
            case 2:
                print("up")
                self.y -= 1
            case 3:
                print("down")
                self.y += 1

    def down_right_walk(self):
        choice = random.randint(0, 7)

        match choice:
            case 0:
                print("left")
                self.x -= 1
            case 1:
                print("up")
                self.y -= 1
            case choice if choice in range(2, 5):
                print("right")
                self.x += 1
            case choice if choice in range(5, 8):
                print("down")
                self.y += 1

    def draw(self):
        context = self.canvas.context
        style = self.canvas.style
        context.circle((self.x, self.y),
                       1,
                       fill=style["fg"],
                       width=style["stroke_width"])