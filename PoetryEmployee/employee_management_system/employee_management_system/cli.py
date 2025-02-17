import argparse
from employee_manager import EmployeeManager

# Initialize the EmployeeManager
manager = EmployeeManager()

def main():
    parser = argparse.ArgumentParser(description="Employee Management System")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Employee Command
    add_parser = subparsers.add_parser("add", help="Add a new employee")
    add_parser.add_argument("--id", type=int, required=True, help="Employee ID")
    add_parser.add_argument("--name", type=str, required=True, help="Employee Name")
    add_parser.add_argument("--age", type=int, required=True, help="Employee Age")
    add_parser.add_argument("--department", type=str, required=True, help="Department")
    add_parser.add_argument("--role", type=str, required=True, help="Role")
    add_parser.add_argument("--salary", type=float, required=True, help="Salary")

    # List Employees Command
    subparsers.add_parser("list", help="List all employees")

    # Find Employee Command
    find_parser = subparsers.add_parser("find", help="Find an employee by ID")
    find_parser.add_argument("--id", type=int, required=True, help="Employee ID")

    # Delete Employee Command (with confirmation)
    delete_parser = subparsers.add_parser("delete", help="Delete an employee by ID")
    delete_parser.add_argument("--id", type=int, required=True, help="Employee ID")

    # Parse the arguments
    args = parser.parse_args()

    # Handle Commands
    if args.command == "add":
        employee_data = {
            "employee_id": args.id,
            "name": args.name,
            "age": args.age,
            "department": args.department,
            "role": args.role,
            "salary": args.salary
        }
        manager.add_employee(employee_data)

    elif args.command == "list":
        manager.list_employees()

    elif args.command == "find":
        employee = manager.find_employee_by_id(args.id)
        if employee:
            print(f"✅ Found Employee: {employee.name}, {employee.department}, ${employee.salary}")
        else:
            print(f"❌ Employee with ID {args.id} not found.")

    elif args.command == "delete":
        employee = manager.find_employee_by_id(args.id)
        if employee:
            confirm = input(f"⚠️ Are you sure you want to delete {employee.name}? (y/n): ").strip().lower()
            if confirm == "y":
                manager.delete_employee(args.id)
            else:
                print("✅ Deletion canceled.")
        else:
            print(f"❌ Employee with ID {args.id} not found.")

if __name__ == "__main__":
    main()
