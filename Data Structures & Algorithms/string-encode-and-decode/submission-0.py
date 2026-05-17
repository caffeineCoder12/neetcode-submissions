class Solution:
    l = []
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        strs2 = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            n = int(s[i:j])
            strs2.append(s[j+1:j+1+n])
            i = j + 1 + n
        return strs2
        