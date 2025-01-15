class Bounds:
    def __init__(self, top, left, bottom, right):
        self.left= left 
        self.top= top 
        self.right = right 
        self.bottom = bottom
        self.width = self.right - self.left
        self.height = self.bottom- self.top
        self.center_x = self.width / 2 + self.left
        self.center_y = self.height / 2 + self.top
        self.center = (self.center_x, self.center_y)
        self.min_dimension = min(self.width, self.height)
        self.top_left = (self.left, self.top)
        self.bottom_left = (self.left, self.bottom)
        self.top_right= (self.right, self.top)
        self.bottom_right= (self.right, self.bottom)
        self.full_bounds = [self.top_left, self.bottom_right]
        if self.top > self.bottom:
            raise Exception("Top edge of boundary cannot be below bottom edge.")
        if self.left > self.right:
            raise Exception("Left edge of boundary cannot be to the right of the right edge.")
        
    def in_bounds_x(self, x_value):
        in_left_bound = x_value > self.left
        in_right_bound = x_value < self.right
        return in_left_bound and in_right_bound

    def in_bounds_y(self, y_value):
        in_top_bound = y_value > self.top
        in_bottom_bound = y_value < self.bottom
        return in_top_bound and in_bottom_bound
    
    def in_bounds(self, point):
        in_bounds_x = self.in_bounds_x(point[0])
        in_bounds_y = self.in_bounds_y(point[1])

        return in_bounds_x and in_bounds_y