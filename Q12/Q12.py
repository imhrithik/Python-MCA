class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14159 * (self.radius ** 2)
    
    def get_perimeter(self):
        return 2 * 3.14159 * self.radius

c = Circle(5)
print("Area of the circle is :", c.get_area())
print("Perimeter of the circle is :", c.get_perimeter())