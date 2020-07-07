class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Adds `data` to the end of the LinkedList
    # O(1) because this operation doesn't depend on the size of the linked list
    def add_to_tail(self, data):
        # create new tail node
        newNode = Node(data)
        newNode.next = None

        # if this is the 1st and only node
        if not self.tail:
            self.tail = self.head = newNode
        # head and tail already exist
        else:
            prevTail = self.tail
            prevTail.set_next(newNode)
            self.tail = newNode

    def remove_tail(self):
      # if list is empty
        if self.tail is None:
            return None
        # set the node before tail's next pointer to 'None'
        # iterate and check 'next' until we find tail
        current = self.head
        prev = self.head

        while current.get_next():
            prev = current
            current = current.get_next()
        data = self.tail.get_value()
        self.tail = prev
        prev.set_next(None)
        return data

    def remove_head(self):
        # if list is empty
        if self.head is None:
            return None
        # if there's only one node
        if self.head.next is None:
            data = self.head.get_value()
            self.head = self.tail = None
        else:
            data = self.head.get_value()
            newHead = self.head.next
            self.head.next = None
            self.head = newHead
        return data

    # Traverses the linked list and returns a boolean indicating whether the
    # specified `data` is in the linked list.
    # What's the runtime for this method? O(n)
    def contains(self, data):
        isFound = False
        # if empty list
        if self.head is None:
            return False

        current = self.head

        # linear search O(n)
        while current:
            if current.get_value() == data:
                return True
            else:
                current = current.next

        return isFound

    #  Traverses the linked list, fetching the max value in the linked list
    # What is the runtime of this method? O(n)

    def get_max(self):
        if self.head is None:
          return None
        
        currentNode= self.head
        currentMax= 0

        # linear search= O(n)
        while currentNode:
          if currentNode.get_value() > currentMax:
            currentMax= currentNode.get_value()
          currentNode= currentNode.next
        return currentMax
