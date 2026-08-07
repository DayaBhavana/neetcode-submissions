class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        dic={}
        for i in nums:
            if i  in dic:
                res = True
            dic[i] = 1
        return res
        