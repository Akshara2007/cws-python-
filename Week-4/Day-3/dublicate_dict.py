a = {"physics": 69, "chemistry": 95, "maths": 18, "english": 80, "cs": 89}
b = {}

for k, v in a.items():
    if v>33:
        b[k] = "pass"
    else:
        b[k]="fail"
print(b)