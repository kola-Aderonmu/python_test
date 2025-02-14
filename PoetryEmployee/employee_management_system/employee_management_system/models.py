from pydantic import BaseModel, Field
from typing import Literal

class Employee(BaseModel):
    employee_id: int = Field(..., gt=0, description="Employee ID must be a positive integer")
    name: str = Field(..., min_length=2, strip_whitespace=True, description="Name must have at least 2 characters")
    age: int = Field(..., ge=18, le=65, description="Age must be between 18 and 65")
    department: str = Field(..., strip_whitespace=True, description="Department must be a string")
    role: Literal["Manager", "Developer", "Designer", "HR", "Sales"]
    salary: float = Field(..., gt=0, description="Salary must be greater than zero")

    class Config:
        schema_extra = {
            "example": {
                "employee_id": 1,
                "name": "Kola Aderonmu",
                "age": 30,
                "department": "IT",
                "role": "Developer",
                "salary": 72000
            }
        }
