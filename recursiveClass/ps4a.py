# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # list that contains all the permutations
    allPermutation = []
    # if the word given is made out of 1 letter, then it print the letter
    if len(sequence) == 1:
    	return list(sequence)

    # main process. It follows a simple rule. To create permutation of, lets say, a word with 3 
    # letters 'abc', we can do it the following way
    # Permutation of 'abc' = 'a' + Permutation of 'bc', b + Permutation of ac, and c + Permutation of ab = 
    # 'ab' + permutation of c, 'ac' + permutation of  b, 'ba' + Permutation of c, 'bc' + permutation
    # of 'a', 'ca' + permutation of b, 'cb' + permutation of 'a'

    # This line is a recursive call that gives us permutation of all n-1 letters
    permutation = get_permutations(sequence[1:])
    # First letter in the word.
    letter = sequence[0]

    # This is the recusion process. Iterate through the list of all the permutation of length
    # n-1. 
    for perm in permutation:
    	for i in range(len(perm)+ 1):
    		# This part joins the permutation with the first letter. In this the first letter is added to the
    		# each index. 
    		allPermutation.append(perm[:i] + letter + perm[i:])
    return allPermutation




if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))


   example_input2 = 'xyz'
   print('Input:', example_input)
   print('Expected Output:', ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
   print('Actual Output:', get_permutations(example_input2))
    

   example_input3 = 'mnop'
   print('Input:', example_input)
   print('Expected Output:', ['mnop', 'mnpo', 'mpno', 'mpon', 'monp', 'mopn', 'nmop', 'nmpo', 'nomp', 'nopm', 'npom', 'npmo', 'ompn', 'omnp', 'onmp', 
   	'onpm', 'opmn', 'opnm', 'pmno', 'pmon', 'pnom', 'pnmo', 'pomn', 'pomn'])
   print('Actual Output:', get_permutations(example_input3))

