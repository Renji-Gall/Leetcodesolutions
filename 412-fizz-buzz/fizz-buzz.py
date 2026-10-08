class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = list(range(1, n + 1))

        for i in range(len(arr)):
            if arr[i] % 3 == 0 and arr[i] % 5 == 0:
                arr[i] = "FizzBuzz"
            elif arr[i] % 3 == 0:
                arr[i] = "Fizz"
            elif arr[i] % 5 == 0:
                arr[i] = "Buzz"
            else:
                arr[i] = str(arr[i])
        return arr