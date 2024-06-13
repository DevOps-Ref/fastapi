# FASTAPI
## SETUP
        pip install fastapi
            fastapi
            starlette
            pydantic
        pip install uvicorn

## START SERVER
* RUN from COMMAND PROMPT
```
    uvicorn <python file>:<Fastapi object> --reload 
            reload :: to reload the sever every time it is saved 
```
* RUN in Python code
```
    uvicorn.run("<python file>:<FastAPI object>",host="localhost",reload=True)
```

# BASIC API (01_Basic.py)
```
    from fastapi import FastAPI
    import uvicorn
    app = FastAPI()

    @app.get('/') # /  :: path / endpoint / route
    def BasicAPI():
        return "Basic_API"

    if __name__ == "__main__":
        uvicorn.run("01_Basic:app",host="localhost",reload=True)
```


# Terminology
* <mark> PATH </mark>  ::  /about
* <mark>OPERATION </mark>  :: get | post
* <mark>PATH OPERATION FUNCTION </mark>:: function

# PATH PARAMETER (02_Path_Parameters.py)
* By specifying path parameter datatype
        * We can perform typecasting(Done by pydantic under the hood)
        * We can perform datatype validation
* If datatype is not specified then it accepts any value.
```
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def home():
        return "Please Enter id in path as Path parameter"

    @app.get("/{id}")
    def get_id_desc(id: int):
        return {id: "the id given as path parameter"}
```

## IMPACT OF ORDER OF "PATH OPEARTION FUNCTIONS" (03_Order_Impact.py)
* The Path matching is done from top to bottom and it stops looking after the first match is found.
* So order is important

E.G : TRY  finding <mark><b> /about </b></mark> path in Both scenarios



<div style="display:flex;">

<div>
<pre style="display:inline-block;background-color:green;">
@app.get("/about")
def get_id_desc():
    return {"data" : "this is about page"}

@app.get("/{id}")
def get_id_desc(id: int):
    return {"data" : id}
</pre>
</div>

<div>
<pre style="display:inline-block;background-color:red;">
@app.get("/{id}")
def get_id_desc(id: int):
    return {"data" : id}

@app.get("/about")
def get_id_desc():
    return {"data" : "this is about page"}
</pre>
</div>

</div>


## QUERY PARAMETER
<b>NOTE</b>:
* <mark><b> Specify default values </b></mark> for Query parameters or-else <u>error is thrown when we miss providing values</u> to "limit, published"
* Specify Optional Values
* We can pass any number of parameters

```
@app.get("/blog")
def get_blogs(limit:int = 10,published:bool = True, sort:Optional['str']=None):
    if published:
        return f"Here are the {limit} blogs from the published blogs"
    else:
        return f"Here are the {limit} blogs from all the blogs"
```

## REQUEST BODY (05_Request_Body.py)
* <b>REQUEST BODY</b> is <mark><b> Data sent by client  </b></mark>
* PYDANTIC MODELS are used to declare request body

```
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

# Specify tags if you want
@app.get("/emp_details", tags=["EMP_DETAILS"])
def home():
    return "hello"

@app.post("/emp_details/create", tags=["EMP_DETAILS"])
def create_emp(emp_details:Post_Data):
    print(emp_details,list(emp_details))
    return (emp_details)
```

