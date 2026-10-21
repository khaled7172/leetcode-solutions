# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        get_size = 0
        slice_start = 0
        curr_idx = 0
        curr = head
        if (curr == None):
            return
        while(curr):
            get_size += 1
            curr = curr.next
        curr = head
        slice_start = int(get_size / 2)
        while curr and curr_idx < slice_start:
            curr = curr.next
            curr_idx += 1
        return curr


        