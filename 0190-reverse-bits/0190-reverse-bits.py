class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        while n:
            ans.append(str(n%2))
            n = n // 2
        ans += ["0"] * (32 - len(ans))
        num = int("".join(ans), 2)
        return num
        