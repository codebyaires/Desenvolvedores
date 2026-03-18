# Função soma
@app.get("/somar")
def somar(a: int, b: int):
    return {"resultado": a + b}