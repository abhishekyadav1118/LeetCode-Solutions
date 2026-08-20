# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         # self.val = val
#         # self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node, no swap needed
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Recurse for the remaining list and connect it to the first node
        first_node.next = self.swapPairs(second_node.next)

        # Swap the pair by pointing the second node to the first node
        second_node.next = first_node

        # The second node is now the new head of this swapped pair
        return second_node
