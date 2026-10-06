class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            lookup_num = target - n
            if lookup_num in nums_map:
                return [nums_map[lookup_num], i]
            nums_map[n] = i

    
        return []