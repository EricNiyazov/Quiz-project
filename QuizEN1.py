test = False #test is false for now
q1 = print("what's 9 + 10") #print question
grade = 0 # grade is 0
print(" ")
print("1. 19 ")
print("2. 21 ")
print("3. an old meme that was never funny ") #print the questions
print("4. 69420 ")

while test == False: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 1:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            test = True#escape condish
        elif 4 >= a1 > 1:
            print("Ok I got it")#tell user ok answer
            test = True #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int
print("your grade is",grade,) #print the grade
