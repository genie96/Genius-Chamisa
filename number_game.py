def game():
	secret_num = random.randint(1, 10)
	guesses = []
	while len(guesses) < 5:
            try:
		guess = int(input("Guess a number between 1 and 10:"))
	    except ValueError:
)			print("You got it! My number was {}".format(secret_num))
		else:
			if guess == secret_num:
                            print("You got it! My number is {}".format(secret_num))
                            break
                        else:
                            print("That's not it!")
                        guesses.append(guess)    
 
