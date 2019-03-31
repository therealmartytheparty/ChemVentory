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

    def remove(self, value):
        temp = self.head

        while temp is not None:
            if temp.chem.name == value:
                # item is in the middle
                if (temp.prev is not None) and (temp.next is not None):
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                # item is head
                elif temp.prev is None:
                    self.head = temp.next
                    temp.next.prev = None
                # item is tail
                else:
                    self.tail = temp.prev
                    temp.prev.next = None

            temp = temp.next

    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.chem.name == value:
                print(temp.chem.name + ' was found')

            temp = temp.next
