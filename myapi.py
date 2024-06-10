from fastapi import FastAPI, Path
from typing import Optional

#Creating an instance of FastAPI
app = FastAPI()

students = {
    1: {
        "name": "jhon",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "khan",
        "age": 18,
        "class": "year 15"
    }
}


#Creating an endpoint
@app.get("/")
def index():
    return {"Name": "First Data"}

#Path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Input the Id of the student", gt=0, lt=3)):
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

