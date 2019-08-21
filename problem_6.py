class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            return

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def llist_to_set(self):
        linked_list_set = set()
        node = self.head
        while node:
            linked_list_set.add(node.value)
            node = node.next
        return linked_list_set

def union(llist_1, llist_2):
    # Previous solution
    # union_set = llist_1.llist_to_set().union(llist_2.llist_to_set())
    union_llist = LinkedList()
    elements = set()
    head = llist_1.head
    while head != None:
        if head.value not in elements:
            elements.add(head.value)
            union_llist.append(head.value)
        head = head.next
    
    head = llist_2.head
    while head != None:
        if head.value not in elements:
            elements.add(head.value)
            union_llist.append(head.value)
        head = head.next
    
    return union_llist

def intersection(llist_1, llist_2):
    # Previous solution
    # intersection_set = llist_1.llist_to_set().intersection(llist_2.llist_to_set())
    intersection_llist = LinkedList()
    elements = set()
    head = llist_1.head
    while head != None:
        if head.value not in elements:
            elements.add(head.value)
        head = head.next

    head = llist_2.head

    while head != None:
        if head.value in elements:
            elements.discard(head.value)
            intersection_llist.append(head.value)
        head = head.next
    return intersection_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2).__str__())
print (intersection(linked_list_1,linked_list_2).__str__())

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4).__str__())
print (intersection(linked_list_3,linked_list_4).__str__())

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [2]
element_6 = [1, 2, 3, 4]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6).__str__())
print (intersection(linked_list_5,linked_list_6).__str__())