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
    


def consultas():
    i = True
    while i:
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
            i = False
            