class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        
        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if not sorted_list or new_node.value < sorted_list.value:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            current = sorted_list
            while current.next and current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_list

    def merge_two_sorted_lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next

# Приклади використання
list1 = LinkedList()
list1.append(4)
list1.append(3)
list1.append(1)
list1.append(2)

print("Оригінальний список 1:")
list1.print_list()

list1.reverse()
print("Реверсований список 1:")
list1.print_list()

list1.insertion_sort()
print("Відсортований список 1:")
list1.print_list()

list2 = LinkedList()
list2.append(5)
list2.append(6)
list2.append(3)
list2.append(7)

list2.insertion_sort()
print("Відсортований список 2:")
list2.print_list()

merged_list = LinkedList()
merged_list.head = list1.merge_two_sorted_lists(list1.head, list2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()
