"""
    Given two polynomial numbers represented by a linked list. The task is to
    complete the  function addPolynomial() that adds these lists meaning adds
    the coefficients who have same variable powers.

    User Task:
    he task is to complete the function addPolynomial() which should add the
    polynomial with same powers.
"""
def addPolynomial(poly1, poly2):
    curr1 = poly1
    curr2 = poly2
    
    head = node(-1, -1)
    tail = head
    
    while curr1 and curr2:
        if curr1.power == curr2.power:
            tail.next = node(curr1.coef + curr2.coef, curr1.power)
            tail = tail.next
            
            curr1 = curr1.next
            curr2 = curr2.next
        elif curr1.power < curr2.power:
            tail.next = node(curr2.coef, curr2.power)
            tail = tail.next
            curr2 = curr2.next
        else:
            tail.next = node(curr1.coef, curr1.power)
            tail = tail.next
            curr1 = curr1.next
    
    while curr2:
        tail.next = node(curr2.coef, curr2.power)
        tail = tail.next
        curr2 = curr2.next
    
    while curr1:
        tail.next = node(curr1.coef, curr1.power)
        tail = tail.next
        curr1 = curr1.next
    
    head = head.next
    
    while head:
        end_str = " + " if head.next else ""
        print(str(head.coef) + "x^" + str(head.power), end=end_str)
        head = head.next
    
    print()