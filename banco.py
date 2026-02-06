#IMPORTAÇÃO
import os
import json

#CLASSE DO BANCO

class Banco():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    #DEPOSITO
    def depositar(self, valor):
        self.saldo += valor
        print(f"Valor depositado.\nSaldo atual: {self.saldo} R$")
    #SAQUE
    def sacar(self,valor):
        if valor > self.saldo:
            print("*SALDO INSUFICIENTE*")
        else:
            print("Insira valor para saque.")
            self.saldo -= valor
    #MOSTRAR CALOR
    def mostrar_saldo(self):
        print(f"Saldo Atual: {self.saldo} R$")
    #SALVAR INFORMAÇÃO EM JSON
    def salvar(self):
        dados = {
            "titular": self.titular,
            "saldo": self.saldo
        }
        with open("conta.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

#FUNÇÃO
    #CARREGAR CONTA EXISTENTE
def carregar_conta():
        try:
            with open("conta.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return Banco(dados["titular"], dados["saldo"])
        except FileNotFoundError:
            return None
    #LIMPAR TERMINAL
def limpar():
    os.system("cls")
    #VOLTAR PARA MENU
def voltar():
    print("*ENTER PARA VOLTAR*")
    input("")

#CARREGAMENTO DA CONTA
conta = carregar_conta()
#MENU
while True:
    try:
        limpar()
        if conta is None: #CASO USUARIO NAO TENHA CADASTRO AINDA, CRIAR CONTA.
            print(f"""
            {"-"*30}
            {"CONTA BANCÁRIA".center(30)}
            {"-"*30}
            {"-CADASTRE USUARIO-"}
            """)
            nome_usuario = str(input(f"{">".center(5)}"))
            conta = Banco(nome_usuario, 0)
        else: #CONTINUA CASO CONTA JA EXISTA
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
            resposta = input(f"{">".rjust(5)}")

            #DEPOSITO
            if resposta.lower() in ("depositar" "1"):
                limpar()
                print("Insira valor para depositar.")
                valor = float(input("> "))
                conta.depositar(valor)
                conta.salvar()
                voltar()
            
            #SACAR
            elif resposta.lower() in ("sacar", "2"):
                limpar()
                print("Insira valor para saque.")
                conta.mostrar_saldo()
                if conta.saldo == 0:
                    voltar()
                else:
                    valor = float(input("> "))
                    conta.sacar(valor)
                    conta.salvar()
                    voltar()
            
            #MOSTRAR SALDO
            elif resposta.lower() in ("saldo", "3"):
                limpar()
                conta.mostrar_saldo()
                voltar()
    #EXCEPT
    except ValueError:
        limpar()
        print("Digite um valor válido.")
        voltar()
    continue