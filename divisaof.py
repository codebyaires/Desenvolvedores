# Função divisão
@app.get("/dividir")
def somar(a: int, b: int):
    return {"resultado": a / b}