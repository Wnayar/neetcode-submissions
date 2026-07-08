# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # time compelxity O(n), space complexity O(n)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if list empty terminate 
        if head == None:
            return head 

        ref = head 
        # list of pointers 
        l= []
        while ref != None:
            l.append(ref)
            ref = ref.next 
        
        i, j = 0, len(l) - 1
        even = len(l) % 2 == 0

        while True: 
            l[i].next = l[j]

            # even terminate condition 
            if j == i + 1 and even:
                l[j].next = None
                return 
            # odd terminate condtion 
            if j == i and not even:
                l[i].next = None
                return     

            l[j].next = l[i + 1]
            i += 1
            j -= 1
            

        

