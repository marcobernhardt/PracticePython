
import random

exit = False 

while not exit:
    guess = int(input("Guess a random number! \n"))
    while guess < 1 or guess > 9:
        guess = int(input("Try again, guess a random number! \n"))
 
    rndm_nmbr = random.randint(1,9)

    if guess == rndm_nmbr:
        print(f"Nailed it! {guess} is the number!")
    else:
        difference = abs(guess-rndm_nmbr)
        print(f"Close! the number was {rndm_nmbr} you were {difference} away!")
    
    input_exit = input("Do you wanna exit?")
    
    if input_exit == "exit":
        exit = True
    else:
        continue
    
    
    