grades=["A+", "A", "A-", "B", "C", "D", "F"]
points=[4.0, 3.75, 3.50, 3.0, 2.0, 1.0, 0.0]
ranges =[100, 80, 70, 60, 50, 40, 33, 0]
marks = float(input("Enter Your Marks: "))

for i, values in enumerate(ranges):
    if marks <= ranges[i] and marks >= ranges[i+1]:
        print("Grade: ",grades[i])
        print("Points: ",points[i])
        break

