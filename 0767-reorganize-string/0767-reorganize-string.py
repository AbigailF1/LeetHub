class Solution:
    def reorganizeString(self, s: str) -> str:
        new_s = ""
        dic = Counter(s)
        maxheap = []
        for val, count in dic.items():
            heappush(maxheap, [-count, val])
        heapify(maxheap)
        prev = None
        
        while prev or maxheap:
            # print(maxheap, prev)
            if prev and not maxheap:
                return ""
            count, val = heappop(maxheap)
            count += 1
            new_s += val
            
            if prev:
                heappush(maxheap,prev)
                prev = None
            if count != 0:
                prev = [count, val]
                
        return new_s
