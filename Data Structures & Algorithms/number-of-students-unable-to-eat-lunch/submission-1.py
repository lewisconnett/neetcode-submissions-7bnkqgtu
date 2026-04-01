class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if not students:
            return 0

        head = Node(students[0])
        curr = head
        queue_len = len(students)

        for student in students[1:]:
            curr.next = Node(student)
            curr = curr.next
        
        tail = curr

        rotations = 0

        while sandwiches and rotations < queue_len:
            if head.val == sandwiches[0]:
                sandwiches.pop(0)
                head = head.next
                queue_len -= 1
                rotations = 0
            else:
                temp_next = head.next
                tail.next = head
                tail = tail.next
                head = temp_next
                rotations += 1
        
        return queue_len

            



        

