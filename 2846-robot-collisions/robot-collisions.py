class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        robots = [[idx, positions[idx], healths[idx], directions[idx]] for idx in range(len(positions))]
        robots.sort(key = lambda x: x[1])

        for robot in robots:
            while stack and stack[-1][3] == 'R' and robot[3] == 'L' and robot[2] > stack[-1][2]:
                stack.pop()
                robot[2] -= 1
            if (not stack) or stack[-1][3] == 'L' or robot[3] == 'R': stack.append(robot)
            elif stack[-1][2] == robot[2]: stack.pop()
            elif stack[-1][2] > robot[2]: stack[-1][2] -= 1
            else:
                robot[2] -= 1
                stack[-1] = robot
        
        stack.sort()
        return [x[2] for x in stack]