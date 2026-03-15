class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

r1 = Rectangle(5, 10)
r2 = Rectangle(3, 4)

print(r1.area(), r1.perimeter())
print(r2.area(), r2.perimeter())