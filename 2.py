 #1-in
# symbols = ["*", "**", "***", "****", "*****"]
# for i in symbols:
    # print(i)
    
    
#2-rd arajadranq   
# previous_num = 1
# for i in range(2,11):
    # sum = previous_num + i
    # print(i, "+", previous_num, "=", sum)
    # previous_num = i


#3-rd    
# a = "AnnaPetrosyan"
# for index in range(len(a)):
    # if index % 2 == 0:
        # print(a[index], end=" ")
 
#4-rd 
n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n % i == 0):
        print(i)