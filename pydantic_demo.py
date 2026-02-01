from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Piyush"
    age: Optional[int] = None,
    cgpa: float = Field(gt=0, lt=10, default=5, description="a decimal value representing the cgpa of the student")


new_student = {"age": 21, "cgpa": 5.6}

student = Student(**new_student)

print(student)