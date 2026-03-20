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

print("Seja Vindo a nosso sistema de calculadora!")
print("Temos algumas opções de calculos, escolha uma delas para usar")
print("1- Calcula de somas")
print("2- Calcula de Subtração")
print("3- Calcula de Divisão")
opcao = int(input("Digite o número da opção desejada: "))

match opcao:
  case 1:
    # Tenho que puxar a função as opções correspondentes e colocar uma caixa de input para que o úsuario escolha a conta
    # que ele quer que o programa execute (continuar daqui) 
    # Acredito que de para colocar o app.get dentro das opções já, para que puxe, já puxe certo. 
    #Entretanto isso é apenas suposição ainda. Abraços do Scrum Master!!
    print("Today is Saturday")
  case 2:
    print("Today is Sunday")
  case 3:
    print("Today is Sunday")
    # 'case _:' serve como um "se não entrar nos outros, cai nesse"
  case _:
    print("Opção Inválida, tente um número válido")