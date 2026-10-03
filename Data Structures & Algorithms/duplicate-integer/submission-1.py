class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        orig_len = len(nums)
        set_len = len(set(nums))

        return len(nums) != len(set(nums))
        