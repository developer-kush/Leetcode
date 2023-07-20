class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if not stack: stack.append(i)
            elif stack[-1]>0 and i<0:
                flag = False
                while stack and stack[-1]>0:
                    if i<0 and stack[-1]<-i:
                        stack.pop()
                    elif stack[-1] == -i:
                        stack.pop()
                        flag = True
                        break
                    else: break
                if not flag and (not stack or stack[-1]<0): stack.append(i)
            else: stack.append(i)
        
        return stack

# 1 2 3 -1 2 
