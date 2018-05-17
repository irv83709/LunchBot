###Lunch Bot 1.5
print("Welcome to the Lunch Bot version 1.5")
lunchPossible = ("Dave's", "Real Meal", "Chipotle", "Potbelly", "Andreas")
from random import *
print (sample((lunchPossible),3))
#Retry logic to run the lunch selection additional time or to exit program
retry = True
while(retry):
    tryAgain = input("Would you like me to try again?")  
    if(tryAgain in("no","No","NO","N","n")):
        retry = False
    elif(tryAgain in("Open the pod bay doors, HAL.")):
        print ("I'm sorry, Dave. I'm afraid I can't do that.")
        retry = False
    elif(tryAgain not in("yes","Yes","YES","Y","y","no","No","NO","N","n")):
        print ("I can't make heads or tails of that.")
    else:
        print (sample((lunchPossible),3))
print("Goodbye, enjoy your lunch!")

    




    



