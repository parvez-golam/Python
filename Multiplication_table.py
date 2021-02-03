#####################################
# Multiplication table r*c
#####################################

limit = int(input("Enter the limit of Multiplication table:"))

for row in range(1, limit + 1):
    for col in range(1, limit + 1):
        product = row * col
        if product < 10:
            print (" ", end = "")
        print(product, " ", end = "")
    print()