# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        stack = [] 
        prev = None
        while head != None:
            data = ListNode()
            data.val = head.val
            data.next = prev
            
            stack.append(data)
            
            prev = data
            head = head.next
            
        if stack:
            return stack.pop()
    
        return head
        