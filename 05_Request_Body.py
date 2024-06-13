from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# Declaring Request BODY
# This provides an example in docs
class Post_Data(BaseModel):
    id: int
    name: str
    salary: float
    caste: Optional['str']

app = FastAPI()

@app.get("/emp_details", tags=["EMP_DETAILS"])
def home():
    return "hello"

@app.post("/emp_details/create", tags=["EMP_DETAILS"])
def create_emp(emp_details:Post_Data):
    print(emp_details,list(emp_details))
    return (emp_details)