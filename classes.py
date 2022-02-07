##Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
# class Circle:
    
    # def __init__(self, radius):
        # self.radius = radius
        
    # def get_perimeter(self):
        # return self.radius * 2 *3.14
        
    # def get_area(self):
        # return 3.14 * self.radius ** 2
        
# c1 = Circle(5)
# print(c1.get_perimeter())
# print(c1.get_area())


# # Create class Human which will be INITIALIZED with following attributes:
# # Name, surname, age, height, weight, 
# # And will have these methods
# # A method which will tel in which year the person will be 100 years old
# # A method which will tell the optimal weight
# # A method to present


class Human:

    def __init__(self, name, surname, age, height, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        
    def get_100(self):
        a = 100 - self.age + 2022
        return a
        
    def get_optimal_weight(self):
        optimal_weight =  45.5 + (0.91 * (self.height - 152.4))
        man_weight =  50 + (0.91 * (self.height - 152.4)) 
        return optimal_weight and man_weight
    
    def presentation(self):
        print(f"{self.get_100} is your")
        
h1 = ("Anna", "Petrosyan", 23, 1.70, 43)
print(h1.presentation())
        
    
















