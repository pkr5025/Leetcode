
# Problem Statement:
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
# The order of the alphabet is some permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the alphabet, 
# return true if and only if the given words are sorted lexicographicaly in this alien language.

# Problem Difficulty: Easy


import functools
class Solution:
    def isAlienSorted(self, words, order):
        for i in range(len(words)-1):
            if self.cmp(words[i], words[i+1], order) == False:
                return False
        return True
    def cmp(self, word1, word2, order):
            n1, n2 = len(word1), len(word2)
            for i in range(min(n1,n2)):
                if order.find(word1[i])< order.find(word2[i]):
                    return True
                elif order.find(word1[i]) > order.find(word2[i]):
                    return False
            return n1<n2
