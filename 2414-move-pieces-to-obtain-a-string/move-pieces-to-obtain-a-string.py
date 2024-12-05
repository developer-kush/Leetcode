class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        def nxt(pos,string):
            for i in range(pos+1,n):
                if string[i]!='_': return i
            return n
        
        n=len(start)
        xpos=ypos=-1
        
        while xpos!=n or ypos!=n:
            xpos,ypos=nxt(xpos,start),nxt(ypos,target)
            if xpos==n and ypos==n: return True
            elif xpos==n or ypos==n: return False
            if start[xpos]!=target[ypos]: return False
            if start[xpos]=='L' and xpos<ypos: return False
            if start[xpos]=='R' and xpos>ypos: return False
        return True