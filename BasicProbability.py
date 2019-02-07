import math
import random

print("Welcome to the guessing game!\n")


print("The following Program picks a number between 1 and 101. It then tries to guess the number that was picked and keeps track of how many guesses it took to guess it correctly. \
The program is run 1000 times and the average probability of guessing a number between 1 and 101 correctly is calculated based on these 1000 run. \
It is compared to what the actual probabiliy should be and a percent error is calculated \n")
x= random.randint(1,101)
y=0
counter=0
number_looped=0
Boolean=True
number_guess=[]


while Boolean:
    y=random.randint(1,101)
    counter+=1
    if x==y and number_looped<1001:
        number_guess.append(counter)
        counter=0
        number_looped+=1
    if x==y and number_looped==1001:
        Boolean=False


total_prob=(sum(number_guess)/(101*1000))

print("Based on 1000 runs of the simulation the probabiliy was" + str(total_prob) + "%" + " and it should have been " + str((1/101)*100) +"%\n")
print("The percent error was " + str(abs(((1/101)*100)-total_prob)/((1/101)*100)*100)+ "%")
