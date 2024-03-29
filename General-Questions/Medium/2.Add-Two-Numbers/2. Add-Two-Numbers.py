from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = []
        list2 = []

        left = l1

        while left:
            list1.append(left.val)
            left = left.next 
                 
        list1.reverse()

        right = l2

        while right:
            list2.append(right.val)
            right = right.next
        
        list2.reverse()
        
        temp1 = ''.join(str(num) for num in list1)
        temp2 = ''.join(str(num) for num in list2)

        sum = str(int(temp1) + int(temp2))

        newList = [int(digit) for digit in sum]

        newList.reverse()

        def convert_to_linked_list(digits):
            head = ListNode()
            current = head

            for digit in digits:
                current.next = ListNode(digit)
                current = current.next

            return head.next
        
        linked_list = convert_to_linked_list(newList)

        return linked_list

        




        