# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        sorted_word = sorted(self.word)


        anagrams = []
        for candidate in word_list:
            
            if sorted(candidate) == sorted_word:
                anagrams.append(candidate)

        return anagrams
