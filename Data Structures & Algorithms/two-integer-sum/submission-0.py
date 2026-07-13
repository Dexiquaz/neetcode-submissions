class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n, num in enumerate(nums):
            comp = target - num

            if comp in seen:
                return [seen[comp], n]
            
            seen[num] = n
        