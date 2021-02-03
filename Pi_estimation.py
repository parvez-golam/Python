#########################################
# PI estimation
########################################
#value of Pi
def estimate_pi(n):
    pi = 2
    for i in range(1, n+1):
        left_num = (2 * i)/(2 * i - 1)
        right_num = (2 * i)/(2 * i + 1)
        pi = pi * left_num * right_num
    return pi

#Pi where n is 100
print( "Estimztion of Pi is", estimate_pi(100)) 

def estimate_pi_2 (n):
    total = 3
    for k in range(1, n+1):
        kth_term = (-1)**(k+1) * (4 / (2*k * (2*k+1) * (2*k+2)))
        total = total + kth_term
    return total

print( "Estimztion of Pi is", estimate_pi_2(100)) 