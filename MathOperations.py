# Devoir 2 :
# 3 :

from random import randint

def MathQuestions(operation):
    CorrectAnswers = 0
    if(operation == 0):
        print("SVP donnez les reponses aux 10 additions suivantes : ")
        for i in range(1, 11):
            f_num = randint(0, 9)
            s_num = randint(0, 9)
            a_num = (f_num + s_num)
            stu_answ = int(input(str(f_num) + " + " + str(s_num) + " = "))
            if(stu_answ == a_num):
                CorrectAnswers += 1
            else:
                print("Incorrect - vous avez dit : ", stu_answ, "la réponse était : ", a_num)
    elif(operation == 1):
        print("SVP donnez les reponses aux 10 multiplications suivantes : ")
        for i in range(1, 11):
            f_num = randint(0, 9)
            s_num = randint(0, 9)
            a_num = (f_num * s_num)
            stu_answ = int(input(str(f_num) + " * " + str(s_num) + " = "))
            if(stu_answ == a_num):
                CorrectAnswers += 1
            else:
                print("Incorrect - vous avez dit : ", stu_answ, "la réponse était : ", a_num)

    return CorrectAnswers

def VerifAnswers(Answers):
    print(Answers, " bonnes réponses correctes")
    if(Answers > 6):
        print("Félicitation! Vous avez obtenu : ", (Answers * 10), "%")
    else:
        print("Demandez à votre enseignant(e) de vous aider. Vous avez obtenu : ", (Answers * 10), "%")

operation = 2
while((operation != 0) and (operation != 1)):
    operation = int(input("Voulez-vous faire des additions (0) ou des multiplications (1) ?(0/1) : "))
VerifAnswers(Answers = MathQuestions(operation))

