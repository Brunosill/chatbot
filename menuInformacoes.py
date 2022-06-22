import os

clear = lambda: os.system ("cls"  if os.name == "nt" else "clear")

def infomações_Horario ():
    continuar = True;
    while continuar:
        print ( '-' * 20 )
        print (  'Nossos cursos são de segunda à quinta, das 19 ás 22 horas' )
        print ( '-' * 20 )
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False

def infomações_contatos ():
    continuar = True;
    while continuar:
        print ( '-' * 20 )
        print (  'Telefone: (000) 99999-9999' )
        print ( '-' * 20 )
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False

def infomações_trabalhe_conosco ():
    continuar = True;
    while continuar:
        print ( '-' * 20 )
        print ( ' Trabalhe conosco, envie seu curriculo para email_email@email.com' )
        print ( '-' * 20 )
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False

def Menu_infomações ():
    iniciar = True
    while iniciar:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao nosso portal de infomações! ')
        print ('-' * 20)
        print ()
        print ('Menu de opcões:')
        print ('[1] Horário dos cursos ')
        print ('[2] Informações para contato')
        print ('[3] Quer trabalhar conosco ? ')
        print ('[4] Para retornar ao menu inicial!')
        print ()
        infomações = input('Escolha uma das opcoes acima: ')
        print ()
        if infomações == '1':
            infomações_Horario ()
        elif infomações == '2':
            infomações_contatos ()
        elif infomações == '3':
            infomações_trabalhe_conosco ()
        elif infomações == '4':
            iniciar = False