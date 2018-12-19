# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Problem Statement:
# 
# In a deck of cards, each card has an integer written on it.
# 
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
# 
# Each group has exactly X cards.
# All the cards in each group have the same integer.

# Problem Difficulty: Easy

from fractions import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck):
        if len(deck)==1:
            return False
        d = collections.Counter(deck).values()
        a = reduce(gcd, d)
        return a>1
