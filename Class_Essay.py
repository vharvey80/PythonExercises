#Classe employé
from pathlib import Path

class Employee:

    empCount = 0
    
    #initialise ma classe employés
    def __init__(self, name = None, socialNum = None, salary = None):
        self._number = str(Employee.empCount)
        self._name = name
        self._socialNum = socialNum
        self._salary = int(salary)
        Employee.empCount += 1
        self.WriteInFile()
        
    #va écrire au fur et à mesure, dans le fichier, les employés qui ont été ajoutés
    def WriteInFile(self):
        file = open("employee.txt", "a")
        myline = "no." + self._number + ", " + self._name + ", " + self._socialNum + ", " + str(self._salary) + "\n"
        file.write(myline)
        file.close()
        
    #fait afficher toute(s) les informations du fichier
    def ReadInFile():
        if Employee.empCount < 1:
            print("Anciennes données\n")
        else:
            print("Nouvelles données\n")
        my_file = Path("employee.txt")
        if my_file.is_file():
            file = open("employee.txt", "r")
            print (file.read())
            file.close()
        else:
            print("Désolé, mais aucun fichier n'a encore été créé sous ce nom")
            
    #fait afficher le nombre(s) de ligne(s)
    def ReadLinesInFile():
        if Employee.empCount < 1:
            print("Anciennes données\n")
        else:
            print("Nouvelles données\n")
        my_file = Path("employee.txt")
        if my_file.is_file():
            file = open("employee.txt", "r")
            print ("Nombre de ligne(s) : ", len(file.readlines()))
            file.close()
        else:
            print("Désolé, mais aucun fichier n'a encore été créé sous ce nom")
            
    #fait afficher les infos de l'employé qui appel cette fonction
    # à partir du fichier (pas encore fait)
    def displayMyInfos(self):
        print ("Solution is comming ...")
        
    #fait afficher le nombre d'employé(s)
    def displayEmpCount(self):
        print ("Total employee(s) : ", Employee.empCount)
        
    #fait afficher les information de l'employé
    def displayEmployee(self):
        print ("No : ", self._number, ", Name : ", self._name, ", Social number : ",
               self._socialNum, ", Salary : ", self._salary)
        
    #calcul le salaire horaire
    def CalculTauxHoraire(self):
        #Prends pour acquis que l'employé a 2 semaines de vancances / année
        #Il travail donc 50 semaines par année et il fait 40 heures / semaine (environ)

        hourPerYear = 50 * 40
        tauxHoraire = (int(self._salary) / int(hourPerYear))
        print (tauxHoraire, "$/h")

    #Propriété du no
    @property
    def number(self):
        return self._number

    #Propriété du nom
    @property
    def name(self):
        print ("Récupération du nom de l'employé no.", self.number)
        return self._name

    @name.setter
    def name(self, n):
        print ("Modification du nom de l'employé no.", self.number)
        self._name = n

    #Propriété du numéro d'assurance social
    @property
    def socialNumber(self):
        print ("Récupération du numéro d'assurance social de l'employé no.", self.number)
        return self._socialNum

    @socialNumber.setter
    def socialNumber(self, sn):
        print ("Modification du numéro d'assurance social de l'employé no.", self.number)
        self._socialNum = sn

    #Propriété du salaire
    @property
    def salary(self):
        print ("Récupération du salaire de l'employé no.", self.number)
        return self._salary

    @salary.setter
    def salary(self, sy):
        print ("Modification du salaire de l'employé no.", self.number)
        self._salary = sy


# CODE DU MAIN
import os

my_file = Path("employee.txt")
if my_file.is_file():
    os.remove("employee.txt")

employees = []
employees.append(Employee("Vincent Harvey", "123456789", 150000))
employees.append(Employee("Lydia Oliveira", "123456987", 110000))
employees.append(Employee("Alex Veilleux", "123654789", 210000))
employees.append(Employee("Christian Veilleux", "123654987", 175500))
employees.append(Employee("Oliver Benning", "123987654", 115000))
employees.append(Employee("Diana Inkpen", "321456789", 222000))

def AddEmployees(name, socialNum, salary):
    if(name != "" and socialNum != "" and salary != ""):
        employees.append(Employee(name, socialNum, salary))
    else:
        print("Vous devez entrez au moins une des trois(3) valeurs demandées")

def CalculMoyenneTauxHoraire():
    j = len(employees)
    t_salary = 0
    m_salary = 0
    th_salary = 0
    print ("Récupération du salaire de chaque employé\n")
    for i in range(j):
        t_salary += employees[i].salary
    m_salary = (t_salary / j)
    th_salary = (m_salary / (50 * 40))
    print ("\nLe salaire moyen dans cette entreprise est de : \n", th_salary, "$/h")

def FindMyInfos(no):
    myhint = "no." + str(no)
    file = open("Employee.txt")
    lines = file.readlines()
    for line in lines:
       if myhint in line :
           print ("Found\n", line)
           break
    file.close()
           


    

    
        

    

        

        
