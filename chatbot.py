import menuDuvidas as duvidas
import menuInformacoes as  informacoes 
import menuConsultas as consultas
import sair


def chatbot():
    iniciar = True
    print("Oi, meu nome é Ia, sou a atendente virtual da ProgLife \n")
    while iniciar:
        sair.clear()
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de informacoes! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print("[1] Informações")
        print("[2] Cunsultas")
        print("[3] Duvidas")
        print("[sair] Sair")
        print("\n")
        escolhaMenuPrincipal = input("Como posso te ajudar ? ")
        if(escolhaMenuPrincipal == '1'):
            print("Você escolheu Informações \n ")
            informacoes.Menu_infomações()
        elif(escolhaMenuPrincipal == '2'):
            print("Você escolheu a opção de Cursos")
            consultas.consultas()
        elif(escolhaMenuPrincipal == '3'):
            print("Você escolheu a opção de	Duvidas")
            duvidas.duvidas()
        elif(escolhaMenuPrincipal.lower() == "sair"):
            sair.clear()
            iniciar = sair.sair()
        else:
            sair.clear()
            print("\n Por favor, Digite uma opção valida \n")


chatbot()