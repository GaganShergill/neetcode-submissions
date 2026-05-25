class ListNode:
    def __init__(self, val:int=0):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def printList(self):
        [print(el, end="-> ") for el in self]
        print()
        print()

    def get(self, index: int) -> int:
        self.printList()
        if index >= self.length or index < 0:
            return -1
        else:
            curr = self.head
            i = 0
            while curr:
                if i == index:
                    return curr.val
                i += 1
                curr = curr.next
            return -1
        

    def addAtHead(self, val: int) -> None:
        # self.printList()
        newNode = ListNode(val)
        if self.length: 
            newNode.next = self.head
            self.head.prev = newNode
        else:
            self.tail = newNode
        
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        # self.printList()
        newNode = ListNode(val)
        if self.length:
            newNode.prev = self.tail
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # self.printList()
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            i = 0
            while curr:
                if i == index:
                    prevNode = curr.prev
                    prevNode.next = ListNode(val)
                    prevNode.next.prev = prevNode
                    prevNode.next.next = curr
                    curr.prev = prevNode.next
                    self.length += 1
                    return
                i += 1
                curr = curr.next



    def deleteAtIndex(self, index: int) -> None:
        # self.printList()
        if index >= self.length or index < 0:
            return
        else:
            curr = self.head
            i = 0
            while curr:
                if i == index:
                    if curr == self.head:
                        self.head = curr.next
                        curr = None
                        if self.head:
                            self.head.prev = None
                    
                    if curr == self.tail:
                        self.tail = curr.prev
                        curr = None
                        if self.tail:
                            self.tail.next = None
                            
                    if curr:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    
                    self.length -= 1
                    return

                i += 1
                curr = curr.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)