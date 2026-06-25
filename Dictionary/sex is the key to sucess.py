# Q6. Accepts a dictionary holding 10 employee names and their salaries. Loops through .items() to print the names of all employees whose salary exceeds 50000.
def display_high_earners(emp_data):
    for name in emp_data:
        if emp_data[name] > 50000:
            print(name)

employees = {"Amit": 40000, "Rahul": 60000, "Neha": 55000, "Priya": 45000}
print("High Earners:")
display_high_earners(employees)