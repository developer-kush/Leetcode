class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @cache
        def rec(rob, fac, lim):
            if rob < 0: return 0
            # if fac < 0: return float('inf')
            if lim == 0: 
                if fac == 0: return float('inf')
                return rec(rob, fac-1, factory[fac-1][1])
            
            a = rec(rob, fac-1, factory[fac-1][1]) if fac > 0 else float('inf')
            b = rec(rob-1, fac, lim-1) + abs(robot[rob]-factory[fac][0])

            return min(a, b)
        
        return rec(len(robot)-1, len(factory)-1, factory[-1][1])