##----------------------------------------------------
# Fibonnacci  Series
##----------------------------------------------------

def fibonnacci(n, pos):
    fib_list = []
    for i in range(n):
        if (i == 0) or (i == 1) :
            fib_list.append(i) 
        else:
            fib_list.append(fib_list[i-2] + fib_list[i-1]) 
            
    print("First %d Fibonnacci numbers:" %n, fib_list)
    print("%dth number in Fibonnacci series is:" %pos, fib_list[pos-1])

# driver program     
position = int(input("Enter a number between 1 and 40:"))   
fibonnacci(40, position)
