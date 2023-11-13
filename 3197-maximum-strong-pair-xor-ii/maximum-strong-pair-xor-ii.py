class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0
        self.opposite = {'0':'1', '1':'0'}

    def add(self, s):
        self.count+=1
        s = bin(s)[2:].rjust(21, '0')

        node = self
        for i in s:
            if i not in node.children:
                node.children[i] = Trie()
            node = node.children[i]
        node.is_end = True

    def remove(self, s):
        self.count -= 1
        s = bin(s)[2:].rjust(21, '0')

        def rem(node, s, i):
            if i == len(s):
                node.is_end = False
                return not bool(node.children)

            if s[i] in node.children:
                next_node = node.children[s[i]]
                if rem(next_node, s, i + 1):
                    del node.children[s[i]]
                    return not bool(node.children) and not node.is_end
            return False

        rem(self, s, 0)
  
    def closest(self, s):
        if not self.count: return -1
        
        res = ''
        s = bin(s)[2:].rjust(21, '0')
        
        for i in s:
            if i in self.children: 
                res, self = res+i, self.children[i]
            elif self.opposite[i] in self.children:
                res, self = res+self.opposite[i], self.children[self.opposite[i]]
            else: return -1
        return int(res, 2)

    # def retrieve(self):
    #     def get(node,string,stings):
    #         if node.is_end:
    #             strings.append("".join(string))
    #         for ch in node.children:
    #             string.append(ch)
    #             get(node.children[ch],string,strings)
    #             string.pop()
    #     string=[]
    #     strings=[]
    #     get(self,string,strings)
    #     return strings

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        nums = sorted(set(nums))
        n = len(nums)
        
        res = 0
        tr = Trie()
        tr.add(nums[-1])
        pos = n-1
        for i in range(n-2, -1, -1):
            while pos > i and nums[pos] > (nums[i]<<1): tr.remove(nums[pos]); pos-=1
            tr.add(nums[i])
            digits = int(log2(nums[i]))+2
            closest = tr.closest(nums[i]^((1<<digits)-1))
            if closest == -1: continue
            res = max(res, nums[i] ^ closest)
        return res