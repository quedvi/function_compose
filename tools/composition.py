class Composition:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __call__(self, value):
        return self.right(self.left(value))

    def __mul__(self, other):
        return Composition(self, other)
