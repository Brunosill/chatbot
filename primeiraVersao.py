def info1 ():
    print ('-' * 20)
    print ('R: A ProgLife fica aberta das 8h as 18h!')
    print ('-' * 20)
    
    
def info2 ():
    print ('-' * 20)
    print ('R: Aulas diarias, acompanhamento dos melhores professores do mercado e monitorias semanais!')
    print ('-' * 20)
    
    
def info3 ():
    print ('-' * 20)
    print ('R: Para trabalhar conosco, manda seu curriculo para o email proglife@prog.com')
    print ('-' * 20)
    

    
def consulta1 ():
    print ('-' * 20)
    print ('R: A proxima turma sera aberta no dia 20/07/2022')
    print ('-' * 20)
    

def consulta2 ():
    print ('-' * 20)
    print ('R: A formatura das turmas 1/2/3 sera no dia 09/07/2022 ')
    print ('-' * 20)
    
    
def consulta3 ():
    print ('-' * 20)
    print ('R: Ficou de recuperacao e nao conseguiu o diploma? nao se proecupe! mande um email para formacao@alunos.com para resolver sua situacao!')
    print ('-' * 20)
    


def duvida1 ():
    print ('-' * 20)
    print ('R: Atualmente temos cursos para front-end,back-end e data analyst!')
    print ('-' * 20)
    
    
def duvida2 ():
    print ('-' * 20)
    print ('R: Temos as duas opcoes disponiveis! Fica a seu criterio escolher o seu na inscricao!')
    print ('-' * 20)
    
    
def duvida3 ():
    print ('-' * 20)
    print ('R: Variam de 1 a 3 anos!')
    print ('-' * 20)
    

def menu_inicial ():
    
    while True:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao portal de atendimento da ProgLife!')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Duvidas')
        print ('[2] Consultas')
        print ('[3] Informacoes')
        print ('[4] Digite "4" para finalizar o atendimento')
        print ()
        opcoes = input('Escolha uma opcao acima: ')
        if opcoes == '1':
            duvidas ()
        elif opcoes == '2':
            consultas ()
        elif opcoes == '3':
            informacoes ()
        elif opcoes == '4':
            break
            
    
        
        
        

def duvidas():
    while True:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de duvidas! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Quais cursos a ProgLife tem disponivel? ')
        print ('[2] As aulas sao online ou presencial?')
        print ('[3] Qual a duracao dos cursos da ProgLife? ')
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
        elif duvidas_frequentes == '4':
            menu_inicial ()


def consultas():
    while True:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de consulta! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Para data de abertura da proxima turma')
        print ('[2] Para data de formatura das turmas 1/2/3')
        print ('[3] Para alunos que ficaram de recuperacao')
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
            
            
def informacoes ():
    while True:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de informacoes! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Horario de funcionamento!')
        print ('[2] Beneficios de ser aluno da ProgLife')
        print ('[3] Trabalhe conosco!')
        print ('[4] Para retornar ao menu inicial!')
        print ()
        infos_usuario = input('Escolha uma das opcoes acima:')
        print()
        if infos_usuario == '1':
            info1 ()
        elif infos_usuario == '2':
            info2 ()
        elif infos_usuario == '3':
            info3 ()
        elif infos_usuario == '4':
            menu_inicial ()
         
    
    

menu_inicial ()