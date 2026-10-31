# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        total = 0
        index = -1
        length = head
        while length:
            index += 1
            length = length.next



        current = head
        while current:
            total += current.val * (2 ** index)
            index -= 1
            current = current.next
        
        return total