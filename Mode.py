###########################################################################
##
###########################################################################

def most_common(lst):
    # Return the most commonly occurring value in list ' lst '
    # (ties broken arbitrarily ). List must be non􀀀empty.
    multiplicities = [ lst.count(elem) for elem in lst ]
    largest = max( multiplicities )
    return lst [ multiplicities.index( largest )]

names = ["Brown", "Green", "Brown", "Gordon", "Brown", "Green", "Green", ]
print(most_common(names))