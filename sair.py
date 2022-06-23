import os
 
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def sair():
    text = input('Sair (s/n)?')
    if(text.lower() == 's'):
        feedb = input("Deseja deixar um feedback (s/n)? ")
        if(feedb.lower() == 's'):
            salvarFeedback()
            print("Obrigado pelo seu FeedBack e até mais! :)")
            return False
        else:
            print("Até mais! :)")
            return False 
            
    else:
        return True

def salvarFeedback():
    text = input("Qual seu feedback ? ")
    with open('feedback.txt', 'a') as arquivoFeedback:
        arquivoFeedback.write('\n' + text)
    