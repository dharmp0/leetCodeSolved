from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2)  or set(word1) != set(word2):
            return False
        
        dict1 = {}
        dict2 = {}

        for i in word1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in word2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        
        if dict1 == dict2:
            return True
        elif Counter(dict1.values()) == Counter(dict2.values()):
            return True
        else:
            return False
