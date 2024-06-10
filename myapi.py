from fastapi import FastAPI, Path

#Creating an instance of FastAPI
app = FastAPI()

students = {
    1: {
        "name": "jhon",
        "age": 17,
        "class": "year 12"
    }
}


#Creating an endpoint
@app.get("/")
def index():
    return {"Name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Input the Id of the student", gt=0, lt=3)):
    return students[student_id]
    #inorder to get only the name or something like that
    # return {"name" : students[student_id]["name"]}


