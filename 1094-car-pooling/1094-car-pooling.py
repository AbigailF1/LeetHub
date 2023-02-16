class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        y=0
        for i in range(len(trips)):
            y = max(y, trips[i][-1])
        x=[0]*(y+1)
        for trip in trips:
            seats,l,r = trip[0],trip[1],trip[2]
            x[l]+=seats
            x[r]-=seats  
        prefixsum=0
        arr=[]
        for i in x:
            prefixsum+=i
            arr.append(prefixsum)
        z=0
        for g in arr:
            z = max(z, g)
        if z<=capacity:
            return True 
        else:
            return False
            
    