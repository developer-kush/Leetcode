class Solution:
    def numSteps(self, s: str) -> int:
        letters = list(s)
        cnt = 0
        while letters != ['1']:
            if letters[-1] == '0':
                cnt += 1
                letters.pop()
            else:
                cnt += 1
                while letters and letters[-1] == '1':
                    letters.pop()
                    cnt += 1
                if not letters: break
                else: 
                    letters.pop()
                    letters.append('1')
        return cnt