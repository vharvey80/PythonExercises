# Program that counts the factorial of a positive number.

def AskNumber():
    while True:
        number = input("Enter a positive number: ")
        try:
            val = int(number)
            if val < 0:  # if not a positive int print message and ask for input again
                print("Sorry, input must be a positive number, try again..")
                continue
            break
        except ValueError:
            print("That's not a number!")
    return int(number)

def CountFact(a):
    number = 1
    mystr = str(a)
    for i in range(1, (a + 1)):
        if(i == 1):
            mystr = mystr + ("! = " + str(i))
        else:
            mystr = mystr + ("*" + str(i))
        number = number * i

    print(mystr)
    return number

number = AskNumber()
fact = CountFact(number)
print("Factiorial of ", number, " is : " , fact)
       


