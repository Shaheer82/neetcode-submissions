class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        for char in s:
            if char not in dict_1:
                dict_1[char] = 1
            else:
                dict_1[char] += 1

        dict_2 = {}
        for char_2 in t:
            if char_2 not in dict_2:
                dict_2.update({char_2:1})
            else:
                dict_2[char_2] += 1
        
        if dict_1 == dict_2:
            return True
        return False
