class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_day = sum(weights)
        min_day = max(weights)
        while min_day <= max_day:
            cur_sum = 0
            cur_day = 0
            mid = (min_day + max_day) //2
            for i in weights:
                if cur_sum + i <= mid:
                    cur_sum += i
                else:
                    cur_day += 1
                    cur_sum = i
            if cur_sum != 0: 
                cur_day += 1
            if cur_day <= days:
                max_day = mid - 1
            else:
                min_day= mid + 1
        return min_day

                
                
                
        