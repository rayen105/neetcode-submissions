class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        for e in nums:
            d[e]=d.get(e,0)+1
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1],reverse=True))
        l=list(sorted_d.keys())[:k]
        return l

        