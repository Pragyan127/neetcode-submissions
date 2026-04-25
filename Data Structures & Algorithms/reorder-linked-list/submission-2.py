# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        #find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #split 
        curr = slow.next
        prev = slow.next = None

        #reverse second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #merge
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
