#!/usr/bin/env python3

# A linked list is a linear data structure where each element is a separate object.
# Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node.
# The last node has a reference to null.
# The entry point into a linked list is called the head of the list.

class Node:
    '''A node in linked list'''
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        '''Initilize a new linked list'''
        self.head = None

    def __repr__(self):
        '''Return a string representation of the list'''
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return f'[{", ".join(nodes)}]'

    def lenght(self):
        '''Return list lenght'''
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def prepend(self, data):
        '''Insert a new element at the beginning of the list'''
        self.head = Node(data=data, next=self.head)

    def append(self, data):
        '''Insert a new element at the end of the list'''
        if not self.head:
            self.head = Node(data=data)
            return
        # Set curr to the beginning of the list
        curr = self.head
        # Traverse the list until the are no more "next"
        while curr.next:
            curr = curr.next
        # Set the current next for the last element of the list with the new node
        curr.next = Node(data=data)

    def insertAfterKey(self, key, data):
        '''Insert a new element after a 'key' matching element'''
        curr = self.head
        while curr.data != key:
            if curr.next:
                curr = curr.next
            else:
                return f'{key} not found in list'
        next_node = curr.next
        curr.next = Node(data=data, next=next_node)
        return

    def insertBeforeKey(self, key, data):
        '''Insert a new element before a 'key' matching element'''
        curr = self.head
        prev = None
        # Loop until you find the matching key
        while curr.data != key:
            # If the current element has a pointer to a next one 
            # keep track of the curr in prev variable
            # and then increment curr
            if curr.next:
                prev = curr
                curr = curr.next
            else:
                return f'{key} not found in list'
        # If you are here that means the current element is the one you are looking for
        # so that set the prev next to point to the new node with data=data and pointer to the current node
        prev.next = Node(data=data, next=curr)
        return

    def find(self, key):
        '''Search for the first element with 'data' matching 'key'. Return the element or 'None' if not found'''
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        '''Remove the first occurrence of 'key' in the list'''
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        '''Reverse the list in-place'''
        # Set curr at the first element of the list
        curr = self.head
        # Initialize variables
        prev_node = None
        next_node = None
        # Traverse the list
        while curr:
            # Set the next element in the next_node var
            next_node = curr.next
            # Set the next element to the value of prev_node
            curr.next = prev_node
            # Set prev_node to the current element
            prev_node = curr
            # Set the curr with the value in next_node
            curr = next_node
        self.head = prev_node


# Main
# Instantiate the list
lst = LinkedList()

# Append elements to the list
for x in 'five', 'seven':
    print(f'Appending {x} to list')
    lst.append(x)

# Prepend elements to the list
for x in 'four', 'two', 'one':
    print(f'Prepending {x} to list')
    lst.prepend(x)

# Print list length and list
print(f'List lenght: {lst.lenght()}')
print(f'List content:{lst}')

# Remove element from list
print('Remove element "two" from the list')
lst.remove('two')
print(f'List lenght: {lst.lenght()}')
print(f'List content:{lst}')

# Find element in the list
print('Looking for element "five" in the list')
print(lst.find('five'))


# Insert new element in after an existing element
print('Insert element "six" afer element "five"')
lst.insertAfterKey('five', 'six')
print(f'List content:{lst}')

# Insert another new element after and existing element
print('Insert element "ten" afer element "seven"')
lst.insertAfterKey('seven', 'ten')
print(f'List content:{lst}')

# Insert another new element before and existing one
print('Insert element "three" before element "four"')
lst.insertBeforeKey('four', 'three')
print(f'List content:{lst}')

# Insert another new element before and existing one
print('Insert element "nine" before element "ten"')
lst.insertBeforeKey('ten', 'nine')
print(f'List content:{lst}')

# Reverse list
print('Reverse the list')
lst.reverse()
print(f'List content:{lst}')
