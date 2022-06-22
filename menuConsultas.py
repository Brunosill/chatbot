def consulta1 ():
    print ('-' * 20)
    print ('R: Nossos cursos disponíveis são: Data Analyst, Web Full Stack e Mobile Developer')
    print ('-' * 20)
    

def consulta2 ():
    print ('-' * 20)
    print ('R: Nosso corpo de professores conta com os mais qualificados profissionais do mercado como: Esli Queiroz, Marisa Silva e Yasmin Guanaes')
    print ('-' * 20)
    
    
def consulta3 ():
    print ('-' * 20)
    print ('R: As cargas horárias dos nossos cursos são: Data Analyst - 560 horas, Web Full Stack - 360 horas e Mobile Developer - 420 horas')
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
        print ('[1] Consultar cursos disponíveis')
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
            