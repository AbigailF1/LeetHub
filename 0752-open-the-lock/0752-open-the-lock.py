class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def find(code):
            ans = []
            for i in range(4):
                updatedDigit = str((int(code[i]) + 1) % 10)
                ans.append(code[:i] + updatedDigit + code[i + 1:])

                updatedDigit = str((int(code[i]) - 1) % 10)
                ans.append(code[:i] + updatedDigit + code[i + 1:])
            return ans

        visited = set(deadends)
        if '0000' in visited:
            return -1
        queue = deque()
        queue.append(('0000', 0))
        while queue:
            code, moves = queue.popleft()
            if code == target:
                return moves
            for neigbour in find(code):
                if neigbour not in visited:
                    queue.append((neigbour, moves + 1))
                    visited.add(neigbour)
        return -1
