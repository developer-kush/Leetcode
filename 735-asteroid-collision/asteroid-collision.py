class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if not stack: stack.append(i);continue
            if stack[-1]<0 or i>0: stack.append(i);continue
            while stack and stack[-1]>0 and i<0:
                if -i>stack[-1]:
                    stack.pop()
                else: 
                    curr = stack.pop()
                    if curr != -i:
                        if curr>-i: stack.append(curr)
                        else: stack.append(i)
                    break
            else: stack.append(i)

            # if ast: stack.append(ast)
            
        return stack

# 1 2 3 -1 2 
