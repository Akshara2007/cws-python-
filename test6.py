a = input("Enter a string: ")
odd_chars = []

for i in a:
    if a.count(i) % 2 != 0 and i not in odd_chars:
        odd_chars.append(i)

print("Characters with odd count:", odd_chars)
