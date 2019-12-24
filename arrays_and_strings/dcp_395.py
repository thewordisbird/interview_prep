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


def group_anagrams(words):
    anagram_hash = {}
    for word in words:
        key = encode_word(word)
        if key in anagram_hash:
            anagram_hash[key].append(word)
        else:
            anagram_hash[key] = [word]

    return [v for _,v in anagram_hash.items()]

def encode_word(word):
    ascii_sum = 0
    for letter in word:
        ascii_sum += ord(letter.lower())

    return f'{ascii_sum}-{len(word)}'

if __name__ == "__main__":
    words = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    result = [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]
    print(group_anagrams(words) == result)