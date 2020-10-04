class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Create head node
        head = ListNode()
        main_head = head
        
        # Until both pointers for l1 and l2 are not None
        # Compare l1 and l2:
            # if l1 is smaller:    Add l1 to head.next
            # if l2 is smaller:    Add l2 to head.next
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        # Below is for cases where len(l1) and len(l2) are different
        
        # Add remaining elements of l1 (if any) to head
        while l1:
            head.next = l1
            head = head.next
            l1 = l1.next
            
        # Add remaining elements of l2 (if any) to head
        while l2:
            head.next = l2
            head = head.next
            l2 = l2.next
        return main_head.next