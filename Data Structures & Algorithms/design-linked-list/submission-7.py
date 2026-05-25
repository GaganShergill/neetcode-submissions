class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        # Create sentinel (dummy) nodes
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        # Link sentinels to each other
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
    
    def __iter__(self):
        # Start at the first actual data node, skip the dummy head
        curr = self.head.next
        while curr != self.tail:
            yield curr.val
            curr = curr.next

    def printList(self) -> None:
        for el in self:
            print(el, end="->")
        print("\n")

    def _getNode(self, index: int) -> ListNode:
        """Helper method to find and return the node at a specific index."""
        # Bidirectional search optimization
        if index < self.length // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.length - 1 - index):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        return self._getNode(index).val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        # Find the node currently at that index position
        # If inserting at tail-end, the target 'succ' node is the dummy tail
        succ = self._getNode(index) if index < self.length else self.tail
        pred = succ.prev
        
        newNode = ListNode(val)
        
        # Splice the new node cleanly between pred and succ
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode
        
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        # Find the actual node to delete
        curr = self._getNode(index)
        pred = curr.prev
        succ = curr.next
        
        # Bypass 'curr' entirely
        pred.next = succ
        succ.prev = pred
        
        self.length -= 1