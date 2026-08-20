import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Dummy node helps easily manage the head of the merged list
        dummy = ListNode(0)
        curr = dummy

        heap = []

        # Put the head of each list into the min-heap
        # We include an index 'i' to prevent comparison errors between ListNodes when values are equal
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        # Process the heap until it is empty
        while heap:
            val, i, node = heapq.heappop(heap)

            # Append the smallest node to our result list
            curr.next = node
            curr = curr.next

            # If there is a next node in that specific list, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
