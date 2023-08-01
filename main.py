from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
def boas_vindas(name: str):
    return {"message":f"Olá {name}, Bem Vindo!"}
@app.get("/items/{item_id}")
def id_product(item_id: int):
    return{"ID Item": f"{item_id}"}