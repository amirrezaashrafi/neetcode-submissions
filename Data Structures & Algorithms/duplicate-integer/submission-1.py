class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        return len(set(nums)) < len(nums)
        
            