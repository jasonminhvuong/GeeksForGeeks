"""
    Given a Linked List of integers, write a function to modify the linked list
    such that all even numbers appear before all the odd numbers in the
    modified linked list. Also, keep the order of even and odd numbers same.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases.
    The first line of each test case is N,N is the number of elements in Linked
    List.
    The second line of each test case contains N input,elements in Linked List.

    Output:
    Print the all even numbers then odd numbers in the modified Linked List.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        if not head:
            return None
        
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        curr = head
        
        while curr:
            if curr.data % 2 == 1:
                if not odd_head:
                    odd_head = curr
                    odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = curr
            else:
                if not even_head:
                    even_head = curr
                    even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = curr
             
            temp = curr.next
            curr.next = None
            curr = temp
            
        if even_head:
            even_tail.next = odd_head
            return even_head
        else:
            return odd_head
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        head = Node(arr[0])
        curr = head
        for i in range(1, n):
            curr.next = Node(arr[i])
            curr = curr.next
        
        curr = sol.segregate(head)
        
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
                
        
        print()

if __name__ == "__main__":
    main()