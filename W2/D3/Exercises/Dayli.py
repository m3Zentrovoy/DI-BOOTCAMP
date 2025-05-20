class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("must be radius or diametr")
        

    def area(self):
        return  f'{(3.14 * self.radius) **2} cm²'
        
    def __str__(self):
        return (f'{self.radius} cm - attributes of the circle')
        
 
    def __add__(self, other):
                 return Circle(self.radius + other.radius)

        
    def __gt__(self, other):
        if not isinstance(other, Circle):
             raise TypeError(f"You can't compare Circle to {type(other)}")
        return self.radius > other.radius
             
          
    def __lt__(self, other):
        if not isinstance(other, Circle):
             raise TypeError(f"You can't compare Circle to {type(other)}")
        return self.radius < other.radius
           
        
    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"You can't compare Circle to {type(other)}")
        return self.radius == other.radius
            
        
circles = [Circle(5), Circle(3)]
sorted_circles = sorted(circles)
for circle in sorted_circles:
    print(circle)


c1 = Circle(8)
c2 = Circle(12)

print(c1.area())
print(str(c1))
print(c1 + c2) 
print(c1 == c2)
print(c1 > c2)
print(c1 < c2)