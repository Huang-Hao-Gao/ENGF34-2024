def gcd(a, b):
    while not a==b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a

ax = 42
bx = 30
#print("Greatest Common Demoninator of", ax, "and", bx, "is", gcd(ax, bx))


def oddeven():
    print("Please enter an integer: ")
    n = int(input())
    if n % 2 == 0:
        print(n, " is even.")
    else:
        print(n, " is odd.")
        
oddeven()
