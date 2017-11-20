#M6LAB
#11/1
#CTI 110
#Gardnerm

def main():
    while 1 == 1:
        name=input("What is your name? ")
        greet(name)
        age=int(input('what is your age? '))
        print(" you are a: ", ageCategory(age))
   
def greet(name):
    """greet user by name"""
    print("Hello,", name)
    
def ageCategory(age):
    answer = "Uknown"
    if age <= 2:
        answer = "infant"
    elif age > 2 and age < 13:
        answer = "child"
    elif age >= 13 and age < 20:
        answer = "teenager"
    elif age >= 20:
        answer = "adult"
    return answer

    
































main()
