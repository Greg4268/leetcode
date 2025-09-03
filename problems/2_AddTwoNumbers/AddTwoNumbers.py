# Definition for singly-linked list.
# public class ListNode {
#     int val;
#     ListNode next;
#     ListNode() {}
#     ListNode(int val) { this.val = val; }
#     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
# }

l1 = [4,5,2]
l2 = [6,1,3]
# 254 + 316 = 570
correct_answer = [5,7,0]

def Solution1(l1, l2) -> []:
    dummy = ListNode() 
    ans = dummy
    total = carry = 0 

    while l1 or l2 or carry: 
        total = carry 

        if l1: 
            total += l1.val 
            l1 = l1.next 
        if l2: 
            total += l2.val 
            l2 = l2.next 

        sums = total % 10 
        carry = total // 10 
        dummy.next = ListNode(sums) 
        dummy = dummy.next 

    if carry > 0: 
        dummy.next = ListNode(carry) 
    
    return ans.next

    

if __name__ == "__main__":
    print(Solution1(l1,l2))