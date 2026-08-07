class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        dic={}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                res = True
    
                break
        return res
        