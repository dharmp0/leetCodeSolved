class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        top_freq = []

        for i in nums:

            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        
        for key, val in sorted_freq[:k]:
            top_freq.append(key)

        return top_freq
