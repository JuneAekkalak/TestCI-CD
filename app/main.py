from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    global names 
    names = name
    return {"hello": name}

@app.post("/callname")
def post_name():
    return {"hello": names}


handler = Mangum(app)
