# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        start = 0
        end = len(pairs) - 1

        return self.sort(pairs, start, end)

    def sort(self, pairs, s, e):
        # base case
        if e - s + 1 <= 1:
            return pairs

        # calculate middle index
        m = (s + e) // 2

        # sort left half
        self.sort(pairs, s, m)

        # sort right half
        self.sort(pairs, m+1, e)

        # merge sorted half
        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, pairs, s, m, e):
        i = 0
        j = 0
        k = s

        L = pairs[s:m+1]
        R = pairs[m+1:e+1]

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            elif L[i].key > R[j].key:
                pairs[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1
        
        return pairs

