q1chk = 0 #test is false for now
q2chk = 0
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
                #grade += 1#change grade by one
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

ask_and_check(q1, q1chk, a1, 1)
ask_and_check(q2, q2chk, a2, 4)

