# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.


percent = float(input("Enter a percentage : "))

if percent >= 90:
    grade = "A+"
elif percent >= 80:
    grade = "A"
elif percent >= 70:
    grade = "B"
elif percent >= 60:
    grade = "C"
elif percent >= 50:
    grade = "D"
elif percent >= 40:
    grade = "E"
else:
    grade = "Fail"

print(f"The result is {percent}% and your grade is {grade}")