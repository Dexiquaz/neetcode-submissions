class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        x =[]
        for num in nums:
            if num in freq:
                freq[num] = freq[num]+1
            else:
                freq[num] = 1
        m = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            x.append(m[i][0])
        return x