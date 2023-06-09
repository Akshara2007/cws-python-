"""
Find the maximum marks in a dictonary
"""
a = {"physics": 69, "chemistry": 59, "maths": 18, "english": 80, "cs": 89}
max_marks = 0
max_marks_subject_name=""

for k,v in a.items():
    if v > max_marks:
        max_marks = v
        max_marks_subject_name=k
        
print(max_marks_subject_name=k)
print(max_marks)
# marks = []

# for v in a.values():
#     marks.append(v)

# print(max(marks))
# print(max(a.values()))