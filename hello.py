import random



print("hello, welcome to our guessing game")
answer = random.randint(1,10)

guess_taken = 0
def get_guess():
    while True:
        try:
            guess = input("Enter a guess: ")
            int_guess=int(guess)
            return int_guess
        except:
            print("That's not a number. Try again")            
guesses=[]
while guess_taken < 3:
    int_guess=get_guess()

    guesses.append(int_guess)
    
    # print(guesses)
    guess_taken = guess_taken+1
    if int_guess == answer:
        print("You guessed correctly")
        break
    elif int_guess > answer:
        print("You guessed too high")
    else:
        print("You guessed to low")

    print("You have taken {} guesses".format(guess_taken))
    print("You have taken" + guess_taken)
    print("You have guessed:{}".format(guesses))
print("end of program")