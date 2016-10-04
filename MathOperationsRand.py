# Devoir 2 :
# 4 :

from random import randint

def MathQuestions():
    CorrectAnswers = 0
    operation = randint(0,1)
    f_num = randint(0, 9)
    s_num = randint(0, 9)
    if(operation == 0):
        a_num = (f_num + s_num)
        stu_answ = int(input(str(f_num) + " + " + str(s_num) + " = "))
        if(stu_answ == a_num):
            CorrectAnswers += 1
        else:
            print("Incorrect - vous avez dit : ", stu_answ, " et la réponse était : ", a_num)
    elif(operation == 1):
        a_num = (f_num * s_num)
        stu_answ = int(input(str(f_num) + " * " + str(s_num) + " = "))
        if(stu_answ == a_num):
            CorrectAnswers += 1
        else:
            print("Incorrect - vous avez dit : ", stu_answ, " et la réponse était : ", a_num)
    return CorrectAnswers

def VerifAnswers(Answers):
    print(Answers, " bonnes réponses correctes")
    if(Answers > 6):
        print("Félicitation! Vous avez obtenu : ", (Answers * 10), "%")
    else:
        print("Demandez à votre enseignant(e) de vous aider. Vous avez obtenu : ", (Answers * 10), "%")

print("Répondez du mieux que vous pouvez !!!")
r_answers = 0
for i in range(1, 11):
    Answers = MathQuestions()
    r_answers += Answers
VerifAnswers(r_answers)
