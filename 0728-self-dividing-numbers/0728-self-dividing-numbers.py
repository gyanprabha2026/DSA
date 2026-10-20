class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        
        op = []

        for i in range(left, right + 1):
            num = i
            temp = i
            sd = True

            while temp > 0:
                d = temp % 10

                if d == 0 or num % d != 0:
                    sd = False
                    break

                temp //= 10

            if sd:
                op.append(num)

        return op