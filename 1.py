#write python code to test whether given number is divisible by 2 or 3 or 5.

num=int(input("enetr the number:"))
if num%2==0 and num%3==0 and num%5==0:
    print("number is dividible by 2,3&5")
elif num%2==0 and num%3==0:
    print("number is divisible by 2&3")
elif num%2==0 and num%5==0:
    print("number is divisible by 2&5")
elif num%3==0 and num%5==0:
    print("number is divisible by 3&5")
elif num%2==0:
    print("number is divisible by 2")
elif num%3==0:
    print("number is divisible by 3")
elif num%5==0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 2,3&5")
    
