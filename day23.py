# Rotate Linked List Right by K Positions

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def rotateRight(self, head, k):

        # Empty list or single node
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce k
        k = k % length

        if k == 0:
            return head

        # Make circular linked list
        tail.next = head

        # Find new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head


# Create Linked List
def create_linked_list(values):
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Print Linked List
def print_linked_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# User Input
numbers = list(map(int, input("Enter linked list elements: ").split()))
k = int(input("Enter k value: "))

# Create list
head = create_linked_list(numbers)

# Rotate list
solution = Solution()
rotated_head = solution.rotateRight(head, k)

# Output
print("Rotated Linked List:")
print_linked_list(rotated_head)
#userinput
# Enter linked list elements: 1 2 3 4 5
# Enter k value: 2
# Rotated Linked List:
# [4, 5, 1, 2, 3]