import menuDuvidas as duvidas
import menuInformacoes as  informacoes 
import menuConsultas as consultas
import sair
import os
 
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def chatbot():
    iniciar = True
    clear()
    print("Oi, meu nome é Ia, sou a atendente virtual da ProgLife \n")
    while iniciar:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de informacoes! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print("[1] Informações")
        print("[2] Cursos")
        print("[3] Duvidas")
        print("[sair] Sair")
        print("\n")
        escolhaMenuPrincipal = input("Como posso te ajudar ? ")
        if(escolhaMenuPrincipal == '1'):
            clear()
            print("Você escolheu Informações \n ")
            informacoes.Menu_infomações()
        elif(escolhaMenuPrincipal == '2'):
            clear()
            print("Você escolheu a opção de Cursos")
            consultas.consultas()
        elif(escolhaMenuPrincipal == '3'):
            clear()
            print("Você escolheu a opção de	Duvidas")
            duvidas.duvidas()
        elif(escolhaMenuPrincipal.lower() == "sair"):
            clear()
            iniciar = sair.sair()
        else:
            clear()
            print("\n Por favor, Digite uma opção valida \n")



chatbot()