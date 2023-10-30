class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        num = 1
        lenn = len(arr)

        while k:
            if i == lenn:
                break
            if arr[i] != num:
                num += 1
                k-=1
            else:
                i += 1
                num += 1
        while k:
            num += 1
            k -= 1
        return num - 1

        