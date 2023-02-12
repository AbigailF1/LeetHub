class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
            
        task_counts = list(counter.values())
        
        max_count = max(task_counts)
                
        max_count_times = task_counts.count(max_count)
        y=max(len(tasks), (max_count- 1) * n + max_count + (max_count_times - 1)) 
        return y
        