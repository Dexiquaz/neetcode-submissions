class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = -1
        for n in range(len(nums)):
            if nums[n] == target:
                return n

        return x
