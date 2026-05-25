# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        while (curr != None):
            if curr.next == None:
                curr.next = list2
                break
            curr = curr.next
        
        if list1 is None:
            list1 = list2
        
        prevNode1 = ListNode()
        prevNode1.next = list1
        curr1 = list1
        while (curr1 != None):
            prevNode2 = curr1
            curr2 = curr1.next
            while (curr2 != None):
                if curr1.val > curr2.val:
                    prevNode1.next = curr2
                    prevNode2.next = curr1

                    tmpNode = curr2.next
                    curr2.next = curr1.next
                    curr1.next = tmpNode

                    tmpNode = curr2
                    curr2 = curr1
                    curr1 = tmpNode
                    if curr2 == list1:
                        list1 = curr1
                
                prevNode2 = curr2
                curr2 = curr2.next
            prevNode1 = curr1
            curr1 = curr1.next

        return list1
        
