from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"coin-grep"}

# todo
@app.get("/checkstr")
async def check():
    pass

# todo
@app.get("/checkimg")
async def check():
    pass
