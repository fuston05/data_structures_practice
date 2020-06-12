class Node:
    def __init__(self, value, next= None):
        self.value= value
        self.next= next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, newNext):
        self.next= newNext

class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

    # Adds `data` to the end of the LinkedList 
    # O(1) because this operation doesn't depend on the size of the linked list 
    def add_to_tail(self, data):
        # create new tail node
        newNode= Node(data)
        newNode.next= None

        # if this is the 1st and only node
        if not self.tail:
            self.tail= self.head= newNode
        # head and tail already exist
        else:
            prevTail= self.tail
            prevTail.set_next(newNode)

    def add_to_head(self, data):
        pass

    def remove_tail(self):
        pass

    def remove_head(self):
        pass

    def contains(self, data):
        pass

    def get_max(self):
        pass

