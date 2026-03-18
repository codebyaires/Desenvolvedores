import math
# Função raiz quadrada
@app.get("/raiz")
def raiz(numero: float):

    resultado = math.sqrt(numero)
    return {"numero": numero, "raiz": resultado}