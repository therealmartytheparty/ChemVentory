class node:

    def __init__(self, obj, prevnode=None, nextnode=None):
        self.prev = prevnode
        self.chem = obj
        self.next = nextnode

class list:

    head = None
    tail = None

    def add(self, obj):
        newnode = node(obj)

        if self.head is None:
            self.head = self.tail = newnode
        else:
            newnode.prev = self.tail
            newnode.next = None
            self.tail.next = newnode
            self.tail = newnode

    def print(self):
        temp = self.head

        while temp is not None:
            print(temp.chem.name)

            temp = temp.next
