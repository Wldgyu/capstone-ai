from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet_json():
    return {"Hello": "World! Welcome to Cap Refrigerator!"}
