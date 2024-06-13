from fastapi import FastAPI
from typing import List,Optional

app = FastAPI()

@app.get("/")
def home():
    return "Please pass Query PARAMETERS in URL"

'''
    NOTE:
        * Specify default values for Query parameters or-else error is thrown when
          we miss providing values to limit, published
        * We can pass any number of parameters 
'''
@app.get("/blog")
def get_blogs(limit:int = 10,published:bool = True, sort:Optional['str']=None):
    if published:
        return f"Here are the {limit} blogs from the published blogs"
    else:
        return f"Here are the {limit} blogs from all the blogs"