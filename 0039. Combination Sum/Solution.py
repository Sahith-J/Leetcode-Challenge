class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(arr,n,target,arr2):
            if target==0:
                res.append(arr2)
                return
            for i in range(n,len(arr)):
                if arr[i]<=target:
                    backtrack(arr,i,target-arr[i],arr2+[arr[i]])
        n=len(candidates)
        arr2=[]
        backtrack(candidates,0,target,arr2)
        return res

                
        
