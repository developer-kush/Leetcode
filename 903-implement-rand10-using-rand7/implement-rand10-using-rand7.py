# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        f = -1

        while f==-1:
            num = rand7()
            if num < 6: f = num
            else: l = num&1

        try: l
        except:
            l = rand7()
            while l == 7: l = rand7()
            l &= 1

        return (((f-1)<<1)|l)+1