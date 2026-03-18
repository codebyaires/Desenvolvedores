from fastapi import FastAPI

# Os Imports dos arquivos dos colaboradores afiliados
import somaf
import divisaof
import raiz

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bem-vindo!"}

# --- ROTAS DE ACESSO DOS JÚNIORS: ---

@app.get("/somar")
def rota_somar(a: float, b: float):
    # Chama o arquivo 'somaf' e a função 'somar'
    resultado = somaf.somar(a, b) 
    return {"resultado": resultado}

@app.get("/dividir")
def rota_dividir(a: float, b: float):
    # Chama o arquivo 'divisaof' e a função 'dividir'
    resultado = divisaof.dividir(a, b)
    return {"resultado": resultado}

@app.get("/raiz")
def rota_raiz(numero: float):
    # Chama o arquivo 'raiz' e a função 'raiz'
    resultado = raiz.raiz(numero)
    return {"numero": numero, "raiz": resultado}

# --- Função Multiplicar Que fiz Integrada direto na Main ---

@app.get("/multiplicar")
def multiplicar(a: float, b: float):
    resultado = a * b
    return {"resultado": resultado}

# --- ROTAS PENDENTES ---

# @app.get("/subtrair")
# @app.get("/exponenciar")
# @app.get("/fatorar")