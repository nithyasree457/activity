class Solution:
    def findTheDifference(self, s, t):
        for ch in t:
            if s.count(ch) != t.count(ch):
                return ch
