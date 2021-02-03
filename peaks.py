#
# list of elements in the numeric list numlist which exceed all previous 
# elements.
#

# # number of elemetns as input 
# n = int(input("Enter number of integers: "))
# # creating an empty list 
# lst = []
# # iterating till the range 
# if n > 0:
#     for i in range(n):
#         next_int = int(input("Enter next integer : "))
#         lst = lst + [ next_int ] # Append next int to end


# Function returns the list of elements from the numeric list 
# 'numlist' which exceed all previous elements.
def peaks(numlist):
    peak_lst = [numlist[0]] if len(numlist) > 0  else []
    for i in range(len(numlist)):
        if numlist[i] > max(peak_lst):
            peak_lst = peak_lst + [numlist[i]]

    return peak_lst

lst = []
#numeric list which exceed all previous elements.
ele_list = peaks(lst)
print("List of elements in the numeric list", lst ,\
     "which exceed all previous elements is:",  ele_list )

   