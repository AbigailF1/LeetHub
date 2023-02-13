class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            d=(x**2)+(y**2)
            minHeap.append([d,x,y])
        heapq.heapify(minHeap)
        arr=[]
        while k>0:
            d,x,y=heapq.heappop(minHeap)
            arr.append([x,y])
            k-=1
        return arr