class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        dic = {}
        indx = 0
        for i, j in costs:
            arr.append((i-j, indx))
            dic[(arr[-1][0], indx)] = [i,j]
            indx += 1
        arr.sort()
        l = 0
        r = len(costs) -1
        ans = 0
        while r > l:
            ans += dic[arr[l]][0]
            ans += dic[arr[r]][1]
            r -= 1
            l += 1
        return ans
            
            
        