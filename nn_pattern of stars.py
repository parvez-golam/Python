##############################################
# N*N pattern of stars
##############################################

#input number
input_number = int(input("Enter a value of n:"))

if input_number < 0:
    print("Enter non negative value")
    input_number = int(input("Enter a number:"))

# #triangle
# for row in range(input_number):
#     for col in range(row+1):
#         print( "*" , end = "")
#     print()

# #matrix
# for row in range(input_number):
#     for col in range(input_number):
#         print( "*" , end = "")
#     print()

# Print triangluar pattern of character 'sym'
# of size 'n '.
def triangle (sym, n):
    for row in range(n):
        for col in range(row+1):
            print (sym, end = "")
        print ()

triangle("*", input_number)

for level in range(2, 7, 2):
    triangle (".", level )