#ATRIBUTOS: TITULAR, SALDO
#METODOS: DEPOSITAR, SACAR, MOSTRAR_SALDO
import os
import json

class Banco():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Valor depositado, Saldo atual: {self.saldo} R$")
    def sacar(self,valor):
        if valor > self.saldo:
            print("*SALDO INSUFICIENTE*")
        else:
            print("Insira valor para saque.")
            self.saldo -= valor
    def mostrar_saldo(self):
        print(f"Saldo Atual: {self.saldo} R$")
    def salvar(self):
        dados = {
            "titular": self.titular,
            "saldo": self.saldo
        }
        with open("conta.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_conta():
        try:
            with open("conta.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return Banco(dados["titular"], dados["saldo"])
        except FileNotFoundError:
            return None

def limpar():
    os.system("cls")
def voltar():
    print("*ENTER PARA VOLTAR*")
    input("")

conta = carregar_conta()

while True:
    try:
        limpar()
        if conta is None:
            print(f"""
            {"-"*30}
            {"CONTA BANCÁRIA".center(30)}
            {"-"*30}
            {"-CADASTRE USUARIO-"}
            """)
            nome_usuario = str(input(f"{">".center(5)}"))
            conta = Banco(nome_usuario, 0)
        limpar()
        print(f"""
        {"-"*30}
        {f"BEM VINDO, {conta.titular.upper()}".center(30)}
        {"CONTA BANCÁRIA".center(30)}
        {"-"*30}
        {"1 -DEPOSITAR-"}
        {"2 -SACAR-"}
        {"3 -SALDO-"}
        """)
        resposta = input(f"{">".center(5)}")
        #DEPOSITO
        if resposta.lower() == "depositar" or "1":
            limpar()
            print("Insira valor para depositar.")
            valor = int(input(f"{">".center(5)}"))
            conta.depositar(valor)
            conta.salvar()
            voltar()
        #SACAR
        if resposta.lower() == "sacar" or "2":
            limpar()
            print("Insira valor para saque.")
            conta.mostrar_saldo()
            if conta.saldo == 0:
                voltar()
            else:
                valor = int(input(f"{">".center(5)}"))
                conta.sacar(valor)
                conta.salvar()
                voltar()
        #MOSTRAR SALDO
        if resposta.lower() == "saldo" or "3":
            limpar()
            conta.mostrar_saldo()
            voltar()
    except ValueError:
        print("Digite um valor válido.")
        voltar()
    continue