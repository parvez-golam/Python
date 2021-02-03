##Analyze a body of English-language text and print the
##percentage of letters that are As, Bs and so on.

def analyze( text ):
    letter_count = 0
    freq = {}
    for c in text :
        # process a character updating freq and letter count
        # (ignore non letters and case diferences )
        # Run through contents of freq to print percentages
        if c.isalpha():
            letter_count += 1
            c_upper = c.upper()
            if c_upper in freq :
                freq [c_upper] += 1
            else:
                freq [c_upper] = 1

    for c in sorted(freq.keys()):
        percent = freq[c] * 100 / letter_count
        print("'%s': %4.2f%%" % (c, percent))


text_value = \
"""
this is a test
of letter frequency
"""
analyze( text_value )