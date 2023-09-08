from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to hidden-plate API"}

@app.get("/blur")
async def get_blurred():
    return{"message": "blurring your imgaes"}
