import os
 
clear = lambda: os.system ("cls"  if os.name == "nt" else "clear")


def duvida1 ():
    continuar = True;
    while continuar:
        clear ()
        print ('-' * 20)
        print ('R: Atualmente temos cursos para front-end,back-end e data analyst!')
        print ('-' * 20)
        print ()
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False
    
def duvida2 ():
    continuar = True;
    while continuar:
        clear ()
        print ('-' * 20)
        print ('R: Temos as duas opcoes disponiveis! Fica a seu criterio escolher o seu na inscricao!')
        print ('-' * 20)
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False
    
def duvida3 ():
    continuar = True;
    while continuar:
        clear ()
        print ('-' * 20)
        print ('R: Variam de 1 a 3 anos!')
        print ('-' * 20)
        volta = input ("[s] Voltar ? ")
        if volta == "s":
            continuar = False




def duvidas():
    iniciar = True
    while iniciar:
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
            clear ()
            duvida1 ()
        elif duvidas_frequentes == '2':
            clear ()
            duvida2 ()
        elif duvidas_frequentes == '3':
            clear ()
            duvida3 ()
        elif duvidas_frequentes == '4':
            clear ()
            iniciar = False