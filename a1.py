#generate all the prime numbers between 1 to 100 using python code.
import math
def f(x):
    for i in range(1,100):
        if math.gcd(100,i)==1:
            print(i)

f(100)            
