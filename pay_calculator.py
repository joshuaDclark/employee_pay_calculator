# create small employee profile
# Profile will include: first and last name, weekly salary, field of experience, years employed
class Employee:

    def __init__(self, first_name, last_name, field_of_experience, salary, years_employed):
        self.first_name = first_name
        self.last_name = last_name
        self.field_of_experience = field_of_experience
        self.salary = salary
        self.years_employed = years_employed

    # calculate pay with raise after 1 year of employement
    def salary_increase(self):
        if self.years_employed > 1:
            return self.salary * 3

# Show Employee Info

Emp1 = Employee('John', 'Smith', 'Engineering', 100000, 3)
Emp2 = Employee('Robert', 'Smith', 'Programming', 50000, 1)

# Perform Employee Salary Increase

print(Emp1.salary_increase())
print(Emp2.salary_increase())




















