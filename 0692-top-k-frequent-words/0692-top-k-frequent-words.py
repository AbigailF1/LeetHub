class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr = []
        count = Counter(words)
        heap = []
        for i in count:
            heappush(heap, [(-1 *count[i]), i])
        for i in range(k):
            f, w = heappop(heap)
            arr.append(w)
        # arr.append(heap[-1][1])
        return arr
        
        
        
        