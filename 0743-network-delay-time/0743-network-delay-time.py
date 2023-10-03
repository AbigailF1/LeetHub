class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {node: float('inf') for node in range(1,n+1)}
        distances[k] = 0
        
        graph = defaultdict(list)
        for a,b,time in times:
            graph[a].append((b,time))
           
        visited = set() 
        priority_queue = [(0, k)]
        while priority_queue:
            current_time, current_node = heapq.heappop(priority_queue)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, time in graph[current_node]:
                distance = current_time + time
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        # print(distances,max(distances.values()) )
        if max(distances.values()) == inf:
            return -1
        else:
            return max(distances.values())
     
