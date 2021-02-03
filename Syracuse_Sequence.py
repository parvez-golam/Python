# #################################################
# Name : Parvez Golam
# # Syracuse Sequence for positive integer n,
# #################################################

# # user input
# input_num = int(input("Enter a number to start the sequence:"))


# # Check if non negative number
# if input_num <= 0:
#     print("Enter a positive non-zero value")
#     input_num = int(input("Enter a number to start the sequence:"))

#variables
length = 1
next_number = 1
largest_num = 1 #input_num

# Check even or odd
def is_odd(x):
    return x % 2 

# Syracuse sequence with starting point n, returns both its length and its largest element
def syracuse(n):
    global length, largest_num, next_number 
    
    if n == 1:
        # x, y = length, largest_num
        # return x, y
        length, largest_num = length, largest_num
    # Check if odd number multiply with 3 and then add 1    
    elif is_odd(n):
        next_number = n * 3 + 1
        # compare the numbers to get the larger number
        if next_number > largest_num:
            largest_num = next_number
        length = length + 1
        #recursive call
        syracuse(next_number)
    #Check even then half the number    
    else:
        next_number = n // 2
        # compare the numbers to get the larger number
        if next_number > largest_num:
            largest_num = next_number
        length = length + 1
        #recursive call
        syracuse(next_number)
    
    return length, largest_num

# length, largest_num = syracuse(input_num)
# print("Sequence length is:", length, "Largest number in the sequence is:", largest_num)
# largest_num = 250
# l, n = syracuse(250)

# print(l, n)


previous_length = 1
ln = 1
seq_num = 1
# For starting points 1 <=n <=250, the value of n whose Syracuse sequence is the longest.
for i in range( 1 , 251):
    length = 1
    previous_length = ln
    largest_num = i
    #length and its largest element
    ln, lrg_num = syracuse(i)
    max_length = previous_length
    #sequence number with largest length 
    if ln > previous_length:
        max_length = ln
        seq_num = i

print("Length of the largest sequence between 1 and 250 is:", max_length, "for Sequence number:", seq_num )