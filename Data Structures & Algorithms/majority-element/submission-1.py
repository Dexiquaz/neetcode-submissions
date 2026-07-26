class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] +=1
            else:
                seen[nums[i]] = 1

        maxfreq=0
        ans = None
        for num, freq in seen.items():
            if maxfreq < freq:
                maxfreq = freq
                ans = num
        return ans

        