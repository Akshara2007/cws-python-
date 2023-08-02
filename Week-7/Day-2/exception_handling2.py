

try:
    a=[53,43,23,32,35,0]
    print(a[9])
    print(a[0]/a[-1])
except ZeroDivisionError:
    print("Cannot divible by zero")
except IndexError:
    ("Wrong index given")
except:
    print("Some error occurenced")