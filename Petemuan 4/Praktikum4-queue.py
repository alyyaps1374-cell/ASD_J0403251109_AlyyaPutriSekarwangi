#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

#=================================================
#Implementasi Dasar: Queue 
#=================================================

class Node:
    def __init__(self,data):
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke node berikutnya (awal=none)

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        #Menambah data di belakang (rear)
        nodeBaru = Node(data)

        #jika queue kosong, front and rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        #menghapus data dari depan

        # 1) ambil data yang paling depan
        data_terhapus = self.front.data

        # 2) geser front ke node berikutnya
        self.front = self.front.next

        # 3) Jika setelah geser front menjadi none, maka queue kosong
        #Rear juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus



    def tampilkan(self):
            #tampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")

#instantiasi objek class queueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()