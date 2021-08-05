import random
from time import sleep


class Hangman:
    """
    In the constructor, first choose a word and declare the needed starting variables.
    Then, run the game, print the number of letters in the word and ask the user to guess
    If the guessed letter is valid and isn't wrong, reveal the word and check if the word has been completed
    If the guessed letter is valid but is wrong, increment the number of rows shown and add it to their list of used letters.

    This is a simple hangman game you can run in your terminal.
    Feel free to change the number of lives a player can have by editing the art in the 'hangman_art' text file. Lives are determined by the number of rows in the art.
    Feel free to edit the pool of random words and phrases that will be used in the game through the 'hangman_words' text file.
    """

    def __init__(self):
        # Choosing a Random Word
        with open("hangman_words.txt", "r") as f:
            file_content = f.readlines()
            random_line = random.randint(0, len(file_content) - 1)
            self.random_word = file_content[random_line].lower()
       
    
        self.random_word = list(self.random_word.rstrip("\n")) # Converting word to a list of letters
        self.list_of_letters = [] # A list of lists that contains the letters and status of those letters. Whether they've been guessed or not
        
        # Converting list of letters into a list of lists
        for letter in self.random_word:
            if letter == " ":
                self.list_of_letters.append(letter)
            else:
                self.list_of_letters.append([letter, False])

        self.used_letters = []
        self.wrong_letter_count = 0
    
    # Checks if the player's guess is correct
    def check_letter(self, letter):

        sleep(1.5)
        
        # If the letter is in the word
        # Loop through the list of letters and set their guessed boolean to True
        if letter in self.random_word:
            for key, character in enumerate(self.list_of_letters):
                if character[0] == letter:
                    self.list_of_letters[key][1] = True
            print("Correct!")
        
        # If the letter is not in the word
        # Append the letter to the list of used letters
        # Increment the wrong letter count
        else:
            self.used_letters.append(letter)
            self.wrong_letter_count += 1
            print("Oops, that's wrong!")
        print(f"Wrong and Used Letters: {', '.join(self.used_letters)}")
    
    # Prints out the necessary information such as the hangman, used letters and letters of the word
    def print_word(self):
        # For every list in the list of letters
        # If the list is not a list but a string with a space in it
        # Print a space on the same line and continue the loop
        # If the list's status is unguessed, print an underscore 
        # Else if the list's status is guessed, print the actual letter
        print("The word is: ", end="")
        for key, character in enumerate(self.list_of_letters):
            if character == " ":
                print(" ", end=" ")
                continue
            
            elif character[1] is False:
                print("_", end=" ")
            else:
                print(character[0], end=" ")
                
        print("")
        
        # Printing out the hangman
        print("HANGMAN STATUS")

        # First open the file, and read it
        # For every row in the file
        # If the player hasn't gotten any letters wrong, tell them they're in the clear
        # If the current line being read is less than the player's wrong letter count, print that row of a dead man
        with open("hangman_art.txt", "r") as f:
            content = f.readlines()
            for key, row in enumerate(content):
                if self.wrong_letter_count == 0:
                    print("Hangman is currently in the clear so far")
                    break
                elif key < self.wrong_letter_count:
                    print(row.rstrip("\n"))
        print("")

    # Gets the user's guess
    def get_input(self):
        # Get the user's guest
        # If the number of characters in the guess is equal to one
        # Check the user's guess by calling the valid function
        # If the number of characters in the guess is more than one, tell them to guess again
        user_guess = input("What is your guess?  ")
        if len(user_guess) == 1:
            self.check_letter(user_guess)
        elif len(user_guess) > 1:
            print("Only one character at a time. Guess again.")
            return None
    
    # Checks if the user has completed the whole word
    def check_win(self):
        # For every list in the list of letters
        # If the letters is a string with a space in it, continue the loop
        # If any of the letters at all are unguessed, return False
        # If all the letters are guessed and the rest are just spaces, return True. The player won
        for letter in self.list_of_letters:
            if letter == " ":
                continue

            elif letter[1] is False:
                return False
        return True
    
    # Checks if the user has lost.
    def check_lose(self):
        # First open the hangman art file and read the content
        # If the wrong letter count is greater than or equal to the number of rows in the text file, return True. The player has lost
        # Else, return False, the player has not lost
        with open("hangman_art.txt", "r") as f:
            file_content = f.readlines()
            if self.wrong_letter_count >= len(file_content):
                return True
        return False
    
    # Game Loop
    def run(self):
        self.print_word() 
        # While the player hasn't lost or won, get their guess and print the necessary information
        while not self.check_win() and not self.check_lose():
            self.get_input()

            sleep(1.5)

            self.print_word()

            sleep(1.5)

        # Determining if the player won or lost
        if self.check_win():
            print(f"You won!! The word was {''.join(self.random_word)}.")
        elif self.check_lose():
            print("Unfortunately, you've ran out of lives. You killed the man.")
            print(f"FYI, the word was {''.join(self.random_word)}.")



if __name__ == "__main__":
    game = Hangman()
    game.run()
