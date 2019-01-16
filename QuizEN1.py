q1chk = 0 #test is false for now
q2chk = 0
grade = 0 # grade is 0
a1 = 0
a2 = 0

q1 = """
What's 9 + 10?
1. 19 
2. 21 
3. an old meme that was never funny 
4. 69420"""

q2 = """
What is the meaning of life the universe and everything?
1. to live, love and be happy for as long as you can
2. to spread the human race to as far as we can and keep it alive
3. there is no meaning :(
4. 42"""

print (q1)
while q1chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 1:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q1chk = 1#escape condish
        elif 4 >= a1 > 1:
            print("Ok I got it")#tell user ok answer
            q1chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int

print (q2)
while q2chk == 0: #while test is false run loop
    try:
        a2 = int(input(" "))#answer one equal an integer input
        if a2 == 4:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q2chk = 1#escape condish
        elif 4 >= a2 > 1:
            print("Ok I got it")#tell user ok answer
            q2chk = -1 #escape condish
        elif a2 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int

print("your grade is",grade,) #print the grade
