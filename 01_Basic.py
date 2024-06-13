from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/') # get | post are called oprations
def BasicAPI():  # /  :: path / endpoint / route & the function is called path operation function
    return "Basic_API"

if __name__ == "__main__":
    uvicorn.run("01_Basic:app",host="localhost",reload=True)