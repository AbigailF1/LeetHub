class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        births = defaultdict(int)
        max_ = 1
        for birth, death in logs:
            births[birth] = 1
            for birth2, death2 in logs:
                if birth >= birth2 and birth < death2:
                    births[birth] += 1
                    max_ = max(max_, births[birth])
        
        # print(births)
        ans = []
       
        for key, values in births.items():
            if values == max_:
                ans.append(key)
        ans.sort()
        # print(logs)
        return ans[0]
        
           

