# #################################################
# Name : Parvez Golam
# # First hundred terms of infinite Sum (real number)
# #################################################

# user input
input_num = float(input("Enter a number:"))

# Finding the sum of first hundred terms
total_sum = 0
for i in range(0, 100):
    # factorial of the each number in range 
    factorial = 1
    for x in range( 1, i + 1):
        factorial = factorial * x
    # Total Sum    
    total_sum = total_sum + ( input_num**i / factorial ) 

print ("e^x based on the first hundred terms of the infinite sum is", total_sum )
# import math
# x = 2.5
# e=0
# pres=0.0001
# s=1
# i=1
# while s>pres:
#     e=e+s
#     s=(x**i)/math.factorial(i)
#     i=i+1
# print(e)