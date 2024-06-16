# Stanford-Code-in-Place-24

# Wordle Clone

This is my project for Stanford's Code in Place 24

The word list used in the project is taken from the following online site: https://wordsrated.com/tools/wordslists/5-letter-words-for-wordle/

It is a little console project based on my favorite word puzzle game, Wordle.
The rules for the puzzle is simple, the player has 5 turns to correctly guess a 5-letter word.
Game starts with an empty board (5x5 matrix of underscores) and a prompt to guess a word.
Once the player enters their guess, the program will update the board.
* Red means the alphabet doesn't exist in the solution.
* Yellow means the alphabet exist but in a different position.
* And green means the alphbet exists and in the same position.

These are meant as hints for the player to figure out the solution.
If player guesses the word correctly before 5 turns, it will be considered as win.
But failing to do so within 5 turns, will count as a loss.