import pytest
from employee_management_system.employee_manager import EmployeeManager
from employee_management_system.models import Employee

from pydantic import ValidationError

@pytest.fixture
def manager():
    """Feature to create a new EmployeeManager instance before each test."""
    return EmployeeManager()

def test_add_employee(manager):
    """Test adding a valid employee."""
    employee_data = {
        "employee_id": 1,
        "name": "Sammy James",
        "age": 30,
        "department": "IT",
        "role": "Developer",
        "salary": 5000
    }
    manager.add_employee(employee_data)
    
    assert len(manager.employees) == 1
    assert manager.employees[0].name == "John Doe"

def test_add_employee_invalid_age(manager):
    """Test adding an employee with an invalid age (below 18)."""
    employee_data = {
        "employee_id": 2,
        "name": "T-Bag Smith",
        "age": 16,  # Invalid age
        "department": "HR",
        "role": "HR",
        "salary": 4500
    }
    
    with pytest.raises(ValidationError):
        manager.add_employee(employee_data)

def test_find_employee_by_id(manager):
    """Test finding an employee by ID."""
    employee_data = {
        "employee_id": 3,
        "name": "Micheal Scofiled",
        "age": 28,
        "department": "Marketing",
        "role": "Sales",
        "salary": 4000
    }
    manager.add_employee(employee_data)
    
    found_employee = manager.find_employee_by_id(3)
    assert found_employee is not None
    assert found_employee.name == "Micheal Scofiled"

def test_find_employee_not_found(manager):
    """Test searching for an employee that does not exist."""
    found_employee = manager.find_employee_by_id(999)
    assert found_employee is None  # Should return None if not found

def test_delete_employee(manager):
    """Test deleting an employee."""
    employee_data = {
        "employee_id": 4,
        "name": "David Miller",
        "age": 35,
        "department": "Finance",
        "role": "Manager",
        "salary": 6000
    }
    manager.add_employee(employee_data)
    
    assert len(manager.employees) == 1
    
    manager.delete_employee(4)
    
    assert len(manager.employees) == 0  # Should be empty after deletion

def test_delete_non_existent_employee(manager):
    """Test deleting an employee that does not exist."""
    result = manager.delete_employee(999)
    assert result is False  # Should return False when deleting a non-existent employee
