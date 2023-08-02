"""
Write a function which returns addition of two values

Addition,check
"""
def addition(n1 ,n2):
    return n1+n2

def check(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
x =addition(55,55)
print(x) 
check(x)