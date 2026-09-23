class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for i in w:
                count[ord(i)-ord('a')] += 1
            hashmap[tuple(count)].append(w)
        return list(hashmap.values())