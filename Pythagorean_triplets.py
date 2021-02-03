#################################################
# pythagorean  triples
################################################

#One way
def pythagorean_triplet(n):
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                if (c <= n) and (c*c == a*a + b*b):
                    print (a, b, c)
                    
            
pythagorean_triplet(20)


#Second way
# Generate pythagorean  triples
def pythagorean_triple(limit) : 
    c, n = 0, 2
  
    while c < limit : 
          
        # loop from 1 to n- 1 
        for i in range(1, n) : 
            #formula to find a given number is triplet or not a^2 + b^2 = C^2
            #Property taken from Pythagorian Triplet generator by Blackpenredpen(you tube)
            a = n * n - i * i 
            b = 2 * n * i 
            c = n * n + i * i  
  
            # if c is greater than limit then don't process
            if c > limit : 
                break
  
            print(a, b, c) 
  
        n = n + 1


#Pythagorean triple, where a, b, c < = 100
print("Pythagorean Triples from 1 to 100 are:")
pythagorean_triple(20) 