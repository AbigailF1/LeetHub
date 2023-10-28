class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        equal =  []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        smaller.extend(equal)
        smaller.extend(greater)
        return smaller