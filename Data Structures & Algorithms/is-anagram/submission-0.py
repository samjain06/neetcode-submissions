class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
        
        for val in char_count.values():
            if val != 0:
                return False
        
        return True