from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname", methods=["POST", "GET"])
async def post_name():
    name = "june"
    return {"hello": name}


handler = Mangum(app)
