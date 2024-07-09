class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time=0
        tot=0
        for s,t in customers:
            time=max(time,s)+t
            tot+=time-s
        return tot/len(customers)