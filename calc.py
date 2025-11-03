import time
print ("======================")
print ("Welcome to the GPA calculator")
print ("Please enter your first semester classes first, followed by your second semseter classes")
print ("======================")
Grades_List = []
Classes_Num_Valid = False
while Classes_Num_Valid == False: #Gets all the information from the user
    try: 
        Classes_Num = int(input (f"How many classes would you like to input? (enter a digit): " ))
        Sem1_Classes_Num = int(input (f"How many classes did you take first semester? (enter a digit): " ))
        Sem2_Classes_Num = int(input (f"How many classes did you take second semester? (enter a digit): " ))
        if Sem1_Classes_Num + Sem2_Classes_Num == Classes_Num: #Checks if sem1 and sem2 GPA add up to total
            Classes_Num_Valid = True #Exits the loop if both checks pass
        else:
            print("Your semster 1 and 2 classes dont add up to your total!")
    except ValueError:
        print ("That is not a valid digit!")
        continue #Restarts the loop if invalid input
if Classes_Num == 0: #Exits program if user enters zero
    print ("Looks like you dont have ANY classes! Why are you even here???")
    exit()
for i in range(Classes_Num): #Loops over everyclass the user is taking and asks for their grade in it
    Class_Grade_Valid = False #Staging variable
    while Class_Grade_Valid == False:
        try: #Input validation
            Class_Grade = float(input (f"Enter grade {i+1} (0.0-4.0): "))
            if 0 <= Class_Grade <= 4:
                Class_Grade_Valid = True
            else:
                print ("That is not between 0.0 and 4.0!")
                continue 
        except ValueError:
            print ("That is not a valid grade!")
            continue
        Grades_List.append (round(Class_Grade,1)) #Adds the grade the user entered to a list with all the grades on it
Semester_Desired_Correct = False #Staging Variable

if Sem1_Classes_Num == 0: #Checks if Semester 1 is empty
    print ("Analyzing semster 2 since 1 is empty")
    Semester_Desired_Correct = True
    Semester_Desired = 2
if Sem2_Classes_Num == 0: #Checks if Semseter 2 is empty
    print ("Analyzing semster 1 since 2 is empty")
    Semester_Desired_Correct = True
    Semester_Desired = 1
while Semester_Desired_Correct == False: #If both semester 1 and 2 have classes, asks the user which semester to analyze
    Semester_Desired = input("Which semster would you like to analyze (1 or 2): ")
    if Semester_Desired == "1" or Semester_Desired == "2":
        Semester_Desired_Correct = True
    else: #Input validation
        print ("That is not 1 or 2!")
print()
print("Calculating...")
print()
GPA_Overall = round(sum(Grades_List)/len(Grades_List),1) #Calculates average GPA of the entire list
if Sem1_Classes_Num != 0:
    GPA_First = round(sum(Grades_List[:Sem1_Classes_Num])/len(Grades_List[:Sem1_Classes_Num]),1) #Calculates the average GPA of first semester
if Sem2_Classes_Num != 0:
    GPA_Second = round(sum(Grades_List[Sem1_Classes_Num:])/len(Grades_List[Sem1_Classes_Num:]),1) #Calculates the average GPA of second semster
time.sleep (1)
print ("================================")
print (f"Your overall GPA is {GPA_Overall} ")
if Semester_Desired == "1": #Checks if sem1 gpa is higher than overall AND sem1 is desired to analyze 
    print (f"Your semester 1 GPA is {GPA_First} ")
    if GPA_First > GPA_Overall:
        print ("Your first semster GPA is greater than your overall")
    if GPA_First == GPA_Overall:
        print ("Your first semster GPA is equal to your overall")
    if GPA_First < GPA_Overall:
        print ("Your first semster GPA is lower than your overall")
if Semester_Desired == "2":  #Checks if sem2 gpa is higher than overall AND sem2 is desired to analyze 
    print (f"Your semester 2 GPA is {GPA_Second} ")
    if GPA_Second > GPA_Overall:
        print ("Your second GPA is greater than your overall")
    if GPA_Second == GPA_Overall:
        print ("Your second GPA is equal to your overall")
    if GPA_Second < GPA_Overall:
        print ("Your second GPA is lower than your overall")
if Sem2_Classes_Num != 0 and Sem1_Classes_Num != 0:
    if GPA_First > GPA_Second: #Says which semster gpa is better if both have classes in them
        print("Your first semster GPA is higher than second")
    elif GPA_First == GPA_Second:
        print ("Your first and second semster GPA are the same")
    elif GPA_First < GPA_Second:
        print ("Your first semester GPA is lower than your second")
print ("================================")
Do_Goal_Valid = False #Staging variable
while Do_Goal_Valid == False:
    Do_Goal = input ("Would you like to analyze your goal GPA? (y/n)") 
    if Do_Goal in ("y", "n", "Y", "N"): #Input validation
        Do_Goal_Valid = True
    else:
        print ("Invalid input")
if Do_Goal == "y" or Do_Goal == "Y":
    Goal_GPA_Valid = False #Staging variable
    Goal_Avaiable = False #Checks if the goal GPA is reachable by only changing one grade
    while Goal_GPA_Valid == False:
        try: #Input validation
            Goal_GPA = float(input ("Enter your goal GPA (0.0-4.0): "))
            if 0 <= Goal_GPA <= 4:
                Goal_GPA_Valid = True
            else:
                print ("That is not between 0.0 and 4.0!")
        except ValueError:
            print ("That is not a valid GPA!")
    if Sem2_Classes_Num == 0 or Sem1_Classes_Num == 0: #If one semester is empty it will just analyze as normal
        Iterate = 0 #For printing which class is curently analyzed, this is superfulous
        #TODO: replace {iterate} in the print command with {i+1}
        for i in Grades_List:
            Iterate += 1
            GPA_Overall_Test = round((sum(Grades_List)+4-i)/len(Grades_List),1) #Calculate the GPA when removing a class and replacing it with 4
            if GPA_Overall_Test >= Goal_GPA: #If replacing the grade got the GPA to the goal
                print (f"To reach a GPA of {Goal_GPA}, you need to get at least a 4.0 in class {Iterate}") #Display info
                Goal_Avaiable = True
    else:
        print ("Since semester 1 is already completed, analyzing semester 2 grades needed to reach goal GPA")
        Iterate = Sem1_Classes_Num #Same as for the the other option, not easily removeable though
        for i in Grades_List[Sem1_Classes_Num:]:
            Iterate += 1
            GPA_Overall_Test = round((sum(Grades_List)+4-i)/len(Grades_List),1) #Calculate the GPA when removing a class and replacing it with 4
            if GPA_Overall_Test >= Goal_GPA: #If replacing the grade got the GPA to the goal
                print (f"To reach a GPA of {Goal_GPA}, you need to get at least a 4.0 in class {Iterate}")
                Goal_Avaiable = True
    if Goal_Avaiable == False:
        print ("It is not possible to reach your goal GPA by only changing one class.")
else:
    print ("GOODBYE!")
    exit()
