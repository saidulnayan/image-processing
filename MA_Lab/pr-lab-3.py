
marks = input("Input your mark: ")
marks = float(marks)
grades = "N/A"
points ={"A+":4.0,"A":3.75,"A-":3.50,"B":3.0,"C":2.0,"D":1.0,"F":0.0,"N/A":"N/A"}

if marks>= 80 and marks<= 100:
    grades = "A+"
    print("Letter grade: ",grades[0])
elif marks>= 70 and marks<= 79:
    grades = "A"
    print("Letter grade: ",grades)
elif marks>= 60 and marks<= 69:
    grades = "A-"
    print("Letter grade: ",grades)
elif marks>= 50 and marks<= 59:
    grades = "B"
    print("Letter grade: ",grades)
elif marks>= 40 and marks <= 49:
    grades = "C"
    print("Letter grade: ",grades)
elif marks>=33 and marks<=39:
    grades = "D"
    print("Letter grade: ",grades)
elif marks>=0 and marks<=32:
    grades = "F"
    print("Letter grade: ",grades)
else:
    print("Invalid marks")

print("Grade point:",points[grades])

