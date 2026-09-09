class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarr = list(s)
        tarr = list(t)
        sarr.sort()
        tarr.sort()
        return sarr == tarr
