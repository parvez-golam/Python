#
# UpDown
#

# # number of elemetns as input 
# n = int(input("Enter number of integers:"))
# creating an empty list 
# lst = []
# # iterating till the range 
# if n > 0:
#     for i in range(n):
#         next_int = int(input("Enter next integer : "))
#         lst = lst + [ next_int ] # Append next int to end


# Function to check if list 's' consists of an increasing segment
# followed by a decreasing segment
def updown(s):
    n = len(s)
    # base case
    if (n==1) or (n==0) :
        return True
    else :
        # if first sub-list is strictly increasing
        if (s[0] < s[1] ) :
            i = 1
            #check for increasing condition
            while(i<n and s[i-1] < s[i]):
                i = i + 1
            #check for decreasing condition
            while( i + 1 < n and s[i] > s[i+1]):
                i = i + 1

            if (i>= n -1):
                return True
            else:
                return False

        #if first sub-list is stritctly decreasing
        elif (s[0]> s[1]):
            i = 1
            #check for decreasing condition
            while ( i<n and s[i-1]> s[i]):
                i = i + 1
            #check for decreasing condition
            while (i + 1 < n and s[i] < s[i + 1]): 
                i  = i + 1

            if (i>= n -1):
                return True
            else:
                return False

        else:    #s[0] == s[1]
            for i in range(2,n):
                if (s[i-1] <= s[i]):
                    return False
            return True


lst = []
#Function call to check if 'lst'
#consists of an increasing segment followed by a decreasing segment.
is_updown = updown(lst)
print(lst, \
    "consists of an increasing segment followed by a decreasing segment:",\
         is_updown)

