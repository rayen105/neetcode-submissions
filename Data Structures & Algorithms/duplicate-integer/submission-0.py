class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        n1=len(nums)
        n2=len(s)
        return not (n1==n2)
        