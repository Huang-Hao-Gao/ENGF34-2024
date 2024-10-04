#greatest common demoninator function
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


#odd or even function
def oddeven():
    try:
        print("Please enter an integer: ", end="")
        n = int(input())
    except ValueError:
        print("Please enter a valid integer.")
        oddeven()
    else:
        if n % 2 == 0:
            print(n, " is even.")
        else:
            print(n, "is odd.")
        
#oddeven()


#fizzbuzz function

def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz", end=" ")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        elif x % 5 == 0:    
            print("Buzz", end=" ")
        else: print(x, end=" ")

fizzbuzz()