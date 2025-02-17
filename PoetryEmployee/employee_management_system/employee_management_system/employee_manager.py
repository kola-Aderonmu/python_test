import json
from models import Employee
from typing import List, Optional

class EmployeeManager:
    FILE_PATH = "employees.json"

    def __init__(self):
        """Initialize EmployeeManager and load employees from file."""
        self.employees = self.load_employees()

    def load_employees(self) -> List[Employee]:
        """Load employees from JSON file."""
        try:
            with open(self.FILE_PATH, "r") as file:
                data = json.load(file)
                return [Employee(**emp) for emp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_employees(self):
        """Save employees to JSON file."""
        with open(self.FILE_PATH, "w") as file:
            json.dump([emp.model_dump() for emp in self.employees], file, indent=4)

    def add_employee(self, employee_data):
        """Add a new employee and save to file."""
        try:
            employee = Employee(**employee_data)
            self.employees.append(employee)
            self.save_employees()
            print(f"✅ Employee {employee.name} added successfully!")
        except Exception as e:
            print(f"❌ Error: {e}")

    def list_employees(self):
        """List all employees from file."""
        if not self.employees:
            print("⚠️ No employees found.")
        else:
            print("\n📌 Employee Records:")
            for emp in self.employees:
                print(f"🆔 {emp.employee_id} | {emp.name} | {emp.age} | {emp.department} | ${emp.salary}")

    def find_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Find an employee by ID."""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def delete_employee(self, employee_id: int):
        """Delete an employee by ID."""
        employee = self.find_employee_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            self.save_employees()
            print(f"✅ Employee {employee.name} deleted successfully!")
        else:
            print(f"❌ Employee with ID {employee_id} not found.")

    def update_employee(self, employee_id: int, updated_data: dict):
        """Update an employee's details."""
        employee = self.find_employee_by_id(employee_id)
        if employee:
            for key, value in updated_data.items():
                if hasattr(employee, key):
                    setattr(employee, key, value)
            self.save_employees()
            print(f"✅ Employee {employee.name} updated successfully!")
        else:
            print(f"❌ Employee with ID {employee_id} not found.")
