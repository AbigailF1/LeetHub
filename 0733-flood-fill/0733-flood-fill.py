class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        pixel = image[sr][sc]
        direc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        row = len(image)
        col = len(image[0])
        def colour(i, j):
            if (i, j) in visited:
                return 
            visited.add((i,j))
            for di in direc:
                x, y = i + di[0], j + di[1]
                if 0 <= x < row and  0 <= y < col and image[x][y] == pixel:
                    image[x][y] = color 
                    colour(x, y)
                    
        if image[sr][sc] != color:
            image[sr][sc] = color
            colour(sr, sc) 
        return image            
            
                    
                    
                    