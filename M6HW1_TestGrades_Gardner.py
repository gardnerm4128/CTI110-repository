#M6HW1
#11/6/17
#CTI-110
#Matthew Gardner

def main():
    while 1 == 1:
        grade1 = float(input("Enter grade: "))
        grade2 = float(input("Enter grade: "))
        grade3 = float(input("Enter grade: "))
        grade4 = float(input("Enter grade: "))
        grade5 = float(input("Enter grade: "))
        calc_average(grade1,grade2,grade3,grade4,grade5)
        average = (grade1 + grade2 + grade3 + grade4 + grade5)
        average = average / 5
        print("your grade is:", determine_grade(average))
        

def calc_average(grade1,grade2,grade3,grade4,grade5):
    """calculate grade average"""
    average = (grade1 + grade2 + grade3 + grade4 + grade5)
    average = average / 5
    print("average = ", average)

def determine_grade(average):
    if average >= 90 and average <=100:
        answer = "A"
    elif average <= 89 and average >= 80:
        answer = "B"
    elif average <= 79 and average >= 70:
        answer = "C"
    elif average <= 69 and average >= 60:
        answer = "D"
    elif average <= 59 and average >= 0:
        answer = "F"
    return answer


















main()
    
