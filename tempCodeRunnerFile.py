a = input("Enter a string: ")

vowels = ['a', 'e', 'i', 'o', 'u']
result = []
words = ""

for i in a:
    if i.lower() in vowels:
        if words:
            result.append(words)
            words = ""
    else:
        words = words + i

if words:
    result.append(words)

print("Split string on vowels:", result)
