# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node to handle edge cases easily (like removing the head)
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # 2. Advance the fast pointer by n + 1 steps to create the gap
        for _ in range(n + 1):
            fast = fast.next

        # 3. Move both pointers together until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # 4. Skip the nth node from the end
        slow.next = slow.next.next

        # 5. Return the updated list head
        return dummy.next
