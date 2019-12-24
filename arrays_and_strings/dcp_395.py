# Given an array of strings, group anagrams together.

# Example.
# Given:
#   ['eat', 'ate', 'apt', 'pat', 'tea', 'now']

# Return:
#   [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]

# Analysis:
# This algorithm runs in O(NM) where N is the number of words in the array, 
# and M is the number of letters in each word.
# The space complexity is O(N) as a hash table is required which will hold all the words

# This algorithm assumes words will be all alpha and doesn't have any checks otherwise. 
#   though, as it is simply using ascii values, any value in the ascii table would work
#   with a modification to the encode_word function to check if it's alphabetic before
#   running the lower() method on it. 


def group_anagrams(words):
    '''Returns anagrams grouped together'''
    # Words are encoded to have a key unique to an anagram.
    # This key is stored in the anagram_hash and words with 
    #   the same anagram_key are added to the value list as they
    #   are seen. 
    # The values in the anagram_hash are returned as the result
    anagram_hash = {}
    for word in words:
        key = encode_word(word)
        if key in anagram_hash:
            anagram_hash[key].append(word)
        else:
            anagram_hash[key] = [word]

    return [v for _,v in anagram_hash.items()]

def encode_word(word):
    '''Sums ascii codes of each letter and appends the word
        length to form a key unique to an anagram'''
    ascii_sum = 0
    for letter in word:
        ascii_sum += ord(letter.lower())

    return f'{ascii_sum}-{len(word)}'

if __name__ == "__main__":
    words = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    result = [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]
    print(group_anagrams(words) == result)

    words = ['eAt', 'ate', 'apt', 'Pat', 'tea', 'now']
    result = [['eAt', 'ate', 'tea'], ['apt', 'Pat'], ['now']]
    print(group_anagrams(words) == result)

    words = ['eAts', 'ate', 'apt', 'Pat', 'tea', 'now', 'SEAT']
    result = [['eAts', 'SEAT'], ['ate', 'tea'], ['apt', 'Pat'], ['now']]
    print(group_anagrams(words) == result)