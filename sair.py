def salvarFeedback():
    text = input("cQual seu feedback e ")
    with open('feedback.txt', 'a') as arquivoFeedback:
        arquivoFeedback.write('\n' + text)

salvarFeedback()