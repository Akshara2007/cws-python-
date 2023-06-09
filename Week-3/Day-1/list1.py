"""
List in python
a=[43]
"""
a=[43,67,11,"Akshara"]
print(a)
print(type(a))
for i in range (0,len(a),1):
    if a[i] % 2 ==0:
        total=total+a[i]

print(f"Total is{total}")
