class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [[s] for s in strs]
        
        result = {}

        for word in strs:
            sorted_joined_word = "".join(sorted(word))
            if sorted_joined_word in result:
                result[sorted_joined_word].append(word)
            else:
                result[sorted_joined_word] = [word]

        return list(result.values())