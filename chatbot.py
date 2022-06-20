import menuDuvidas as duvidas
import sair
import os

def chatbot():
    inciar = True

    print("Oi, meu nome é Ia, sou a atendente virtual da ProgLife \n")
    while inciar:
        print("[1] Imformações")
        print("[2] Cursos")
        print("[3] Duvidas")
        print("[sair] Sair")
        print("\n")
        escolhaMenuPrincipal = input("Como posso te ajudar ? ")
        if(escolhaMenuPrincipal == '1'):
            
            print("Você escolheu Imformações \n ")
        elif(escolhaMenuPrincipal == '2'):
            print("Você a opção de Cursos")
        elif(escolhaMenuPrincipal == '3'):
            clear = lambda: os.system("clear")
            clear()
            print("Você escolher duvidadas")
            duvidas.duvidas()
        elif(escolhaMenuPrincipal == "sair"):
            sair.salvarFeedback()
            inciar = False
        else:
            print("\n Por favor, Digite uma opção valida \n")


chatbot()