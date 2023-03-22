from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.options("/")
async def handle_options():
    return {"Allow": "POST"}

@app.post("/generate_output")
async def generate_output(input: dict):
    
     Retrieve the input string from the request body
    input_str = input["input"]
    
    TODO: Write code to generate the output string using your logic here
    output_str = input_str[::-1]
    
     Return a JSON response containing the generated output
    return JSONResponse(content={"output": output_str})

# @app.route("/")

# # todo
# @app.get("/checkstr")
# async def check():
#     pass

# # todo
# @app.get("/checkimg")
# async def check():
#     pass
