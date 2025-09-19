#---------Gradebook--------
#Using a list of numbers, your application will need to calculate the average score for list.
#You will then take that score and print the corresponding letter grade.
#Use a function (create one) to find the corresponding letter grade.
#Rerun application for each test case.  Do not use loops.

# Function created to get letter grade based on student grade average
def letter_Grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Prompt to ask for student name
studentName = input("Please enter Student Name: ")

# Prompt to ask for the 5 grades individually
studentGrade1 = int(input("Please enter Grade 1: "))
studentGrade2 = int(input("Please enter Grade 2: "))
studentGrade3 = int(input("Please enter Grade 3: "))
studentGrade4 = int(input("Please enter Grade 4: "))
studentGrade5 = int(input("Please enter Grade 5: "))

# List created to store entered grades
gradeList = [studentGrade1, studentGrade2, studentGrade3, studentGrade4,studentGrade5]

# Avg calculated of the 5 grades and grade given based on calculation
averageGrade = sum(gradeList) / len(gradeList)
letter = letter_Grade(averageGrade)

# Print the desired output
print(studentName)
print(f"Average: {averageGrade}")
print(f"Letter Grade: {letter}")