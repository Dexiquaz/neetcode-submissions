class Solution:
    def findMin(self, nums: List[int]) -> int:
        x = float("infinity")
        for i in nums:
            if i <= x:
                x = i
        return x
                
        