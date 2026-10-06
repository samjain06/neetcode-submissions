class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            lookup_num = target - nums[i]
            if lookup_num in nums_map.keys():
                return [nums_map.get(lookup_num), i]
            nums_map[nums[i]] = i

    
        return []