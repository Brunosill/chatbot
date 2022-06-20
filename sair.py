



def salvarFeedback():
    text = input("Qual seu feedback e ")
    with open('feedback.txt', 'a') as arquivoFeedback:
        arquivoFeedback.write('\n' + text)
