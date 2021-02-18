# ---------------------------Intro to Programming----------------------------------

# MIT PS2

# Date : 2021-02-17

# Created by: Cyrus Gautam

# Tutor: Andrew Hamilton

#----------------------------------------------------------------------------------

# Text file
WORDLIST_FILENAME = 'words.txt'

import random
import string


# Load the file. Read the file and convert all the words in the textfile 
# into a list and print the number of words printed.
def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
    
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print('Loading wordlist from file...')
	inFile = open(WORDLIST_FILENAME, 'r')
	line = inFile.readline()
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist

#-------------------------------------------------------------------------------------------------------------------------

def choose_word(wordlist):
	"""
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
	return random.choice(wordlist)


# Calling the function puts its inner part/function in the assigned word. 
# For eg: the wordlist contains the list of all the words from the text file
# which we retirved from the load_words function.
wordlist = load_words()

#-------------------------------------------------------------------------------------------------------------------------

def is_word_guessed(secret_word, letters_guessed):
	'''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
	n = 0
	zero_one_list = []	
	secret_word_list = list(secret_word)
	# This will run until all the letters from the secret word is not covered.
	while n != len(secret_word):
		n += 1
		for i in range(0, len(secret_word)):
			# This line checks if the letters in secret word is present in letters
			# guessed or not. If they are, they then we add 0 to the zero_one_list. 
			# If they aren't we add 1.
			if secret_word_list[i] in letters_guessed:
				zero_one_list.append(0)
			else:
				zero_one_list.append(1)

	# This part of the code determines whether the the word is guessed or not. It is done
	# by looking at the added 0s and 1s from the previous part. If there is a single 1 in the 
	# zero_word_list, this means one of the letters has not been guessed, so it will return 
	# False to the questin "if the secret word is guessed?" and vice versa.
	if 1 in zero_one_list:
		return False
	else:
		return True

# print(is_word_guessed('ca', ['c', 'a', 't', 'e']))
#-------------------------------------------------------------------------------------------------------------------------

def get_guessed_word(secret_word, letters_guessed):
	'''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
	display = []
	# Iterates through secret word
	for i in secret_word:
		# Iterates through letters guessed. If the letters in secret word is in the letters 
		# guessed list, it adds the letter to the display list , if not, it add _ in the place
		# of the non-guessed letters.
		if i in letters_guessed:
			display.append(i)
		else:
			display.append('_')
	return ' '.join(display)


#-------------------------------------------------------------------------------------------------------------------------

def get_available_letters(letters_guessed):
	'''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
	allLetters = string.ascii_lowercase 		# all the alphabet in lowercase.
	remain = []									# list of the remaining alphabet

	# This part adds letters to the remain list if any alphabet hasn't been guessed
	# yet.
	for i in allLetters:
		if i not in letters_guessed:
			remain.append(i)
	return ' '.join(remain)

		

#-------------------------------------------------------------------------------------------------------------------------
	
def hangman(secret_word):
	'''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
	allLetters = string.ascii_lowercase				
	all_letter_guessed = []						# list for all the letters guessed
	correct_letter_list = []					# list for all the correct letters guessed
	vowels = 'aeiou'
	max_guess = 6								# total guesses available
	warnings = 3								# total warnings that can be given

	# This part is an introduction to the program. It prints out most of the rules of the
	# game and provides information about guesses and warnings.
	print('Welcome to the game Hangman!')
	print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long')
	print('You have 3 warnings left')
	print('You have ' +str(max_guess) + ' guesses to figure out the secret word')
	print('Available letters: ' + allLetters )
	print('-------------------------------------')

	# Start of the main program. This loop continues until you run out of guesses
	# or the word has been guessed.
	while max_guess > 0 and (is_word_guessed(secret_word, all_letter_guessed)==False):
		print('You have ' + str(max_guess) + ' guesses left')
		print('Available letters: ' + get_available_letters(all_letter_guessed))
		guess = input('Please guess a letter: ').lower() 	# input from user	

		# Checks if the guess is an alphabet or not.
		if guess in allLetters:					# If the guess is an alphabet.

			# Checks if the letters has already been guessed.
			if guess not in all_letter_guessed:	# If the letters has already been guessed.
				all_letter_guessed.append(guess)

				# This part checks if the secret contains the guessed letter or not.
				if guess in list(secret_word):	# If the secret word contains the guess
					correct_letter_list.append(guess)
					print('Good guess: ' + get_guessed_word(secret_word, correct_letter_list))
					print('-------------------------------------')
				else:							# If the secret word does not contain the guess.

					# Checks if the guess is a vowel or not. This is important because wrong vowel
					# guess decreases two guesses.
					if guess not in list(vowels):# If the guess is not a vowel
						max_guess -= 1
						print('Oops! the letter is not in my word. ')
						print(get_guessed_word(secret_word, correct_letter_list))
						print('-------------------------------------')
					else:						# If the guess is a vowel
						max_guess -= 2
						print('Oops! the letter is not in my word. ')
						print(get_guessed_word(secret_word, correct_letter_list))
						print('-------------------------------------')
			else:								# If the letters has already been guessed.

				# Checks if the warning is greater than 0 or not. This is important because after
				# three warning, the guesses will be decreased instead of warning.
				if warnings > 0:				# If number of warning is greater than 0
					warnings -= 1
					print('Oops! You have already guessed that letter.')
					print('You have ' + str(warnings) + ' warnings left')
					print(get_guessed_word(secret_word, correct_letter_list))
					print('-------------------------------------')
				else:							# If number of warning is equal to 0
					max_guess -= 1				
					print('Oops! You have already guessed that letter.')
					print("Since you don't have any warnings left, you have " + str(max_guess) + ' guesses remaining')
					print(get_guessed_word(secret_word, correct_letter_list))
					print('-------------------------------------')

		else:									# If the guess is not an alphabet.

			# If the guess is not an alphabet three warnings are given. After the three warnings 
			# the guesses start decreasing. This part checks if the warning is greater than 0 or not.
			if warnings > 0:					# If number of warning is greater than 0
				warnings -= 1 
				print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left')
				print(get_guessed_word(secret_word, correct_letter_list))
				print('-------------------------------------')
			else:								# If number of warning is equal to 0
				max_guess -= 1
				print('Oops! That is not a valid letter')
				print("Since you don't have any warnings left, you have " + str(max_guess) + ' guesses remaining')
				print(get_guessed_word(secret_word, correct_letter_list))
				print('-------------------------------------')

	# This part of the program decides wheather the user won or lost the game. If the user
	# run out of guesses than they lost. If they don't then according to our initial 
	# while loop all the letters in the secret word is guessed which means the user
	# wins.			
	if max_guess == 0:							# If there is no guesses left
		print('Oops! You ran out of guesses. You lost')
		print('The word was ' + (secret_word))
	else:										# If the user guessed all the letter in secret word
		print('Congrats! You successfully guessed the word. Hurray!!')
		print('Your total score is: ' + str(max_guess * len(correct_letter_list)))


#-------------------------------------------------------------------------------------------------------------------------

def match_with_gaps(my_word, other_word):
	'''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
	allLetters = string.ascii_lowercase
	check_list = []

	# This part checks if the length of the current guess of secret word
	# is equal to the regular English word.
	if len(my_word) == len(other_word):			# If the length is same.
		for i in range(len(my_word)):

			# This part looks for alphabets in my_word. Since, my_word, comprises of both
			# alphabet and _, it checks if letters in my_words are alphabet or not and then
			# carries out certain task. If the letter is not an alphabet, it just passes 
			# the letter and moves on to the next one.
			if my_word[i] in allLetters:		# If the letter in my_word is an alphabet

			# This parts checks wheather or not the alphabet found in a certain index of 
			# my_word is same as the alphabet found in the same index of the other_word.
			# If it is same, it adds 0 to the check list above, if not, it adds 1.
				if my_word[i] == other_word[i]:	# If the alphabets are same.
					check_list.append(0)
				else:							# If the alphabets are different
					check_list.append(1)
			else:								# If the letter in my_word is not an alphabet
				pass
	else:										# If the length is different
		return False

	# This part checks wheather all the alphabets in my_word and other_word are same with exact
	# same indexes. If the check_list contains a single 1, that means one of the alphabet is 
	# not same or the indexes are not same which means it is not a perfect match.
	if 1 in check_list:
		return False
	else:
		return True


#-------------------------------------------------------------------------------------------------------------------------

def show_possible_matches(my_word):
	'''
    my_word: string with _ characters, current guess of secret word
    returns: print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
	all_words = []
	# This function iterates through the wordlist and tries to find the exact same 
	# word that matches the patter of my_word. This is done by using the match_with_gaps
	# function.
	for j in wordlist:
		# print(i)
		if (match_with_gaps(my_word, j) == True):
			all_words.append(j)
		else:
			pass

	if len(all_words)> 0:
		return ", ".join(all_words)
	else:
		return 'No match found'


#-------------------------------------------------------------------------------------------------------------------------

	
def hangman_with_hints(secret_word):
	    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    '''
	allLetters = string.ascii_lowercase
	all_letter_guessed = []						# list for all the letters guessed
	correct_letter_list = []					# list for all the correct letters guessed
	vowels = 'aeiou'
	max_guess = 6								# total guesses available
	warnings = 3								# total warnings that can be given

	# This part is an introduction to the program. It prints out most of the rules of the
	# game and provides information about guesses and warnings.
	print('Welcome to the game Hangman!')
	print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long')
	print('You have 3 warnings left.')
	print('You have ' +str(max_guess) + ' guesses to figure out the secret word')
	print('Press * and enter to get hint on your guesses')
	print('Available letters: ' + allLetters )
	print('-------------------------------------')

	# Start of the main program. This loop continues until you run out of guesses
	# or the word has been guessed.
	while max_guess > 0 and (is_word_guessed(secret_word, all_letter_guessed)==False):
		print('You have ' + str(max_guess) + ' guesses left')
		print('Available letters: ' + get_available_letters(all_letter_guessed))
		guess = input('Please guess a letter: ').lower() 	# input from user	

		# Checks if the guess is an alphabet or not.
		if guess in allLetters:					# If the guess is an alphabet.

			# Checks if the letters has already been guessed.
			if guess not in all_letter_guessed:	# If the letters has already been guessed.
				all_letter_guessed.append(guess)

				# This part checks if the secret contains the guessed letter or not.
				if guess in list(secret_word):	# If the secret word contains the guess
					correct_letter_list.append(guess)
					print('Good guess: ' + get_guessed_word(secret_word, correct_letter_list))
					print('-------------------------------------')
				else:							# If the secret word does not contain the guess.

					# Checks if the guess is a vowel or not. This is important because wrong vowel
					# guess decreases two guesses.
					if guess not in list(vowels):# If the guess is not a vowel
						max_guess -= 1
						print('Oops! the letter is not in my word. ')
						print(get_guessed_word(secret_word, correct_letter_list))
						print('-------------------------------------')
					else:						# If the guess is a vowel
						max_guess -= 2
						print('Oops! the letter is not in my word. ')
						print(get_guessed_word(secret_word, correct_letter_list))
						print('-------------------------------------')
			else:								# If the letters has already been guessed.

				# Checks if the warning is greater than 0 or not. This is important because after
				# three warning, the guesses will be decreased instead of warning.
				if warnings > 0:				# If number of warning is greater than 0
					warnings -= 1
					print('Oops! You have already guessed that letter.')
					print('You have ' + str(warnings) + ' warnings left')
					print(get_guessed_word(secret_word, correct_letter_list))
					print('-------------------------------------')
				else:							# If number of warning is equal to 0
					max_guess -= 1				
					print('Oops! You have already guessed that letter.')
					print("Since you don't have any warnings left, you have " + str(max_guess) + ' guesses remaining')
					print(get_guessed_word(secret_word, correct_letter_list))
					print('-------------------------------------')

		# This part of the program provides hints to the user if they enter *. This was
		# done using the previous two function.
		elif guess == '*':
			print('Possible word matches are: ')
			print(show_possible_matches((get_guessed_word(secret_word, correct_letter_list)).replace(" ", '')))
			print('-------------------------------------')

		else:									# If the guess is not an alphabet.

			# If the guess is not an alphabet three warnings are given. After the three warnings 
			# the guesses start decreasing. This part checks if the warning is greater than 0 or not.
			if warnings > 0:					# If number of warning is greater than 0
				warnings -= 1 
				print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left')
				print(get_guessed_word(secret_word, correct_letter_list))
				print('-------------------------------------')
			else:								# If number of warning is equal to 0
				max_guess -= 1
				print('Oops! That is not a valid letter')
				print("Since you don't have any warnings left, you have " + str(max_guess) + ' guesses remaining')
				print(get_guessed_word(secret_word, correct_letter_list))
				print('-------------------------------------')

	# This part of the program decides wheather the user won or lost the game. If the user
	# run out of guesses than they lost. If they don't then according to our initial 
	# while loop all the letters in the secret word is guessed which means the user
	# wins.			
	if max_guess == 0:							# If there is no guesses left
		print('Oops! You ran out of guesses. You lost')
		print('The word was ' + (secret_word))
	else:										# If the user guessed all the letter in secret word
		print('Congrats! You successfully guessed the word. Hurray!!')
		print('Your total score is: ' + str(max_guess * len(correct_letter_list)))


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

