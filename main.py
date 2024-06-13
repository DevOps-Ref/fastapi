

from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
import csv
import os



class User(BaseModel):
    userId : int
    userName :str
    type : str
    address : str
    phone : str

app = FastAPI()


# Define the path to your templates directory
templates = Jinja2Templates(directory="templates")

'''
@app.get("/")
def read_root():
    return {"Hello":"world"}

@app.get("/forms")
def forms_list(request:Request): # request is compulsory when rendering template
    context = {"request":request}
    return templates.TemplateResponse("forms.html",context)




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
'''
@app.post("/register")
def register_user(user: User):
    # 
    if not os.path.isfile("users.csv"):
        with open("users.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header row
            header = [attr for attr in dir(User) if not attr.startswith('__')]
            print(header)
            writer.writerow(header)
            csvfile.close()
             
    
    with open("users.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(list(user))
        csvfile.close()

    return "registered user"

    


