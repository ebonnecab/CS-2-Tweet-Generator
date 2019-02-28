#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        # O(1) only needs to check head for whether the list is empty or not
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: Best and worst case are O(n) because we need to loop through all the nodes to get each item and find the length of the list.
        """
        node = self.head # O(1) time to assign new variable
        count = 0 
        #Loops through all nodes and count one for each
        while node is not None: #always n iterations
            count += 1
            node = node.next # O(1) time to reassign variable
        return count #  O(1) time to return list
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(n) because we need to loop through all the nodes to get to end of list if you start at the head and loop"""
        # TODO: Create new node to hold given item
        new_node = Node(item) # O(1) because 
        # checking if list is empty, if so make new node the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            current_node = self.head
        # if list is not empty continue to traverse

        #TO DO: start at tail instead of looping through whole list; makes the code O(1)
            while current_node.next is not None:
                current_node = current_node.next
                
        # if tail, add new node
            current_node.next = new_node
        # set previous pointer to current node
            new_node.prev = current_node
        # sets new tail to equal new node
            self.tail = new_node
             


    def prepend(self, item):
        # """Insert the given item at the head of this linked list.
        #Best and worse case runtime is O(1) because we only change the first node
        #Create new node to hold given item
        new_node = Node(item) # O(1)  time to assign new variable
        #Check if list is empty, if so make new node head and tail
        if self.head is None: # O(1) because it only checks if head is empty or not
            self.head = new_node
            self.tail = new_node
            return
        else:
            current_node = self.head
            #set head and prev pointer to new node
            self.head = new_node
            current_node.prev = new_node
            #next pointer points you back to head
            new_node.next = current_node
        


    def find(self, quality):
        # Return an item from this linked list satisfying the given quality.
        # Best case running time: O(1) if item is near the head of the list.
        # Worst case running time: O(n) if item is near the tail of the list 
        # or not in the list and we have to loop till the end.
        current_node = self.head #constant time to assign variable
       
        # loops through nodes to find if quality(item) is True
        #Checks if node's data satisfies given quality function
        while current_node is not None: #up to n iterations
            if quality(current_node.data): #constant time to call function
                return current_node.data #constant time to return data
            else:
                current_node = current_node.next # constant time to reassign variable
        return None # constant time to return None
    def delete(self, item):
        # Delete the given item from this linked list, or raise ValueError.
        # Best and worst run times are O(n) because you have to loop through the nodes
        extra_node = Node(item) #runtime is 0(1) to assign new variable
        current_node = self.head
        prev_node = None
        found = False
    #Loop through all nodes to find one whose data matches given item
        while current_node is not None: #up to n iterations
            if current_node.data == item: # O(1) time to call function
                found = True
    #Update previous node to skip around node with matching data
                if prev_node is not None:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                
                if current_node.next == None:
                    self.tail = prev_node
                
            
            prev_node = current_node
            current_node = current_node.next

        #Otherwise raise error to tell user that delete has failed
        if not found:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
