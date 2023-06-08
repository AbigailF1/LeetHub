class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        
        def helper(val):
            r = (val - 1) // n
            c = (val - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r,c]
        
        queue = deque()
        visited = set()
        queue.append([1, 0]) # [values, moves]
        visited.add(1)
        
        while queue:
            val, moves = queue.popleft()
            
            for i in range(1, 7):
                next_val = val + i
                row, col = helper(next_val)
                if board[row][col] != -1:
                    next_val = board[row][col]
                if next_val == n*n:
                    return moves + 1
                if next_val not in visited:
                    queue.append([next_val, moves + 1])
                    visited.add(next_val)
        return -1
        
        
                
        