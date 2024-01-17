class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        return sum((s-t).values()) 
