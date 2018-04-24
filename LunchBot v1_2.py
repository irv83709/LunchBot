###Lunch Bot 1.2
print("Welcome to the Lunch Bot version 1.0")
lunchPossible = ("Dave's", "Real Meal", "Chipotle", "Potbelly", "Andreas")
from random import *
def lunch():
    option1=choice (lunchPossible)
    option2=choice (lunchPossible)
    option3=choice (lunchPossible)
    return option1+"\n"+option2+"\n"+option3
print(lunch())
tryAgain = input("Would you like me to try again?")
while(tryAgain in ("yes","Yes","YES","Y","y")):
    print(lunch())
    tryAgain = input("Do you want try again?")
print("Goodbye, enjoy your lunch!")
