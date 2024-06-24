from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return "hello"

@app.get('/about/{id}')
def get_description(id:int):
    return f"Info of {id}"