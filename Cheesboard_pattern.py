############################################
##   Chess board pattern
################################################

def chessboard(n):
    WHITE, BLACK = '.', '#'
    for row in range(n):
        for col in range(n):
            if (row + col) % 2 == 0:
                print(WHITE, end = "")
            else :
                print(BLACK, end = "")
        print ()

chessboard(5)

# def foo( first , second, length, sep):
#     return sep.join([first if c == 0 else second for c in range(length)])
# def bar(n):
#     ONE = "."
#     OTHER = "."
#     line1 = foo(ONE, OTHER, n, "#" )
#     print(line1)
#     line = line1.replace(ONE, "#" ).replace(OTHER,ONE).replace( "" ,OTHER)
#     print(line)
#     print(foo(line1 , line , n, ""))

# bar(6)