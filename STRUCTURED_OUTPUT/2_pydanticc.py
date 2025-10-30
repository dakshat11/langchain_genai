from pydantic import BaseModel, EmailStr, Field
from typing import Optional
 

class Student(BaseModel):
    name : str # = "nitish"  # default value can also be passdd
    age : Optional[int] =  32
    email : EmailStr
    cgpa : float = Field(gt = 0 , lt = 10, description= " A decimal val representing the student score")  # we can give constaints from field and add our own descroption.

new_student = {'name': "nitish", "email" : "abs@gmail.com", "cgpa" : 7}

Student = Student(**new_student)

student_dict = dict(Student) # we can transform it to dict also

student_json = Student.model_dump_json() # we can transform it to json also
print(Student)