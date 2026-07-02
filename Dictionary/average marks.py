#Store subject marks in a dictionary and calculate total and average marks

def calculate_subject_marks():
    print("Question: Enter marks of each subject and calculate the total and average marks.")

    marks = {}

    n = int(input("Enter number of subjects: "))
    for _ in range(n):
        sub = input("Enter subject name: ")
        marks[sub] = int(input("Enter marks: "))

    total = sum(marks.values())
    average = total / n

    print("Total Marks:", total)
    print("Average Marks:", average)


calculate_subject_marks()