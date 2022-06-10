def sair (opcoes):
    if opcoes == 'sair' or 'Sair':
        return False
    else:
        return True
    

def consulta1 ():
    print ('-' * 20)
    print ('R: ')
    print ('-' * 20)
    print ()

def consulta2 ():
    print ('-' * 20)
    print ('R: ')
    print ('-' * 20)
    print ()
    
def consulta3 ():
    print ('-' * 20)
    print ('R: ')
    print ('-' * 20)
    print ()


def duvida1 ():
    print ('-' * 20)
    print ('R: A empresa esta aberta das 8h as 18h, de segunda a sexta!')
    print ('-' * 20)
    print ()
    
def duvida2 ():
    print ('-' * 20)
    print ('R: Para trabalhar conosco, manda seu curriculo para o email empresaficcticia@empresa.com')
    print ('-' * 20)
    print ()
    
def duvida3 ():
    print ('-' * 20)
    print ('R: Sendo assinante voce tem acesso ao nosso portal exclusivo, aulas diarias e monitorias semanais!')
    print ('-' * 20)
    print( )

def menu_inicial ():
    rodar_laco = True
    while rodar_laco:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao portal de atendimento da ProgLife')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Duvidas')
        print ('[2] Consultas')
        print ('[3] Informacoes')
        print ('[4] Digite "Sair" para finalizar o atendimento')
        print ()
        opcoes = input('Escolha uma opcao acima: ')
        if opcoes == '1':
            duvidas ()
        elif opcoes == '2':
            consultas ()
        elif opcoes == '3':
            pass
        else:
            rodar_laco = sair (opcoes)
            print('Saindo do portal!')
    
        
        
        

def duvidas():
    rodar_laco = True
    while rodar_laco:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de duvidas! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Qual o horario de funcionamento?')
        print ('[2] Trabalhe conosco')
        print ('[3] Beneficios de ser assinante')
        print ('[4] Para retornar ao menu inicial!')
        print ()
        duvidas_frequentes = input('Escolha uma das opcoes acima: ')
        print ()
        if duvidas_frequentes == '1':
           duvida1 ()
        elif duvidas_frequentes == '2':
            duvida2 ()
        elif duvidas_frequentes == '3':
            duvida3 ()
        else:
            rodar_laco = sair (duvidas_frequentes)
            print('Saindo do portal!')


def consultas():
    while True:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de consulta! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1]  ')
        print ('[2] ')
        print ('[3] ')
        print ('[4] Para retornar ao menu inicial!')
        print ()
        consulta_usuario = input('Escolha uma das opcoes acima: ')
        print ()
        if consulta_usuario == '1':
            consulta1 ()
           
        elif consulta_usuario == '2':
            consulta2 ()
            
        elif consulta_usuario == '3':
            consulta3 ()
            
        elif consulta_usuario == '4':
            menu_inicial ()
    
    

menu_inicial ()