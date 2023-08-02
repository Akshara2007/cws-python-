"""
2
sumlist,checker

sum(a) -> return
"""
def sumlist(customlist):
    total = sum(customlist)
    return total

def checker(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

p = [20,10,35,25,45]
r = sumlist(p)
print(r)
checkerer(r)
