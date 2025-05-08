import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


# time complexity O(n), space complexity O(n)
def isHealthRecordSymmetric(head) -> bool:
    
    # early exit for empty list
    if head is None:
        return False
    
    # early exit for single element in a list
    if head and head.next is None:
        return False

    fast, slow = head, head
    stack = []

    #find the middle of the linked list
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # slow pointer points to the middle now

    # check if list is odd to decide if we need to increment slow by one
    if fast:
        slow = slow.next
    
    # now compare the stack to remaining elements in the list
    while slow:
        if stack.pop() != slow.value:
            return False
        slow = slow.next

    # reached end of list with all comparisons matching
    return True


class TestLinkedList(unittest.TestCase):

    def test_single(self):
        single_list = LinkedList()
        single_list.append(1)
        self.assertFalse(isHealthRecordSymmetric(single_list.head))
    
    
    def test_double_symmetric(self):
        double_list = LinkedList()
        double_list.append(1)
        double_list.append(1)
        self.assertTrue(isHealthRecordSymmetric(double_list.head))
    
    
    def test_empty(self):
        empty_list = LinkedList()
        self.assertFalse(isHealthRecordSymmetric(empty_list.head))
    
    
    def test_odd(self):
        odd_list = LinkedList()
        odd_list.append(0)
        odd_list.append(1)
        odd_list.append(0)
        self.assertTrue(isHealthRecordSymmetric(odd_list.head))
    
    
    def test_even_asymmetric(self):
        even_asymmetric_list = LinkedList()
        even_asymmetric_list.append(0)
        even_asymmetric_list.append(1)
        even_asymmetric_list.append(0)
        even_asymmetric_list.append(0)
        self.assertFalse(isHealthRecordSymmetric(even_asymmetric_list.head))

if __name__ == "__main__":
    unittest.main()