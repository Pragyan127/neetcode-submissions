# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy
        # Create gap of n+1
        for i in range(n+1):
            ahead = ahead.next
        # Move together until ahead hits end
        while ahead:
            behind = behind.next
            ahead = ahead.next
            
         # Skip nth node from end
        behind.next = behind.next.next

        return dummy.next
