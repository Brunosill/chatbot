def consulta1 ():
    i = True
    while i:
        print ('-' * 20)
        print ('R: Atualmente temos aulas no período matutino (8h as 10h) e noturno (19h as 21h)')
        print ('-' * 20)
        volta = input("[s] Voltar ? ")
        if volta == "s":
            i = False

    
    

def consulta2 ():
    i = True
    while i:
        print ('-' * 20)
        print ('R: Nosso corpo de professores conta com os mais qualificados profissionais do mercado como: Esli Queiroz, Marisa Silva e Yasmin Guanaes')
        print ('-' * 20)
        volta = input("[s] Voltar ? ")
        if volta == "s":
            i = False

    
    
def consulta3 ():
    i = True
    while i:
        print ('-' * 20)
        print ('R: As cargas horárias dos nossos cursos são: Data Analyst - 560 horas, Web Full Stack - 360 horas e Mobile Developer - 420 horas')
        print ('-' * 20)
        volta = input("[s] Voltar ? ")
        if volta == "s":
            i = False

    


def consultas():
    i = True
    while i:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de consulta! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Consultar horarios das aulas')
        print ('[2] Consultar corpo docente')
        print ('[3] Consultar carga horária de cada curso')
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
            