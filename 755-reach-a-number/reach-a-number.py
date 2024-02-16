class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        closest = int(sqrt(target*2))

        if target == closest*(closest+1)//2: return closest

        while (dist:=((closest*(closest+1)//2) - target))&1 or dist < 0:
            closest += 1

        return closest