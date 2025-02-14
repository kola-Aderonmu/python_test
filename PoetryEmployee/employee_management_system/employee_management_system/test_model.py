from models import Employee

# Valid employee data
valid_employee = {
    "employee_id": 1,
    "name": "Alice Johnson",
    "age": 29,
    "department": "HR",
    "role": "HR",
    "salary": 55000
}

try:
    employee = Employee(**valid_employee)
    print("✅ Employee created successfully:", employee)
except Exception as e:
    print("❌ Error:", e)

# Invalid employee data (negative salary)
invalid_employee = {
    "employee_id": 2,
    "name": "Bob",
    "age": 17,  # Age too low
    "department": "IT",
    "role": "Developer",
    "salary": -20000  # Invalid salary
}

try:
    employee = Employee(**invalid_employee)
    print("✅ Employee created successfully:", employee)
except Exception as e:
    print("❌ Error:", e)
