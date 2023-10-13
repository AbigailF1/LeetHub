class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        test_cases = ( minutesToTest // minutesToDie)
        test_cases += 1
        x = 0
        while (test_cases ** x) < buckets:
            x += 1
        return x
        