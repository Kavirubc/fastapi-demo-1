from fastapi import FastAPI

#Creating an instance of FastAPI
app = FastAPI()

#Creating an endpoint

@app.get("/")
def index():
    return {"Name": "First Data"}
