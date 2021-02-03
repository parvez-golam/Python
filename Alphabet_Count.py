#####################################################
#                Alphabet count
####################################################
text = \
"""
The quick brown fox jumped over the lazy dog, so he did .
"""


count = 0
for c in text :
    if c. isalpha ():
        count = count + 1
    
print("Letter count is ", count)