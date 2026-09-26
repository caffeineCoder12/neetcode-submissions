class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        s1 = sorted(s1)
        for i in range(n2 - n1 + 1):
            window = s2[i:i+n1]
            if sorted(window) == s1:
                return True
        return False