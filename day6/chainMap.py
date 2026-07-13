from collections import ChainMap

student={
    "Name":"John",
    "Age":20,
}

course={
    "Course":"Python", 
    "Duration":"3 months",
}

combined=ChainMap(student,course)
print(combined)
print(combined["Name"])  
print(combined["Course"])  
