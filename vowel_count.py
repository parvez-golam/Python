# 
# Count vowels
# 

# "any string entry
input_string = input("Type a string:")

#function to count vowels in a string
def count_vowels(s):
    num_vowel = 0
    
    # Check if vowel and count
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            num_vowel = num_vowel + 1
    return num_vowel

# Vowel count in the entered string
vowel_count = count_vowels(input_string)
print("Number of vowels in entered string '", input_string, "' is:", vowel_count)