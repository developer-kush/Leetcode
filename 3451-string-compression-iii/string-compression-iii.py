class Solution:
    def compressedString(self, word: str) -> str:
        n, last, res = len(word), 0, ''
        for i in range(1, n):
            if word[i]!=word[i-1]:
                res += f"9{word[i-1]}"*((i-last)//9)+(f"{(i-last)%9}{word[i-1]}" if (i-last)%9 else "")
                last = i

        res += f"9{word[n-1]}"*((n-last)//9)+(f"{(n-last)%9}{word[n-1]}" if (n-last)%9 else "")
        return res