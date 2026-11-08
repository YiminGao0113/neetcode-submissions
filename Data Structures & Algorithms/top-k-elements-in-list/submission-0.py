import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This seems easy we just rank them?
        count = {}
        heap = []

        for num in nums:
            count[num] = count.get(num, 0) + 1


        for num, freq in count.items():
            # python implements a min-heap...
            heapq.heappush(heap, [freq, num])

            if len(heap) > k:
                heapq.heappop(heap)
        

        return [num for freq, num in heap]