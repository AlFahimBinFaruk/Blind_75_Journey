# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # Time O(N) | Space O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we gonna use slow and fast pointer to solve this.
        # the main concept is we gonna see if slow == fast if it match means there is a cycle.
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next    

            if slow == fast:
                return True

        return False      
