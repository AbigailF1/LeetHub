class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_dig = "".join(str(digit) for digit in digits)
        new_dig = int(new_dig)
        new_dig += 1
        new_dig = [int(i) for i in str(new_dig)]
        return new_dig        