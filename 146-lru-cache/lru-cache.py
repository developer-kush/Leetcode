class QueueSet:

    class Node:
        def __init__(self, val, prev = None, next = None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.keys = {}
        self.head = self.tail = None

    def remove(self, key):
        node = self.keys[key]

        if node.prev is None: self.head = node.next
        else: node.prev.next = node.next

        if node.next is None: self.tail = node.prev
        else: node.next.prev = node.prev
        
        del self.keys[key]

    def add(self,key):
        if self.head is None:
            self.head = self.tail = self.Node(key)
            self.keys[key] = self.head
            return
        self.tail.next = self.Node(key, self.tail)
        self.tail = self.tail.next
        self.keys[key] = self.tail

    def refresh(self, key):
        self.remove(key)
        self.add(key)

    def popfront(self):
        val = self.head.val
        self.remove(val)
        return val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = {}
        self.q = QueueSet()

    def get(self, key: int) -> int:
    
    # def print(self):
    #     curr = self.head
    #     print("Queue : ",end = "")
    #     while curr:
    #         print(curr.val, end = " ")
    #         curr = curr.next
    #     print()
        # print("\nGet Called : ", key)
        if key in self.vals: 
            self.q.refresh(key)
            # self.q.print()
            return self.vals[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print("\nPut Called : ", key)
        if key in self.vals:
            self.vals[key] = value
            self.q.refresh(key)
            # self.q.print()
            return
        if len(self.vals) >= self.cap: 
            # print(self.vals.keys())
            rem = self.q.popfront()
            del self.vals[rem]
        self.q.add(key)
        self.vals[key] = value
        # self.q.print()

# APPROACH 1
# -> PUT all values in a queue

# 1 2 3 2 4 1 5 6
# [ , ]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)