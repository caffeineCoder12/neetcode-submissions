class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = {}
        n2 = {}
        for i in s:
            if i in n1:
                n1[i] += 1
            else:
                n1[i] = 1;
        for j in t:
            if j in n2:
                n2[j] += 1
            else:
                n2[j] = 1;
        if n1.items()==n2.items():
            return True
        return False