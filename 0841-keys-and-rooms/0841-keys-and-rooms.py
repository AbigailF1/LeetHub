class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)
        while queue:
            x = queue.popleft()
            for i in rooms[x]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return len(visited) == len(rooms)
                