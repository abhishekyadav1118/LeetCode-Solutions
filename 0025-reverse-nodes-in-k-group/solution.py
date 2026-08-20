# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 1. Check if there are k nodes left
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # 2. Reverse the k group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 3. Fix the outer connections
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
