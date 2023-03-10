class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        pointer = 0
        while tickets[k] != 0:
            if tickets[pointer] > 0:
                tickets[pointer]-=1
                time += 1
            pointer += 1
            if pointer == len(tickets):
                pointer = 0
        return time 
        