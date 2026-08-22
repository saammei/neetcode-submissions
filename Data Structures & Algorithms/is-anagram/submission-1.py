class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = {}
        for x in s:
            if x in r:
                r[x] += 1
            else:
                r[x] = 1
        for x in t:
            if x not in r:
                return False
            r[x] -= 1
        for x in r:
            if r[x] != 0:
                return False
        return True