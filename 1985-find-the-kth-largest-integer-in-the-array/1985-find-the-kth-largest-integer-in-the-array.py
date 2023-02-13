class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr=[]
        for i in nums:
            i=int(i)
            arr.append(i)
        x=sorted(arr, reverse=True)
        y=x[k-1]
        s=(f"{y}")
        return s
