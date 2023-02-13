class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        A=[]
        for i in range(1,n+1):
          numbers=''
          if i%3==0 and i%5==0:
            numbers+="FizzBuzz"
          elif i%3==0:
            numbers+="Fizz"
          elif i%5==0:
            numbers+="Buzz"
          else:
            numbers+=str(i)
          A.append(numbers)
        return A
    
    