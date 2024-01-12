class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_half = s.lower()[len(s)//2:]
        s = s.lower()[:len(s)//2]
        vow = ['a','e','i','o','u']
        def cnt(v):
            count = 0
            for i in range(len(v)):
                if v[i] in vow:
                    count+=1
            return count
        if cnt(s) == cnt(s_half):
            return True
        return False
