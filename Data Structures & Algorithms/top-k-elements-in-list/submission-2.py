class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            l.append(tuple(sorted_count.keys())[i])
        return l