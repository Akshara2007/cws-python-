a = input("Enter a string = ")
b = a.split('_')

pascal_case = ''.join(word.capitalize() for word in b)

print("Pascal case string:", pascal_case)
