class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)

        curr = n[0]

        for i in range(1, len(n)):
            if n[i] < n[i-1]:
                ch = n[i-1]
                while i and n[i-1] == ch: i-=1
                i+=1
                return int (
                    (
                        n[:i-1] + str(int(ch)-1) + '9'*(len(n)- i)
                    ).lstrip('0')
                )
        return int(n)