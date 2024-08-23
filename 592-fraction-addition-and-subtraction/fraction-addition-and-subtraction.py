class Solution:
    def fractionAddition(self, expression: str) -> str:
        def getGCD(a, b):
            while a: a, b = b%a, a
            return b

        def add(n1, d1, n2, d2):
            num = d2*n1 + n2*d1
            den = d1*d2
            return [num,den]
        
        def makefrac(f, sign = 1):
            f = f.split('/')
            return [sign*int(f[0]),int(f[1])]

        expression = expression.split('+')
        fractions = []
        for ex in expression:
            fracs = ex.split('-')
            if fracs[0] != '': fractions.append(makefrac(fracs[0]))
            for i in range(1,len(fracs)):
                fractions.append(makefrac(fracs[i], -1))
        
        ans = fractions[0]
        for i in range(1,len(fractions)):
            ans = add(*ans, *fractions[i])

        gcd = getGCD(*ans)
        ans = [ans[0]//gcd, ans[1]//gcd]
        if ans[1]<0: ans[0]*=-1; ans[1]*=-1

        return f"{ans[0]}/{ans[1]}"