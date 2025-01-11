from PIL import Image, ImageDraw

class Canvas:
    def __init__(self,
                 width,
                 height,
                 style={
                    "bg": (40, 40, 40),
                    "fg": (230, 230, 230),
                    "stroke_width": 2,
                 }):
        self.width = width
        self.height = height
        self.style = style
        self.out = Image.new("RGB", 
                             (self.width, self.height),
                             self.style["bg"])
        self.context = ImageDraw.Draw(self.out)

    def write(self, file_name):
        self.out.save(f"./images/{file_name}.png")
