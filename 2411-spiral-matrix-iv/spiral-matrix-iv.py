# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]
        u, d, r, l = 1, m-1, n-1, 0
        dir = 0
        x = y = 0
        
        while head:
            mat[x][y] = head.val
            head = head.next 

            if dir == 0 and y == r:
                dir = 1
                r -= 1
            elif dir == 1 and x == d:
                dir = 2
                d -= 1
            elif dir == 2 and y == l:
                dir = 3
                l += 1
            elif dir == 3 and x == u:
                dir = 0
                u += 1
            
            match dir:
                case 0 : y += 1
                case 1 : x += 1
                case 2 : y -= 1
                case 3 : x -= 1

            # for i in mat: print(*i)
            # print()

        return mat
                