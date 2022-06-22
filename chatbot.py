import menuDuvidas as duvidas
import menuInformacoes as  informcoes 
import sair
import os
 
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def chatbot():
    inciar = True
    clear()
    print("Oi, meu nome é Ia, sou a atendente virtual da ProgLife \n")
    while inciar:
        print("[1] Informações")
        print("[2] Cursos")
        print("[3] Duvidas")
        print("[sair] Sair")
        print("\n")
        escolhaMenuPrincipal = input("Como posso te ajudar ? ")
        if(escolhaMenuPrincipal == '1'):
            clear()
            print("Você escolheu Imformações \n ")
            informcoes.Menu_infomações()
        elif(escolhaMenuPrincipal == '2'):
            clear()
            print("Você a opção de Cursos")
        elif(escolhaMenuPrincipal == '3'):
            clear()
            print("Você escolher duvidadas")
            duvidas.duvidas()
        elif(escolhaMenuPrincipal.lower() == "sair"):
            clear()
            inciar = sair.sair()
        else:
            clear()
            print("\n Por favor, Digite uma opção valida \n")



chatbot()