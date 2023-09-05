import csv

employees = open('EmployeePay.csv', 'r')

csv_file = csv.reader(employees)

next(employees)

for rec in csv_file:
    print(f"first name: {rec[1]}")
    print(f"last name: {rec[2]}")
    salary = float(rec[3])
    print(f"Salary: ${salary:10,.2f}")
    bonus_percentage = float(rec[4])
    bonus = salary * bonus_percentage
    print(f"Bonus:  ${bonus:10,.2f}")
    pay = bonus + salary
    print(f"Pay:    ${pay:10,.2f}\n")

employees.close()