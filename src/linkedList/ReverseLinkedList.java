package linkedList;

public class ReverseLinkedList {
    class ListNode{
        int val;
        ListNode next;
        ListNode(){}
        ListNode(int val){ this.val = val ;}
        ListNode(int val, ListNode next){
            this.val = val;
            this.next = next;
        }
    }
    class IterativeSolution{
        public ListNode reverseList(ListNode head){
            ListNode prev = null;
            ListNode reverseL = null;
            ListNode curr = head;
            while (curr != null) {
                prev = reverseL;
                reverseL = curr;
                curr = curr.next;
                reverseL.next = prev;
            }
            return reverseL;
        }
    }
    // Recursive Solution
    class RecursiveSolution{
        public ListNode reverseList(ListNode head){
            return recursive(head,null);
        }
        public ListNode recursive(ListNode node, ListNode previous){
            if(node == null) return previous;
            ListNode temp = node.next;
            node.next = previous;
            return recursive(temp,node);
        }
    }
}