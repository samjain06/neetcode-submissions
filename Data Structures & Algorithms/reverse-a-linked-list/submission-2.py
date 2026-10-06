# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ITERATIVE SOLUTION
        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return prev

        # RECURSIVE SOLUTION
        

        def helper(head):
            # base case
            if not head:
                return None

            new_head = head

            # recursive case
            if head.next:
                new_head = helper(head.next)
                head.next.next = head
            head.next = None
            return new_head


        result = helper(head)
        return result