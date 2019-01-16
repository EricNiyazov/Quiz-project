
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
q1chk = 0 #q1chk is 0 for now
q2chk = 0 #q2chk is 0 for now
q3chk = 0 #q3chk is 0 for now
q4chk = 0 #q4chk is 0 for now
q5chk = 0 #q5chk is 0 for now
q6chk = 0 #q6chk is 0 for now
q7chk = 0 #q7chk is 0 for now
q8chk = 0 #q8chk is 0 for now
q9chk = 0 #q9chk is 0 for now
q10chk = 0 #q10chk is 0 for now
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0

# question1 text
q1 = """
What's 9 + 10?
1. 19 
2. 21 
3. an old meme that was never funny 
4. 69420""" 
#question2 text
q2 = """
What is the meaning of life the universe and everything?
1. to live, love and be happy for as long as you can
2. to spread the human race to as far as we can and keep it alive
3. there is no meaning :(
4. 42""" 
#question3 text
q3 = """
If jon is moving at 1 km/hour and his home is 1 km away.
what's the square root of pi?
1. 1 hour
2. I am bad at math
3. 1.77245385091
4. 2"""
#question4 text
q4 = """
Can a match box?
1. I dunno
2. no but a tin can
3. yes light them up
4. there is no smoking in the ring"""
#question5 text
q5 = """
Are you going to give Eric N 10$?
1. yes, I will right now or I suck.
2. no, I will give 20$ or I suck.
3. no, I will give 50$ or I suck.
4. no, I will give 100$ right now or I suck."""
#question6 text
q6 = """
rewsnA siht noitseuq sdrawkcab?
1. wwhhhhhaaaaaaaaaaaaaatttttttttt
2. the program is broken
3. ko 
4. sure"""
#question7 text
q7 = """
If 2+2 is 4 and trains in new york are always late
what is the distance from earth to the sun?
1. 92.96 million mi
2. 92.97 million mi
3. 92.98 million km
4. 4 meters"""
#question8 text
q8 = """
What is the shape of the earth?
1. flat pancake
2. a donut
3. a sphere 
4. a spheroid"""
#question9 text
q9 = """
What point on earth has the least distance from space?
1. mount everest
2. mount k2
3. the sky
4. mount chimborazo"""
#question10 text
q10 = """
What is the best icecream flaver?
1. chocolate
2. vanilla
3. mint choclate chip
4. pineapple"""

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


