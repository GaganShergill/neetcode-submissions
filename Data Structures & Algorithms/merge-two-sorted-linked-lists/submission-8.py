# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = self

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            pass
        
        curr1 = list1
        curr2 = list2

        prevNode1 = ListNode()
        prevNode1.next = curr1
        while (curr1 != None and curr2 != None):
            print()
            if curr1.val > curr2.val:
                prevNode1.next = curr2
                
                tmpNode = curr2.next
                curr2.next = curr1
                if curr1 == list1:
                    list1 = curr2
                prevNode1 = curr2
                curr2 = tmpNode
            else:
                prevNode1 = curr1
                curr1 = curr1.next
        
        if curr2:
            prevNode1.next = curr2
        return list1
        
