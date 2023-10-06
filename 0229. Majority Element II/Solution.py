class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l1=[]
        l=set(nums)
        for i in l:
            if nums.count(i)>len(nums)//3:
                l1.append(i)
        return l1
