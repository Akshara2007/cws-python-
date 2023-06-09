"""
Put 5 subject name and marks in a dictionary.
Print the total of all marks divisible by 2.
"""
a={"physics":78,"computer": 68,"chemistry":50,"history":88,"Maths":70}
total=0

for v in a.values():
    if v % 2 == 0:
        total = total + v

print(total)
