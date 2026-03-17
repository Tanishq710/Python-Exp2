marks=int(input("Enter Percentage of Student: "))
if marks>60 and marks<=100:
    print("Student Gets First Division")
elif marks>50 and marks<=59:
    print("Student gets second Division")
elif marks>40 and marks<+49:
    print("Student gets Thrid Division")
else:
    print("Student is Failed")