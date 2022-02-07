# class Triangle:
    # _counter = 0

    # def __init__(self,a,b,c):
        # self.a = int(a)
        # self.b = int(b)
        # self.c = int(c)
        # self._perimeter = self.a + self.b + self.c
        # self.s = self._perimeter / 2
        # self._area = ((self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5
        
        
    # def area(self):
        # return f"The area of given triangle is equal to {self._area}"
        
    # def perimeter(self):
        # return f"The perimeter of given triangle is equal to {self._perimeter}"
    
    
    # def __eq__(self, other):
        
        # return self._area == other._area
        
    # def counter(self):
        # Triangle._counter += 1
        # self.id = Triangle._counter
        # return self.id
        
            
            
# t1 = Triangle(1, 2, 2)
# t2 = Triangle(2, 1, 2)
# print(t2.area())
# print(t1 == t2)
# print(t1.perimeter())



class Rectangular:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.s = 2 * (self.a * self.b + self.a * self.c + self.b * self.c)
        self.v = self.a * self.b * self.c
        
    def count_v(self):
        
        return f"The volume of given rectangular is equal to {self.v}: "
        
    def count_s(self):
        
        return f"The surface area of given rectangular is equal to {self.s}:"
        
        
    def __eq__(self, other):
        return self.s == other.s
    
    def __gt__(self, other):
        if self.v > other.v is True:
            return "the first rectangular can contain the second one"
        
            
        
    def __lt__(self, other):
        if self.v < other.v is True:
            return "the second rectangular can contain the first one"
           
            
           
           
r1 = Rectangular(1, 3, 4)
r2 = Rectangular(3, 2, 4)
print(r1.count_v())
print(r1.count_s())
print(r1 == r2)
print(r1 < r2)
print(r1 > r2)

     
    































