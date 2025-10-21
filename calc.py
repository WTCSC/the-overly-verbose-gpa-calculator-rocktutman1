import time
print ("======================")
print ("Welcome to the GPA calculator")
print ("Please enter your first semester classes first, followed by your second semseter classes")
print ("======================")
Grades_List = []
Classes_Num_Valid = False
while Classes_Num_Valid == False:
    try: 
        Classes_Num = int(input (f"How many classes would you like to input? (enter a digit): " ))
        Sem1_Classes_Num = int(input (f"How many classes did you take first semester? (enter a digit): " ))
        Sem2_Classes_Num = int(input (f"How many classes did you take second semester? (enter a digit): " ))
        if Sem1_Classes_Num + Sem2_Classes_Num == Classes_Num:
            Classes_Num_Valid = True
        else:
            print("Your semster 1 and 2 classes dont add up to your total!")
    except ValueError:
        print ("That is not a valid digit!")
        continue
if Classes_Num == 0:
    print ("Looks like you dont have ANY classes! Why are you even here???")
    exit()
for i in range(Classes_Num):
    Class_Grade_Valid = False
    while Class_Grade_Valid == False:
        try: 
            Class_Grade = float(input (f"Enter grade {i+1} (0.0-4.0): "))
            if 0 <= Class_Grade <= 4:
                Class_Grade_Valid = True
            else:
                print ("That is not between 0.0 and 4.0!")
                continue
        except ValueError:
            print ("That is not a valid grade!")
            continue
        Grades_List.append (round(Class_Grade,1))
Semester_Desired_Correct = False

if Sem1_Classes_Num == 0:
    print ("Analyzing semster 2 since 1 is empty")
    Semester_Desired_Correct = True
    Semester_Desired = 2
if Sem2_Classes_Num == 0:
    print ("Analyzing semster 1 since 2 is empty")
    Semester_Desired_Correct = True
    Semester_Desired = 1
while Semester_Desired_Correct == False:
    Semester_Desired = input("Which semster would you like to analyze (1 or 2): ")
    if Semester_Desired == "1" or Semester_Desired == "2":
        Semester_Desired_Correct = True
    else:
        print ("That is not 1 or 2!")
print()
print("Calculating...")
print()
GPA_Overall = round(sum(Grades_List)/len(Grades_List),1)
if Sem1_Classes_Num != 0:
    GPA_First = round(sum(Grades_List[:Sem1_Classes_Num])/len(Grades_List[:Sem1_Classes_Num]),1)
if Sem2_Classes_Num != 0:
    GPA_Second = round(sum(Grades_List[Sem1_Classes_Num:])/len(Grades_List[Sem1_Classes_Num:]),1)
time.sleep (1)
print ("================================")
print (f"Your overall GPA is {GPA_Overall} ")
if Semester_Desired == "1":
    print (f"Your semester 1 GPA is {GPA_First} ")
    if GPA_First > GPA_Overall:
        print ("Your first semster GPA is greater than your overall")
    if GPA_First == GPA_Overall:
        print ("Your first semster GPA is equal to your overall")
    if GPA_First < GPA_Overall:
        print ("Your first semster GPA is lower than your overall")
if Semester_Desired == "2":
    print (f"Your semester 2 GPA is {GPA_Second} ")
    if GPA_Second > GPA_Overall:
        print ("Your second GPA is greater than your overall")
    if GPA_Second == GPA_Overall:
        print ("Your second GPA is equal to your overall")
    if GPA_Second < GPA_Overall:
        print ("Your second GPA is lower than your overall")
if Sem2_Classes_Num != 0 and Sem1_Classes_Num != 0:
    if GPA_First > GPA_Second:
        print("Your first semster GPA is higher than second")
    elif GPA_First == GPA_Second:
        print ("Your first and second semster GPA are the same")
    elif GPA_First < GPA_Second:
        print ("Your first semester GPA is lower than your second")
print ("================================")
Do_Goal_Valid = False
while Do_Goal_Valid == False:
    Do_Goal = input ("Would you like to analyze your goal GPA? (y/n)")
    if Do_Goal in ("y", "n", "Y", "N"):
        Do_Goal_Valid = True
    else:
        print ("Invalid input")
if Do_Goal == "y" or Do_Goal == "Y":
    Goal_GPA_Valid = False
    Goal_Avaiable = False
    while Goal_GPA_Valid == False:
        try:
            Goal_GPA = float(input ("Enter your goal GPA (0.0-4.0): "))
            if 0 <= Goal_GPA <= 4:
                Goal_GPA_Valid = True
            else:
                print ("That is not between 0.0 and 4.0!")
        except ValueError:
            print ("That is not a valid GPA!")
    if Sem2_Classes_Num == 0 or Sem1_Classes_Num == 0:
        Iterate = 0
        for i in Grades_List:
            Iterate += 1
            GPA_Overall_Test = round((sum(Grades_List)+4-i)/len(Grades_List),1)
            if GPA_Overall_Test >= Goal_GPA:
                print (f"To reach a GPA of {Goal_GPA}, you need to get at least a 4.0 in class {Iterate}")
                Goal_Avaiable = True
    else:
        print ("Since semester 1 is already completed, analyzing semester 2 grades needed to reach goal GPA")
        Iterate = Sem1_Classes_Num
        for i in Grades_List[Sem1_Classes_Num:]:
            Iterate += 1
            GPA_Overall_Test = round((sum(Grades_List)+4-i)/len(Grades_List),1)
            if GPA_Overall_Test >= Goal_GPA:
                print (f"To reach a GPA of {Goal_GPA}, you need to get at least a 4.0 in class {Iterate}")
                Goal_Avaiable = True
    if Goal_Avaiable == False:
        print ("It is not possible to reach your goal GPA by only changing one class.")
else:
    print ("GOODBYE!")
    exit()
