## Python program that takes in a positive
## numbers, asks the user to enter that many integers
## and then prints the integers in reverse order.
#############################################################################

n = int(input("Enter number of integers: "))
lst = []

for i in range(n):
    next_int = int(input("Enter next integer : "))
    lst = lst + [ next_int ]

for i in range(n-1, -1, -1):
    print( lst [ i ])