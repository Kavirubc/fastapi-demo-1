from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#link - https://www.youtube.com/watch?v=tLKKmouUams

#Creating an instance of FastAPI
app = FastAPI()

students = {
    1: {
        "name": "jhon",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "khan",
        "age": 18,
        "year": "year 15"
    }
}


class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str]
    age : Optional[int]
    year : Optional[str]


#Creating an endpoint
@app.get("/")
def index():
    return {"Name": "First Data"}

#Path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Input the Id of the student", gt=0)):
    return students[student_id]
    #inorder to get only the name or something like that
    # return {"name" : students[student_id]["name"]}

#Query parameters

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int,name : Optional[str] = None, test :int = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}


#Request passing
@app.post("/create-student/{student_id}")
def create_student(student_id:int, student :Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

#Put method

@app.put("/update-student/{student_id}")
def update_stduent(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name !=None:
        students[student_id].name = student.name

    if student.age !=None:
        students[student_id].age = student.age

    if student.year !=None:
        students[student_id].year = student.year

    
    return students[student_id]
