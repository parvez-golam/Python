##########################################
###########    Ten Green bottles         ############
##########################################

def sing_verse (n):
    # Print the 'n'th verse of the song.
    print (n, "Green Bottles hanging on the wall,")
    print (n, "Green Bottles hanging on the wall,")
    print ("And if one Green Bottle should accidentally fall ,")
    print ( "There' ll be", n - 1, "Green Bottles hanging on the wall.")

def pause_for_breath ():
    # Print a small bit of silence .
    print ()

for verse in range(100, 0, -1):
    sing_verse ( verse )
    pause_for_breath ()