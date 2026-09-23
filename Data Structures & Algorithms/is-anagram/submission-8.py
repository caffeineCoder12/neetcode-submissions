class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for i in s:
            if i not in h1:
                h1[i] = 0
            h1[i] += 1
        for j in t:
            if j not in h2:
                h2[j] = 0
            h2[j] += 1
        if h1 == h2:
            return True
        return False