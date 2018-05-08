###Lunch Bot 1.4
print("Welcome to the Lunch Bot version 1.4")
lunchPossible = ("Dave's", "Real Meal", "Chipotle", "Potbelly", "Andreas")
from random import *
def lunch():
    option1=choice (lunchPossible)
    option2=choice (lunchPossible)
    option3=choice (lunchPossible)
    return option1+"\n"+option2+"\n"+option3
print(lunch())
tryAgain = input("Would you like me to try again?")
while(tryAgain in ("yes","Yes","YES","Y","y","no","No","NO","N","n")):
    if(tryAgain in ("yes","Yes","YES","Y","y")):
        print(lunch())
    if(tryAgain in("no","No","NO","N","n")):
        print("Goodbye, enjoy your lunch!")
        exit()
else:
    print ("I can't make heads or tails of that.")
    tryAgain = input("Would you like me to try again?")
    print(lunch())




    



