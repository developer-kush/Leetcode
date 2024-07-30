class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children == 1:
            if money == 4: return -1
            if money == 8: return 1
            return 0

        if money >= (children<<3): 
            return children - int((money-(children<<3)) > 0)

        if money < children: return -1

        money -= children

        if money//7 == children-1:
            if money%7 == 3: return children-2
            return children-1
        
        return money//7