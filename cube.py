# 
# perfect cube
# 

# integer input
input_int  = int(input("Enter a number:"))


# Function that takes integer 'n' and returns True 
# if it is a perfect cube False otherwise
def is_cube(n):
    l_cube = 0

    for i in range(n+1):
        # find cube of each number
        l_cube = i * i * i

        # check if cube equal to the argument integer
        if l_cube == n :
            return True
        else:
            return False


#Function call to check entered number is a perfect cube or not
cube = is_cube(input_int)
print("Integer", input_int, "is a perfect cube:", cube)