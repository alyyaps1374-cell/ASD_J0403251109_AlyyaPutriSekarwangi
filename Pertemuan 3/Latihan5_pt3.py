class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # head lama jadi tail baru

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  # prev jadi head baru
        self.display()

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

print("Linked list sebelum dibalik:", end=" ")
ll.display()
print("Linked link setelah dibalik:", end=" ")
ll.reverse()