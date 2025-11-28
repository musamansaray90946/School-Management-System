from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="School Management System",
    description="Modern REST API with user login & full student management – Built with FastAPI",
    version="1.0",
    contact={"name": "Your Name", "email": "your.email@gmail.com"},
    license_info={"name": "MIT"}
)

users = {"admin": "123456}
students: List[dict] = []

class Student(BaseModel):
    id: int = None
    name: str
    age: int
    grade: str

@app.get("/", tags=["Home"])
def home():
    return {"Welcome to School Management API": "Go to /docs for interactive testing"}

@app.post("/login", tags=["Auth"])
def login(username: str = Form(), password: str = Form()):
    if users.get(username) == password:
        return {"access_token": "demo-jwt-2025", "token_type": "bearer", "role": "admin"}
    raise HTTPException(401, "Incorrect credentials")

@app.post("/students/", response_model=Student, tags=["Students"])
def add_student(s: Student):
    s.id = len(students) + 1
    students.append(s.dict())
    return s

@app.get("/students/", response_model=List[Student], tags=["Students"])
def list_students():
    return students

@app.delete("/students/{sid}", tags=["Students"])
def delete_student(sid: int):
    for i, s in enumerate(students):
        if s["id"] == sid:
            students.pop(i)
            return {"deleted": sid}
    raise HTTPException(404, "Not found")