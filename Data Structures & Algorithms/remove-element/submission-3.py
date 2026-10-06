class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = 0
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                
        return l
