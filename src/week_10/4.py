class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_kth_from_end(self, k=None):
        if self.head is None:
            return

        list_len = 1

        current = self.head
        while current.next:
            list_len += 1
            current = current.next
        if k is None:
            k = list_len
        node_index_from_head = list_len - k
        #print(k, node_index_from_head, list_len)
        if node_index_from_head >= list_len:
            return
        if node_index_from_head < 0:
            return
        if node_index_from_head == 0:
            self.head = self.head.next
            return

        current_index = 0
        current_node = self.head
        before_node = None
        del_node = None

        while current_node.next:
            #print('curr', current_index)
            if current_index == node_index_from_head - 1:
                #print('before', current_index)
                before_node = current_node
            if current_index == node_index_from_head:
                #print('del node', current_index)
                del_node = current_node

            current_index += 1
            current_node = current_node.next

        if node_index_from_head+1 != list_len:
            before_node.next = del_node.next
        else:
            before_node.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(2)
linked_list.append(1)
linked_list.append(1)



# Полученный список:
linked_list.print_list()  # Вывод: 1 -> 2 -> 3 -> 4 -> 5 -> None

linked_list.delete_kth_from_end(3)  # Удаляем 2-ой узел с конца (4)

# Список после удаления 2-го узла с конца:
linked_list.print_list()  # Вывод: 1 -> 2 -> 3 -> 5 -> None
