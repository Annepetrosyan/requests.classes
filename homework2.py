a=5
b=6
c=7
#the average value of a, b, c
print(int(int(a+b+c)/3))
#a^c + b^c (2^4 in python is 2**4)
num_1=a**c
num_2=b**c
print(num_1+num_2)
#(a + b)^c
print(int(a+b)**c)
#abc + a*b*c   (for our case: 567 + 5*6*7)
print(int(str(a)+str(b)+str(c))+int(a*b*c))


