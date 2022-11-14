print("Welcome to question game...")

lstring = """
there is 5 questions you need to answered and every question has a point for it """

print("Here are our rules "+ lstring )

descion = input("would you like to begin the game? ").lower()

if descion != "yes":
    quit()


score=0


#first question
answer =  input("what is the captal of France? ").lower()
if answer == "paris":
    print("correct")
    score+=1
else:
    print("incorrect") 




#second question
answer =  input("what is the captal of Germany? ").lower()
if answer == "berlien":
    print("correct")
    score+=1
else:
    print("incorrect") 



#third question
answer =  input("what RAM stands for? ").lower()
if answer == "random access memory":
    print("correct")
    score+=1
else:
    print("incorrect") 



#fourth question
answer =  input("what PSU stands for? ").lower()
if answer == "power supply":
    print("correct")
    score+=1
else:
    print("incorrect") 


#fifth question
answer =  input("what CPU stands for? ").lower()
if answer == "computer processing unit":
    print("correct")
    score+=1
else:
    print("incorrect") 



print("you finished the game and you got " + str(score) )
print("you finished the game and you got " + str((score/5)*100 ) +"%")
