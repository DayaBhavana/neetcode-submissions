class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for item in strs:
            key = ''.join(sorted(item))
            d[key].append(item)
        return list(d.values())
        