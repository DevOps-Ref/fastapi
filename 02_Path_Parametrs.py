from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Please Enter ID in path as Path parameter"

@app.get("/{id}")
def get_id_desc(id: int):  # id will be type casted by fast api, any other datatype will throw error
    return {"data" : id}

@app.get("/dummy/{id}")
def get_id_desc(id):
    return {"data" : id}