class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            m = (i + j) // 2
            if nums[m] > target:
                j = m
            elif nums[m] < target:
                i = m + 1
            else:
                return m
        return i
