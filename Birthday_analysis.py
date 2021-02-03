##Analyze date of birth data for group of individuals and
##identify clusters (of two or more) who share the same birthday

def day_of_year(date ):
    # Return the day-month prefix of parameter 'date'
    return date [: date.rfind("/")]


def common_birthdays(persons):
    # Analyze list 'persons' and output the names of all clusters
    # of individuals that share a common birthday. Assume each
    # element of 'persons' is a name & date-of-birth pair.
    days = {}
    flag = False
    for p in persons:
        name = p[0]
        dob = p[1]
        birthday = day_of_year(dob)

        if birthday not in days:
            days[ birthday ] = [name]
        else :
            days[ birthday ].append(name)

    for d in days:
        names = days[d]
        if len(names) > 1:
            flag = True
            print("%s: " % d, end = "")
            for n in names:
                print("%s " % n, end = "")
            print ()

    if not flag:
        print("No common birthdays")


classlist = [
["Aoife", "1/1/1990"],
["Barra", "2/2/1990"],
["Turlough", "3/6/1991"],
["Johny", "3/6/1992"]
]
common_birthdays(classlist)