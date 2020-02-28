""" Class Node for linked list """


class Node():
    """ class Node for single linked list """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter method for "data" atribut    q224e """
        return self.__data

    @data.setter
    def data(self, data):
        """ setter method for "data" atribute """
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node


class SinglyLinkedList():
    """ Class SinglyLinkedList """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ tmp temporal node """
        tmp = self.__head
        if tmp == None:
            self.__head = Node(data=value)
        else:
            tmp = self.__head
            prev = tmp
            while tmp.next_node and tmp.data <= value:
                prev = tmp
                tmp = tmp.next_node
            if tmp.next_node == None and tmp.data <= value:
                prev.next_node = Node(data=value)
            else:
                self.__insert(prev, value)

    def __insert(self, prev, value):
        """  """
        tmp = prev.next_node
        new = Node(data=value)
        prev.next_node(new)
        new.next_node(tmp)

    def __str__(self):
        data = ""
        tmp = self.__head
        while tmp.next_node:
            data += "{}\n".format(tmp.data)
            tmp = tmp.next_node
        data += "{}".format(tmp.data)
        return data



if __name__ == "__main__":
    #!/usr/bin/python3

    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)

