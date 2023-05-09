class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dic = defaultdict(list)
        dic2 = defaultdict(int)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                dic[ingredients[i][j]].append(recipes[i])
                dic2[recipes[i]] += 1
       
        queue = deque()
        ans = []
                   
        for i in supplies:
            queue.append(i)
                
        r = set(recipes)
        while queue:
            x = queue.popleft()
            if x in r:
                ans.append(x)
            for neighbour in dic[x]:
                dic2[neighbour] -= 1
                if dic2[neighbour] == 0:
                    queue.append(neighbour)
        
        return ans
        
        