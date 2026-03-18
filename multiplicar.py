@app.get("/multiplicar")
def multiplicar(a, b):
    return a ** b


