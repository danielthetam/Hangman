# Hangman

Libraries Used
- Time(used the sleep function to pace the game)
- Random(used to choose a random line/word/phrase from the 'hangman_words.txt' file)

DESCRIPTION
- This is a simple hangman game made with Python you can run in your terminal.

NOTES
- The 'hangman_words.txt' file contains a list of words and phrases that will be chosen at random by the program
- The 'hangman_art.txt' file contains ASCII art of the complete hangman. 
  For each letter the player gets wrong, it increases the number of rows that will be printed from the ASCII art.
  Once all the rows have been printed, meaning the ASCII art is complete, the game will end.
  Lives are determined by the number of rows in the art.
- Feel free to change the number of lives a player can have by editing the art in the 'hangman_art' text file. 
- Feel free to edit the pool of random words and phrases that will be used in the game through the 'hangman_words' text file.
