class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        pixel = image[sr][sc]
        row = len(image)
        col = len(image[0])
        def colour(i, j):
            if (i, j) in visited or i < 0 or i >=row or j < 0 or j >=col or image[i][j]!= pixel:
                return 
            visited.add((i,j))
            image[i][j] = color
            colour (i, j+1)
            colour (i, j-1)
            colour (i+1, j)
            colour (i-1, j)
            return 
        
        colour(sr, sc)
        return image            
            
                    
                    
                    