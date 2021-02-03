# #################################################
# Name : Parvez Golam
# # Prime number
# #################################################
def is_prime(n):
    # Return True if 'n' is prime
    no_divisors = n > 1
    cand = 2
    while no_divisors and cand < n:
        no_divisors = no_divisors and n % cand != 0
        cand = cand + 1
    return no_divisors


# user input
input_num = int(input("Enter a number:"))

# Check if non negative number
if input_num < 0:
    print("Enter a positive value")
    input_num = int(input("Enter a number:"))

st = "is not a prime Number"
if input_num > 2 : 
    # check for prime number
    for i in range( 2, input_num):
        if ( input_num % i == 0 ):
            st = "is not a prime number"
            break
        else:
            st = "is a prime number"
elif input_num == 2:
    st = "is a prime number"

print ( input_num, st )

if is_prime(input_num):
    print (input_num, "is a prime number")
else:
    print (input_num, "is not a prime number")



