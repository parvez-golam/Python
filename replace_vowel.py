#
# Replace Vowel
#

# any string entry
input_string = input("Type a string:")


#function to replace vowels in a string
def bleep(s):
    new_str = ""
    # Check if vowel and replace
    for i in range(len(s)):
        if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or 
           s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
            new_str = new_str + "*"
        else:
            new_str = new_str + s[i]
    
    return new_str

replace_str = bleep(input_string)
print("Replaced string for string", input_string, "is:", replace_str )


