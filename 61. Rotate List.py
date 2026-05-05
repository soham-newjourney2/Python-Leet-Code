# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        last_node = head
        length = 1

        while last_node.next:
            last_node = last_node.next
            length += 1

        last_node.next = head

        k = k % length

        tail = length - k
        new_tail = last_node

        for _ in range(tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        