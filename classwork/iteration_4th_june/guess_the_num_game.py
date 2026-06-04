#program for guess the number game:
#initialize constants:
secret_num = 7
guess_num = 0
#-------------------------------------------
#iteration begins:
while(guess_num != secret_num):
    guess_num = int(input("Guess the Number:"))
    #if the guess is correct:
    if(guess_num == secret_num):
        print("Congratulations! You guessed the correct number.")
    #---------------------------------------    
    else:
        print("Wrong Guess. Try Again.\n")
#-------------------------------------------
#-------------------------------------------
