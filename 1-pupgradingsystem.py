# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropped

# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

def getLetter():
    prelimq = input("Is your grade INC, W, or D? Please enter Yes or No: ")
    if prelimq == "Yes":
        textgrade = input("Please enter if your grade is INC, W, or D: ") 
        return textgrade
    else:
        if prelimq == "No":
            _grade = float(input(("Enter your grade here: ")))
            grade = round(_grade)
            return grade




inputGrade = getLetter()






