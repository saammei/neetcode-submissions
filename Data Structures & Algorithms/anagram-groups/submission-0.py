class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            ans[key].append(s)
        return list(ans.values())