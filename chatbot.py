import os

def chatbot():
    inciar = True

    print("Oi, meu nome é Ia, sou a atendente virtual de ProgLife \n")
    while inciar:
        print("[1] Imformações")
        print("[2] Cursos")
        print("[3] Duvidas")
        print("[sair] Sair")
        print("\n")
        escolhaMenuPrincipal = input("Como posso te ajudar ? ")
        if(escolhaMenuPrincipal == '1'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Você escolheu Imformações \n ")
        elif(escolhaMenuPrincipal == '2'):
            print("Você a opção de Cursos")
        elif(escolhaMenuPrincipal == '3'):
            print("Você escolher duvidadas")
        elif(escolhaMenuPrincipal == "sair"):
            inciar = False
        else:
            print("\n Por favor, Digite uma opção valida \n")


chatbot()