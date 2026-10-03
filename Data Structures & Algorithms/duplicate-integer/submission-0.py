class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        orig_len = len(nums)
        set_len = len(set(nums))

        return False if orig_len == set_len else True
        