class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        Count={}
        for i in range(len(nums)):
            Count[nums[i]]=1+Count.get(nums[i],0)
        for i in Count.values():
            if i%2!=0:
                return False
        return True
        
