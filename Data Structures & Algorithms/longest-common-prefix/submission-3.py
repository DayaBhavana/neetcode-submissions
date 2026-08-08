class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        plen=len(pre)
        for s in (strs[1:]):
            while pre[0:plen]!=s[0:plen]:
                plen-=1
                if plen==0:
                    return ""
            pre=pre[0:plen]
        return pre
        