class Solution {
    public ListNode removeElements(ListNode head, int val) {

        // Remove matching nodes from the beginning
        while (head != null && head.val == val) {
            head = head.next;
        }

        // Traverse the remaining list
        ListNode current = head;

        while (current != null && current.next != null) {

            if (current.next.val == val) {
                // Skip the node
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}