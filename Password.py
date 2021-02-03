####
##                      Password is good or not
#############################################################################
# Function that takes in a password 'pw' as a string
# and returns True if it 
# (i) has length at least 8, 
# (ii) has at least one upper case letter and one lowercase letter and 
# (iii) contains at least one digit.
def is_good(pw):
    has_eight = len(pw) >= 8
    has_upper, has_lower , has_num = False, False , False
    for ch in pw:
        has_upper = has_upper or ch.isupper()
        has_lower = has_lower or ch.islower()
        has_num = has_num or ch.isdigit()
    return has_eight and has_upper and has_lower and has_num

if is_good("sdgkdgkd98"):
    print("is a good password")
else:
    print("is a bad password")