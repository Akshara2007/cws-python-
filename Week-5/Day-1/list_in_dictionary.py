a={"Sagar":[64,25,70,89,60],
   "Akshara":[86,76,86,90,70],
   "sanjay":[67,89,95,60,24]}

#print(a["Akshara"][3])
#print(a["sanjay"][4])

#print(sum(a["Sagar"]))

#print student name along with their total marks
#Sagar has scored 333 marks

max_marks=0
for k,v in a.items():
#   print(f"{k} has scored {sum(v)}")

     for m in v:
        if m > max_marks: 
            max_marks=m
print(max_marks)            
          
