
global grade
grade = 0 # grade is 0
a1 = 0
a2 = 0

def ask_and_check(qText, qChk, aUser, aCorr):
    print(qText) #print question1

    while qChk == 0: #while test is false run loop
        try:
            aUser = int(input(">>"))#answer one equal an integer input
            if aUser == aCorr:# if answer 1 equal 1
                print ("Ok I got it")#tell user ok answer
                global grade
                grade += 1#change grade by one
                qChk = 1#escape condish
            elif 4 >= aUser >= 1:
                print("Ok I got it")#tell user ok answer
                qChk = -1 #escape condish
            elif aUser > 4: #if answer more then 4
                print ("no answers more then 4 duh") # tell user no answer more then 4
            else:
                print ("no answers less then 1 duh") #tell user no answer less then 1
        except ValueError: #if ValueError
            print("answer must be a integer 1,2,3 or 4")   #tell user it must be int
from Quiz_questions import *


ask_and_check(q1, q1chk, a1, 1)
ask_and_check(q2, q2chk, a2, 4)
ask_and_check(q3, q3chk, a3, 3)
ask_and_check(q4, q4chk, a4, 2)
ask_and_check(q5, q5chk, a5, 4)
ask_and_check(q6, q6chk, a6, 3)
ask_and_check(q7, q7chk, a7, 1)
ask_and_check(q8, q8chk, a8, 4)
ask_and_check(q9, q9chk, a9, 4)
ask_and_check(q10, q10chk, a10, 1)


print("your grade is",grade,"/ 10") #print the grade
if grade == 10:
    print ("you did it perfect")
elif grade == 9:
    print ("almost perfect oof 9/10")
elif grade == 8:
    print ("ok 8/10 very normal")
elif 7 >= grade >= 6:
    print ("ok, ok try a little harder")
elif  5 >= grade >= 1:
    print ("what a fail go try again")
elif grade == 0:
    print ("FFS try guessing next time you will get a better score")


