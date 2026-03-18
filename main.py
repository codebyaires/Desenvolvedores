from fastapi import FastAPI

app = FastAPI()

@app.get()
def root():
    return {"message": "Bem-vindo!"}

#@app.get("/somar")

#@app.get("/subtrair")

#@app.get("/dividir")

#@app.get("/multiplicar")

#@app.get("/exponenciar")

#@app.get("/exponenciar")

#@app.get("/fatorar")