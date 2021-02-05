##----------------------------------------------------------------------------
# Most popular word froma file
##----------------------------------------------------------------------------

def most_popular(fname):
    # Function that takes text file in 'fname' and prints
    # (i)the most popular word
    # (ii) all words with more than 150 occurrences
    # (iii) all words with a frequency-based probability greater than 0.01 in
    #      the file.

    # Open and read file
    textfile = open(fname, "r",  encoding ="ISO-8859-1")
    file_content = textfile.read()
    file_content = file_content.replace("\n", " ")

    word_list = file_content.split() 
    word_count = len(word_list)
    
    # words and their frequencies
    d1 = {}
    for word in word_list:
        d1[word] = (d1[word] + 1) if word in d1 else 1
    
    multiplicities = [ word_list.count(ele) for ele in word_list ]
    print("Most popular word/words is/are:" )
    for (k,v) in d1.items():
        # most popular word
        if v == max(multiplicities):
            print("'%s' : %d" %(k, v))

    print("All words with more than 150 occurrences are:" )
    for (k,v) in d1.items():
        # words with more than 150 occurrences
        if v >= 150:
            print("'%s' : %d" %(k, v))

    # words with a frequency-based probability greater than 0.01
    print("All words with a frequency-based probability greater than" \
        " 0.01 are:")
    for k in d1.keys():
        freq = d1[k] / word_count 
        if freq >= 0.01 :
            print("'%s' : %f " %(k, freq))

    textfile.close ()


# Driver program
file_name = "testPos.txt"
most_popular(file_name)

