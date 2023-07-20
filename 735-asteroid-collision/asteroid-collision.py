class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if not len(stack): stack.append(i);continue
            if stack[-1]<0 or i>0: stack.append(i);continue
            while len(stack) and stack[-1]>0 and i<0:
                if -i>stack[-1]:
                    stack.pop()
                else: 
                    curr = stack.pop()
                    i = None if curr==-i else curr
                    break

            if i: stack.append(i)
            # if len(stack): stack.pop()
            # stack.append(i)

        return stack