class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None


    def printlist(self):
        print("Printing List")
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


    def inserthead(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def insert(self, middle_node, node):
        if middle_node is None:
            print("Node doesn't exist")
            return
        
        new_nodes_next = middle_node.next
        middle_node.next = node
        node.next = new_nodes_next

# Function to remove node
    def remove(self, rem_key):
        #removing at head
        head = self.head
        if head.data == rem_key:
            self.head = head.next
            return

        # remove from rest
        curr = self.head
        while curr.next.data != rem_key:
            curr = curr.next
            if curr.next == None:
                break
        if (curr.next.data == rem_key):
            curr.next = curr.next.next
            return


list1 = SLinkedList()
list1.head = Node("Zuby")
second = Node("Sammy")
third = Node("Aneeb")
list1.head.next = second
second.next = third
# list1.printlist()

list1.inserthead(Node("Moby"))
# list1.printlist()

list1.insert_tail(Node("Munir"))
list1.inserthead(Node("Saima"))

list1.insert(third, Node("Mummy"))
list1.printlist()

list1.remove("Zuby")
list1.printlist()

list1.remove("Saima")
list1.printlist()

