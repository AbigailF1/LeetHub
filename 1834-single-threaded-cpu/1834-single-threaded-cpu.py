class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        et = []
        for i, task in enumerate(tasks):
            heappush(et, (task[0], task[1], i))
        
        ans = []
        pt = []
        time = 0
        print(et, et[0][0])
        while et or pt:
            while et and (et[0][0] <= time):
                e, p, i= heappop(et)
                heappush(pt, (p, i))
                
            if pt:
                p, i = heappop(pt)
                ans.append(i)
                time += p
            elif et:
                time = et[0][0]
        return ans
                
        