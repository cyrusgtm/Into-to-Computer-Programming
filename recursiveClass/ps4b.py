# Problem Set 4B
# Name: Cyrus Raj Gautam
# Collaborators: None
# Time Spent: 6 hours

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
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
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Creating a new empty dictionary
        self.dictionary = {}
        # list containing all the lowercase letters. This will be used as the keys of our new dictionary.
        lowerKeys = list(string.ascii_lowercase)
        # list containing all the lowercase letters. This will be used as values for our new dictionary
        lowerValues = list(string.ascii_lowercase)
        # Shift. If, for example, 2 is the shift then this line of code will take the two letters and it will
        # attach it to the end of the group of letters.
        lowerShift = lowerValues[shift:] + lowerValues[:shift]


        # list containing all the uppercase letters. This will also be used as the keys of our new dictionary.
        upperKeys = list(string.ascii_uppercase)
        # list contauining all the uppercase letters. This will be used as values of our new dictionary
        upperValues = list(string.ascii_uppercase)
        # Shifting letters as before.
        upperShift = upperValues[shift:] + upperValues[:shift]

        # Since, we need both uppercase and lowercase letters, we combine the upper keys and value and the lower
        # keys and values to get a bigger list.
        allKeys = lowerKeys + upperKeys
        allValues = lowerShift + upperShift

        # The bigger list is then added to the dictionary. It is mapped in a way that the keys of our dictionary
        # are the normal alphabets whereas the values are the shifted alphabets.
        for i in range(len(allValues)):
            self.dictionary[allKeys[i]] = allValues[i]


        return self.dictionary




    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift

        '''
        # list that will contain the shifted message
        shiftedMessage = []
        # iterate through the provided message
        for i in self.message_text:
            # check if the letter from the above iteration is in our main dictionary(from above) or not.
            if i in self.build_shift_dict(shift).keys():
                # if it is, then add the values of that letter from the above dictionary to the shifted
                # Message list.
                shiftedMessage.append(self.dictionary[i])
            else:
                # If not, just add the letter to the list.
                shiftedMessage.append(i)
        return ''.join(shiftedMessage)

        


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
            '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # The maximum valid word that will be calculated
        maxValidWord = 0
        # The optimum shift while iterating
        bestShift = 0
        # Our final decrypted Message
        # decryptedMessage = ''
        # Iterating through all the alphabet(# of alphabet = 26)
        for i in range(26):
            # Count of all the valid word while testing
            validWord = 0
            # applying the shift from range 0-25. 
            for word in (self.apply_shift(i)).split():
                # After the shift if the length of the word is 1
                if len(word)==1:
                    # If the word with length 1 is a valid alphabet
                    if word in string.ascii_letters:
                        # if that valid alphabet is a valid word, then we increase our validWord count
                        if is_word(self.get_valid_words(), word) == True:
                            validWord+=1
                else:
                    # If the word is greater than length 1 and is a valid word, then we increase
                    # our validWord count
                    if is_word(self.get_valid_words(), word) == True:
                        validWord+=1
            # if the valitWord count is greater than max Valid word, then change the max valid word count
            # to valid word count. Through the iteration, almost every iteration(while shifting letters) will 
            # have some words that are real words. The more real words form in iteration the more the count for
            # maxValidWord will change.
            if validWord > maxValidWord:
                maxValidWord = validWord
                bestShift = i                       # After findin the best match set your optimum shift to the i
                decryptedMessage = self.apply_shift(i) # Our decrypted message
        return (bestShift, decryptedMessage)


if __name__ == '__main__':
   #Example test case (PlaintextMessage)
   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())
#
   #Example test case (CiphertextMessage)
   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())

   # Test 1 for plain text
   plaintext = PlaintextMessage('Harry Potter', 1)
   print('Expected Output: Ibssz Qpuufs')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   # Test 1 for  Cipher text
   story = get_story_string()
   ciphertext = CiphertextMessage(story)
   print('Unencypted story:', ciphertext.decrypt_message())

   # Test 2 for Plain Text
   plaintext = PlaintextMessage('I love dogs.', 2)
   print('Expected Output: K nqxg fqiu.')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   # Test 2 for  Cipher text
   ciphertext = CiphertextMessage('K nqxg fqiu.')
   print('Expected Output:', (24, 'I love dogs.'))
   print('Actual Output:', ciphertext.decrypt_message())






