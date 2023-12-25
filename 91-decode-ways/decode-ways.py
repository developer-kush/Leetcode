class Solution:
    def numDecodings(self, s: str) -> int:
        a=b=1
        if s[0]=="0": return 0
        for i in range(1,len(s)):
            if s[i]=="0" and not("0"<s[i-1]<"3"):
                return 0
            elif s[i]=="0":
                a,b=b,a
            elif "0"<s[i-1]<"2" or s[i]<="6" and s[i-1]=="2":
                a,b=b,a+b
            else:
                a,b=b,b
        return b