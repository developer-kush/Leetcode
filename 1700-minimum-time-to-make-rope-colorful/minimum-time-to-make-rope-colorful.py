class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot=0
        currtot=currmax=neededTime[0]
        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                currtot+=neededTime[i]
                currmax=max(currmax,neededTime[i])
            else:
                tot+=currtot-currmax
                currtot=currmax=neededTime[i]
        return tot+currtot-currmax
    