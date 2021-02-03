###
## A string is palindrome
#

# Returns filltered version of 'text' with all punctuation
# marks removed.
def depunctuated(text):
    MARKS = '''!()-[]{};:'\", <>./?@#$%^&*_~'''
    dep = ""
    for c in text :
        if c not in MARKS:
            dep = dep + c
    return dep

# Returns mirror image of 's'
def reverse(s):
    return s[::-1]


# Returns 'Ture' if 's' is palindrome 'False' otherwise.
def is_palindrome(s):
    return depunctuated(s).lower() == reverse(depunctuated(s).lower())

str_value = "August"
#check entered string is palindrome
palindrome = is_palindrome(str_value)
if palindrome == True:
    print("'",str_value,"'", "is palindrome.")
else:
    print("'",str_value,"'", "is not palindrome")