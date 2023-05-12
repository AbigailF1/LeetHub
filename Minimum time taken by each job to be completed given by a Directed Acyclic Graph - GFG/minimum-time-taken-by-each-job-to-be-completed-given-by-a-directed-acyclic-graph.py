from typing import List


from typing import List

from collections import defaultdict, deque
class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        dic = defaultdict(list)
        incoming = [1]* n
        for u, v in edges:
            dic[u].append(v)
            incoming[v - 1] += 1
        visited = set()
        queue = deque()
        for i in range(n):
            if incoming[i] == 1:
                queue.append(i+1)
                visited.add(i+1)
        ans = [0]*n
        count = 0
        while queue:
            count += 1
            for i in range(len(queue)):
                x = queue.popleft()
                ans[x-1] += count
                for j in dic[x]:
                    incoming[j - 1] -= 1
                    if incoming[j - 1] == 1:
                        queue.append(j)
                        visited.add(j)
        return " ".join(list(map(str, ans)))
        
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends