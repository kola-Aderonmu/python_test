from models import Employee
from typing import List, Optional

class EmployeeManager:
    def __init__(self):
        """Initialize an empty list to store employee records."""
        self.employees: List[Employee] = []

    def add_employee(self, employee_data: dict) -> Optional[Employee]:
        """
        Adds a new employee after validating the input data.
        
        :param employee_data: Dictionary containing employee details.
        :return: The created Employee object if successful, None otherwise.
        """
        try:
            employee = Employee(**employee_data)
            self.employees.append(employee)
            print(f"✅ Employee {employee.name} added successfully!")
            return employee
        except Exception as e:
            print(f"❌ Error adding employee: {e}")
            return None

    def list_employees(self) -> None:
        """Lists all stored employees."""
        if not self.employees:
            print("📂 No employees found.")
            return
        print("\n📌 Employee Records:")
        for emp in self.employees:
            print(f"🆔 {emp.employee_id} | {emp.name} | {emp.age} | {emp.role} | ${emp.salary}")

    def find_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """
        Searches for an employee by their ID.
        
        :param employee_id: The ID of the employee to find.
        :return: The Employee object if found, None otherwise.
        """
        for emp in self.employees:
            if emp.employee_id == employee_id:
                print(f"🔍 Employee found: {emp}")
                return emp
        print(f"❌ Employee with ID {employee_id} not found.")
        return None
