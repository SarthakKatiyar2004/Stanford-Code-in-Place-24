from word_list import wordlist
import random

placeholder = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
answer = random.choice(wordlist).upper()

def printPlaceholder():
	for i in range (5):
		for j in range(5):
			print(placeholder[i][j], end = " ")
		print("")
    
def takeInput():
	guess = input("\nGuess the word: ").upper()
	while len(guess) != 5:
		print("\nThe word should not exceed 5 characters!")
		guess = input("\nGuess again: ")
	return str(guess)
 
def updatePlaceholder(guess, row):
	for i in range(5):
		if (guess[i] not in answer):
			placeholder[row][i] = '\033[31m'+guess[i]+'\033[0m'
		else:
			if (guess[i] == answer[i]):
				placeholder[row][i] = '\033[32m'+guess[i]+'\033[0m'
			else:
				placeholder[row][i] = '\033[93m'+guess[i]+'\033[0m'

def main():
	i = 0
	printPlaceholder()
	while i < 5:
		guess = takeInput()
		updatePlaceholder(guess, i)

		if (guess == answer):
			printPlaceholder()
			print("\nYay you won!")
			break

		printPlaceholder()
		i += 1
	    	
	if i == 5:
		print("\nBetter luck next time! The word was: ",answer)
    	
    	
if __name__ == "__main__":
    main()