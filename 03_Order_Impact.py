from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello"
'''
Below code throws error when /about path is accessed
    * Because the paths are matched from top to bottom
    * "/about" matches "/{id}" where "id = about" 

    * Avoid this by changing their order

        @app.get("/{id}")
        def get_id_desc(id: int):
            return {"data" : id}

        @app.get("/about")
        def get_id_desc():
            return {"data" : "this is about page"}

'''

@app.get("/about")
def get_id_desc():
    return {"data" : "this is about page"}

@app.get("/{id}")
def get_id_desc(id: int):
    return {"data" : id}

        