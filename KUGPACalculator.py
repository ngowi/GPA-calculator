# Grade point average calculator
# Korea University grading system
# Project 2

A_PLUS = 4.5
A      = 4.0
B_PLUS = 3.5
B      = 3.0
C_PLUS = 2.5
C      = 2.0
D_PLUS = 1.5
D   = 1
F      = 0

print("GPA calculator v1.0 under GNU license\n")

grade = input("Enter grade(Press enter to quit): ")

points = 0
credit_counter  = 0 

while grade != "":
    credit = int(input("How many credits?  "))
    if grade =='A+':
        points += A_PLUS * credit
        credit_counter += credit
    elif grade =='A':
        points += A * credit
        credit_counter += credit
    elif grade =='B+':
        points += B_PLUS * credit
        credit_counter += credit
    elif grade =='B':
        points += A * credit
        credit_counter += credit
    elif grade =='C+':
        points += C_PLUS * credit
        credit_counter += credit
    elif grade =='C':
        points += C * credit
        credit_counter += credit
    elif grade =='D+':
        points += D_PLUS * credit
        credit_counter += credit
    elif grade =='D':
        points += D * credit
        credit_counter += credit
    elif grade =='F':
        points += F * credit
        credit_counter += credit
    grade = input("Enter grade(Press enter to quit): ")

gpa = points / credit_counter

#Reporting grade point average

print("Your GPA is %.2f"%gpa)
    
    
