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
        elif index < self.length // 2:
            curr = self.head
            i = 0
            while curr:
                if i == index:
                    return curr.val
                i += 1
                curr = curr.next    
        else:
            curr = self.tail
            i = self.length-1
            while curr:
                if i == index:
                    return curr.val
                i -= 1
                curr = curr.prev
        
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
        if index > self.length and index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length // 2:
            curr = self.head
            i = 0
            while curr:
                if i == index:
                    prevNode = curr.prev
                    newNode = ListNode(val)
                    prevNode.next = newNode
                    newNode.prev = prevNode
                    newNode.next = curr
                    curr.prev = newNode
                    self.length += 1
                    return
                i += 1
                curr = curr.next
        else:
            curr = self.tail
            i = self.length - 1
            while curr:
                if i == index:
                    prevNode = curr.prev
                    newNode = ListNode(val)
                    prevNode.next = newNode
                    newNode.prev = prevNode
                    newNode.next = curr
                    curr.prev = newNode
                    self.length += 1
                    return
                i -= 1
                curr = curr.prev



    def deleteAtIndex(self, index: int) -> None:
        # self.printList()
        if index >= self.length or index < 0:
            return
        elif index < self.length // 2:
            curr = self.head
            i = 0
            while curr:
                if i == index:
                    if curr == self.head:
                        self.head = curr.next
                        if self.head:
                            self.head.prev = None
                        if curr == self.tail:
                            self.tail = curr.prev
                    
                    elif curr == self.tail:
                        self.tail = curr.prev
                        self.tail.next = None
                            
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    
                    self.length -= 1
                    return

                i += 1
                curr = curr.next
        else:
            curr = self.tail
            i = self.length - 1
            while curr:
                if i == index:
                    if curr == self.head:
                        self.head = curr.next
                        if self.head:
                            self.head.prev = None
                        if curr == self.tail:
                            self.tail = curr.prev
                    
                    elif curr == self.tail:
                        self.tail = curr.prev
                        self.tail.next = None
                            
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    
                    self.length -= 1
                    return
                
                i -= 1
                curr = curr.prev



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)