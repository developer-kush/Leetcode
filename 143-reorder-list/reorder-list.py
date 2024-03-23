
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dq = deque()
        while head:
            dq.append(head)
            head = head.next

        curr = dq.popleft()
        for i in range(len(dq)):
            if i & 1: curr.next = dq.popleft()
            else: curr.next = dq.pop()
            curr = curr.next
        curr.next = None