class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for i in row:
                heappush(heap, i)
        
        while k > 1:
            k -=1
            heappop(heap)

        return heap[0]