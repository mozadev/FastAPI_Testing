from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    """
    Test client,
    
    ;return: Mensaje de bienvenida en formato JSON.
    """
    return {"message": "Hello World"}