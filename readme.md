# FastAPI Demo

This is a demo application showcasing the usage of FastAPI framework. It provides endpoints for managing student data.

## Installation

To run this application, follow these steps:

1. Clone the repository: `git clone https://github.com/Kavirubc/fastapi-demo-1`
2. Navigate to the project directory: `cd fastapi-demo`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the application: `uvicorn main:app --reload`

## Usage

Once the application is running, you can access the following endpoints:

- `GET /` - Returns the first data.
- `GET /get-student/{student_id}` - Retrieves a student by their ID.
- `GET /get-by-name/{student_id}` - Retrieves a student by their name.
- `POST /create-student/{student_id}` - Creates a new student.
- `PUT /update-student/{student_id}` - Updates an existing student.
- `DELETE /delete-student/{student_id}` - Deletes a student.

Please refer to the code comments for more details on each endpoint.

## Documentation

http://127.0.0.1:8000/docs - For Docs

For detailed documentation on the FastAPI framework, please visit the official [FastAPI documentation](https://fastapi.tiangolo.com/).
