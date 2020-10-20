# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Find mid
        slow = head
        fast = head
        while fast !=None:
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        #reverse second half of linked list - using mid found above
        temp = slow
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        
        # compare values of linked list - 1 (head) and other reversed one (slow)
        head1 = head
        head2 = prev
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        if not head1 or not head2:
            return True
            
# Other optimization would be to reverse first half of linked list while we are trying to find mid. Thats most optimal solution possible.