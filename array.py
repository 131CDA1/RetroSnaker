class Array:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
    def __repr__(self):
        return (self.x, self.y)

a = Array(1,2)
print(a)