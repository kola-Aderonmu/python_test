from employee_manager import EmployeeManager

# Initialize the manager
manager = EmployeeManager()

# Sample employees
employees = [
    {"employee_id": 1, "name": "Alice Johnson", "age": 29, "department": "HR", "role": "HR", "salary": 55000},
    {"employee_id": 2, "name": "Audu Williams", "age": 35, "department": "Engineering", "role": "Developer", "salary": 80000},
    {"employee_id": 3, "name": "Ade Goke", "age": 41, "department": "Sales", "role": "Sales", "salary": 62000},
]

# Add employees
for emp_data in employees:
    manager.add_employee(emp_data)

# List all employees
manager.list_employees()

# Search for an employee
manager.find_employee_by_id(2)

# Search for a non-existent employee
manager.find_employee_by_id(99)
