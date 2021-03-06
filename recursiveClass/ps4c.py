# Problem Set 4C
# Name: Cyrus Raj Gautam
# Collaborators: None
# Time Spent: 3 hours

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        try: 
            self.valid_words = load_words(file_name)
        except NameError:
            self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        validWordCopy = self.valid_words[:].copy()
        return validWordCopy
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Creating a new Dictionary
        transposeDictionary = {} 
        # Iterating through the all lowercase alphabets
        for letter in string.ascii_lowercase:
            # if the letters from the alphabet are vowels
            if letter in VOWELS_LOWER:
                # find the index/position of the vowel in the from 'aeiou'. So if the letter is i the position/index
                # will be 2 and so on.
                vowelPosition = str.lower(VOWELS_LOWER).find(letter)
                # Now set the value of that vowel to the vowel with the same position/index from the permuted vowel string.
                transposeDictionary[letter] = vowels_permutation[vowelPosition]
                # Do the same thing with the uppercase Vowels too
                transposeDictionary[str.upper(letter)] = str.upper(vowels_permutation[vowelPosition])
            else:
                # If the letter are not vowels then map the letters with themselves for both
                # upper and lowercase.
                transposeDictionary[letter] = letter
                transposeDictionary[str.upper(letter)] = str.upper(letter)
        return transposeDictionary
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        newMessage = ''
        for i in self.message_text:
            # If the letter is an alphabet
            if i in string.ascii_letters:
                # Set the alphabet to it's value from the transpose dictionary
                i = transpose_dict[i]
            newMessage += i
        return newMessage
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # The maximum valid word that will be calculated
        maxValidWord = 0
        # Get all the permutation possible for our string of vowels
        vowelsPermutation = get_permutations(VOWELS_LOWER)
        # Iterate through all the Permutation of vowels.
        decryptedMessage = ''
        for permutation in vowelsPermutation:
            # Count of all the valid word while testing
            validWords = 0
            # Building a dictionary using the permutation
            transposeDictionary = self.build_transpose_dict(permutation)
            # iterating through all the word in made up using the permutation
            for word in self.apply_transpose(transposeDictionary).split():
                # if the word has length 1
                if len(word)==1:
                    # If the word with length 1 is a valid alphabet
                    if word in string.ascii_letters:
                         # if that valid alphabet is a valid word, then we increase our validWord count
                        if is_word(self.get_valid_words(), word) == True:
                            validWords+=1
                else:
                    # If the word is greater than length 1 and is a valid word, then we increase
                    # our validWord count
                    if is_word(self.get_valid_words(), word) == True:
                        validWords+=1

            # if the validWord count is greater than max Valid word, then change the max valid word count
            # to valid word count. Also get the sentence/word with the max valid word and set it as
            # our decrypted message          
            if validWords > maxValidWord:
                    maxValidWord = validWords
                    decryptedMessage = self.apply_transpose(transposeDictionary)

        # If our max Valid word is 0, return the initial message itself, else return the decrypted message.
        if maxValidWord == 0:
            return self.message_text
        else:
            return decryptedMessage
    

if __name__ == '__main__':

    # Example test case
    print('Example 1')
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print('-------------------------------------------------------')
     
    #TODO: WRITE YOUR TEST CASES HERE
    print('Test Case 1')
    message = SubMessage("I'll be there for you.")
    permutation = "aueio"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "E'll bu thuru fir yio.")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print('-------------------------------------------------------')

    print('Test case 2')
    message = SubMessage("Knock knock! Who's there? Tank. Tank who? You are welcome.")
    permutation = "uoiea"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Kneck kneck! Whe's thoro? Tunk. Tunk whe? Yea uro wolcemo.")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print('-------------------------------------------------------')
     
