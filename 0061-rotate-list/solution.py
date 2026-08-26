# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list or single node
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute length and find tail
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        # Step 2: Calculate effective steps
        k = k % length
        if k == 0:
            return head

        # Step 3: Make the list circular
        last.next = head

        # Step 4: Traverse to the new tail node
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 5: Break the circle and set new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
