class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = [[0, 0]]
        op = []
        for i in expression:
            if i == ',': continue
            if i in '!|&': op.append(i)
            if i == '(': st.append([0, 0])
            if i == 't': st[-1][0]+=1; st[-1][1]+=1
            if i == 'f': st[-1][1]+=1
            if i == ')':
                t, c = st.pop()
                o = op.pop()
                if o == '!':
                    if t == 0: st[-1][0]+=1; st[-1][1]+=1
                    else: st[-1][1] += 1
                if o == '|':
                    if t > 0: st[-1][0]+=1; st[-1][1]+=1
                    else: st[-1][1] += 1
                if o == '&':
                    if t == c: st[-1][0]+=1; st[-1][1]+=1
                    else: st[-1][1] += 1
        
        return bool(st[0][0])