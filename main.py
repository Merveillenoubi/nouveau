from fastapi import FastAPI

# Initialisation de l'application FastAPI
app = FastAPI()

@app.get("/")
async def test():
    return {"message": "merveilleOK"}
