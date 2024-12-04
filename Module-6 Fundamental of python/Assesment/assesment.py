marks = []

def take_numbers():
    for i in range(5):
        mark = int(input("Enter number: "))
        marks.append(mark)
    return marks

def calculate_sum(marks):
    return sum(marks)

def find_avg():
    average = total_sum / len(marks)
    return average

def find_grades():
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "Fail"

while True:
    name = input("Enter a student name: ")
    
    take_numbers()
    total_sum = calculate_sum(marks)
    
    average = find_avg()
    print(f"Average: {average}")
    
    grades = find_grades()
    print(f"Grade: {grades}")
    
    continue_input = input("Do you want to enter another student? yes/no : ")
    if continue_input != 'yes':
        break

print("Programm end")
    