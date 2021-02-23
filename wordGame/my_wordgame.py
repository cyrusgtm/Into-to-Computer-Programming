# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by:  Cyrus Raj Gautam
#
# Name          : Cyrus Raj Gautam
# Collaborators : None
# Time spent    : 10+ hours

import math
import random
import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
handSize = 7


scrabbleLetterValue = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

wordlistFilename = 'words.txt'

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print('Loading word list from file')
    # inFile: file
    inFile = open(wordlistFilename, 'r')
    #wordlist: list of strings
    wordlist = []
    for line in inFile:
    	wordlist.append(line.strip().lower())
    print(' ', len(wordlist), 'words loaded.')
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
    	freq[x] = freq.get(x,0) + 1
    return freq



def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    scrabbleValues = []
    # checking if the words contains '*' or not. Since the point system
    # acts differently when we make a sentence using *, we have to make two
    # different cases for these.
    for i in word.lower():
        if i != '*':
            scrabbleValues.append(scrabbleLetterValue[i])
        else:
            pass

    # Our point system.
    if (7*len(word) - 3*(n-len(word))) < 1:
    	return 1 * sum(scrabbleValues)
    else:
    	return sum(scrabbleValues) * (7*len(word) - 3*(n-len(word)))



def display_hand(hand):
	"""
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

	allLetters = []
	for key in hand:                          # Loops through the key of dictionary
		allLetters.append(key * hand[key])    # multiplies the string to match its number
		combineLetters = "".join(allLetters)  # it combines all the string from above

    # we use two join because, the allLetters list after appending all the letter 
    # will look like [a bb c ddd e], therefore we need to remove all the gap first
    # between letters and then seperate each letter. If we only use one join the letters
    # will be seperated in groups. 
	return " ".join(combineLetters)

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand = {}
    # setting the celing for how many vowels should be there in our hand.
    num_vowels = int(math.ceil(n / 3))

    # Adding vowels in our hand
    for i in range(num_vowels - 1):     
        x = random.choice(vowels)       # choosing random vowels to add in the hand.
        hand[x] = hand.get(x, 0) + 1    # calculating the total no of vowels.
    
    # Adding consonants in our hand
    for i in range(num_vowels, n):    
        x = random.choice(consonants)   # choosing random consonants to add in the hand.
        hand[x] = hand.get(x, 0) + 1    # calculating the total no of that specific consonants.


    hand['*'] = 1                       # this line adds * to our hand.
    return hand




def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # making a new copy of my original hand, so that my original hand stays
    # intact.
    newHand = hand.copy()
    for i in word.lower():
        if i in newHand:
            # if the word contains letter from the hand then we decrease the number of that
            # letter in the hand
            newHand[i] -= 1
            # If the number of the letter in the new hand reaches 0, then we completely delete
            # the letter
            if newHand[i] == 0:
                del newHand[i]
    return newHand




# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    test = []
    # making a new copy of my original word, so that my original word stays
    # intact.
    newWord = word.lower()
    # if * is not present in our newWord
    if '*' not in newWord:
        for i in range(len(newWord)):
            # if my hand contains letters from my newWord and number of that letter 
            # in the hand is greater than or equal to its number in the newWord and
            # if the newWord is in my wordlist then it will add 1 to the test list. 
            if newWord[i] in hand and hand[newWord[i]] >= newWord.count(newWord[i]) and newWord in word_list:
                test.append(1)
            else:
                pass
        # Since the above iteration runs for every letter in newWord, that means 
        # the length of newWord should be same as the test list. This is done in order
        # to safe from missing letters that are present twice or more in the same word. 
        if sum(test) == len(newWord):
            return True
        else:
            return False

    # if * is present in our newWord            
    elif '*' in newWord:
        for i in range(len(vowels)):
            # replacing * with almost all vowels and if the word formed after replacing *
            # is in wordlist then it goes throught the iteration else it passes.
            if newWord.replace('*', vowels[i]) in word_list:
                for j in range(len(newWord)):
                    # if the letters from my newWord is in the hand and the number of 
                    # that letter in the hand is greater or equal to its number in the
                    # newWord then it will add 1 to the list else it will pass.
                    if newWord[j] in hand and hand[newWord[j]] >= newWord.count(newWord[j]):
                        test.append(1)
                    else:
                        pass
                # Similar to above if the length of the newWord matches the length of our
                # test than return True else return False.
                if sum(test) == len(newWord):
                    return True
                else:
                    return False
            else:
                pass

        if sum(test) != len(newWord):
            return False



# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for i in hand.values():
        count += i
    return count

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    
    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    totalScore = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand):
        # Display the hand
        print("Current Hand: ", display_hand(hand))
        
        # Asking the user for input
        word = input("Enter word, or \"!!\" to indicate that you are finished: ")
        # If the input is two exclamation points, stop the game. The game is over
        if word == "!!":
            print('The game is over, you have earned ' + str(totalScore) + ' points')
            break
            
        # If the word is valid, display the points and their total score.
        elif is_valid_word(word, hand, word_list):
            score = get_word_score(word, calculate_handlen(hand))
            totalScore += score
            print("\"{}\" earned".format(word), score, "points.", "Total:", totalScore, "points")
        
        # If the word is invalid, say the word is not valide and remove those letters 
        # from your hand to display a new hand.
        else:
            print("That is not a valid word. Please choose another word.")
        hand = update_hand(hand, word)    # Updating new hand by removing the invalid word letters.
        print()

    # If the user runs out of letters in the hand. 
    if not calculate_handlen(hand):
        print(" Ran out of letters. Total score for this hand: " + str(totalScore) + " points")
    
    
    # Return the total score as result of function
    return totalScore




def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.
    If user provide a letter not in the hand, the hand should be the same.
    Has no side effects: does not mutate hand.
    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # new copy of our original hand.
    newHand = hand.copy()
    if letter in newHand:
        # Calculates the value of letter present in the hand
        num = newHand[letter]
        # the letters that can be substituted. At the beginning everyletter has a 
        # chance to be substituted.
        availableSubs = string.ascii_lowercase

        # This iteration removes the letters from the available Subs that are
        # in the hand and cannot be used as a substitute. After iterating
        # availableSubs will contain letters that can be substituted(the letters
        # that are not already in hand or that is being removed)
        for letters in newHand:
            availableSubs = availableSubs.replace(letters, '')
        # Deletes the letter given by the user from the hand
        del newHand[letter]
        # Replaces the removed letter with other letter present in the availableSubs
        newHand[random.choice(availableSubs)] = num
    
    return newHand

    


def play_game(word_list):
    """
    Allow the user to play a series of hands
    * Asks the user to input a total number of hands
    
    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.
    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.
            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands
    word_list: list of lowercase strings
    """

    totalScore = 0
    # Ask the user for the total number of hands they wanna play.

    # Check if the input given by the user for the no of hand is valid number or not
    numHands = input("Enter total number of hands: ")
    while numHands.isdigit() == False:
        print('The number of hands is not a number. Please use a number')
        numHands = input("Enter total number of hands: ")
    

    # Display the hand. 
    for hand in range(int(numHands)):
        newHand = deal_hand(handSize)
        print("Current Hand: ", display_hand(newHand))

        # Ask they want to substitute a letter.
        sub = str.lower(input("Would you like to substitute a letter (y/n)? "))
        if sub.lower() == "y":
            # ask which letter they want to substitue
            letter = str.lower(input("Which letter would you like to replace? "))
            subHand = newHand.copy()
            newHand = substitute_hand(subHand, letter) # substitutes the hand.
        print()

        
        # making a new copy of the hand in case the user wants to play the hand again.
        copyHand = newHand.copy()
        # plays the hand.
        handScore = play_hand(copyHand, word_list)
        print("-----------------------------------------------")

        # if the user replays, the score for replay.
        replayScore = 0
        # Ask if the user wants to play again.
        replay = str.lower(input("Would you like to replay the hand?(y/n) "))
        if replay.lower() == "y":
            replayScore = play_hand(newHand, word_list)
            print("-----------------------------------------------")
        
        # Caclulates the score for all the hand and replayed hand and spits the maximum
        # score by the user.
        totalScore += max(handScore, replayScore)

    # print the total score for the user.
    print("Total score over all hands:", totalScore)
    return totalScore


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)