class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for index, val in enumerate(nums):
            diff = target - val
            if diff in nums_dict:
                return [nums_dict[diff], index]
            nums_dict[val] = index
        
        return []