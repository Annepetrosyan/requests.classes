##2

# a = (1, 2, 3, 4, 4, 3, 5, 5,  6, 7)
# def crn(a: tuple) -> tuple:
    # for item in a:
        # if a.count(item) > 1:
        
            # return item
    
# print(crn(a))

##3  Write a Python function to reverse a tuple

# def rev(tuple_: tuple) -> tuple:
    # new_tup = tuple_[::-1]
    # return new_tup
    
# a = ( 'A', 'n', 'n', 'a', 'P', 'e', 't', 'r', 'o', 's', 'y', 'a', 'n')
# print(rev(a))

#Write a Python function to calculate and print the average value of the numbers in a given tuple of tuples

def average_(b: tuple) -> int:
    for t in a:
        for k in t:
            sum = 0
            average = (sum + int(k))/ len(t)
        
            return average
        
a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(average_(a))
            
