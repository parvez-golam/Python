# ##########################################
# # 1:Factorial
# ##########################################
# user input
input_num = int(input("Enter a number:"))

# Check if non negative number
if input_num < 0:
    print("Enter a positive value")
    input_num = int(input("Enter a number:"))

factorial = 1

# #For loop for finding a factorial
for i in range( 1, input_num + 1 ):
    factorial = factorial * i

print("Factorial of", input_num, "is", factorial )

    


