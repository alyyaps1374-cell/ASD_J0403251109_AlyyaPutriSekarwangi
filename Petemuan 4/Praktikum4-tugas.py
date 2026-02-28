# ===========================================
# Nama: Alyya Putri Sekarwangi
# NIM: J0403251109
# Kelas: TPL B1

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node: #Mendefinisikan Node
    def __init__(self, no, nama, servis):
        self.no = no #Menyimpan nomor antrian
        self.nama = nama #Menyimpan nama pelanggan
        self.servis = servis #Menyimpan jenis servis
        self.next = None #Menyimpan ke node berikutnya

class QueueBengkel: #Mendefinisikan queue, terdiri atas front dan rear
    def is_empty(self):
        return self.front is None #Ketika queue kosong maka front = rear = none
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, no, nama, servis): #menambahkan data baru ke rear (belakang) => menambahkan data pelanggan baru
       #jika data ditambahkan ke queue yang kosong maka data baru = front = rear
       NodeBaru = Node(no,nama,servis)
       if self.is_empty():
          self.front = NodeBaru
          self.rear = NodeBaru
          return
       #jika queue tidak kosong maka data baru diletakkan setelah rear, dan dijadikan rear
       self.rear.next = NodeBaru
       self.rear = NodeBaru

    def dequeue(self): #menghapus data (melayani pelanggan)
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan untuk dilayani.")
            return None
       
       #simpan data di bagian front ke variabel data yang akan dihapus
        node_dilayani = self.front

       #geser pointer dari front ke next front
        self.front = self.front.next

       #jika front menjadi none (antrian terkahir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
       
    def tampilkan(self):
       print("Data Antrian Pelanggan Bengkel (Front => Rear): ")
       current = self.front
       no = 1
       while current is not None:
          print(f"{no}. {current.nama} - {current.servis}")
          current = current.next
          no += 1
       

def main(): #Program Utama
    q = QueueBengkel() #Instantiasi queue

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu(1-4): ")

        if pilih == "1":
            no = input("No Antrian : ").strip()
            nama = input("Nama : ").strip()
            servis = input("Servis : ").strip()
            q.enqueue(no, nama, servis)
            print("Data pelanggan berhasil ditambahkan")

        elif pilih == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Pelanggan Dilayani: {dilayani.no}. {dilayani.nama} - {dilayani.servis}")
        
        elif pilih == "3":
            q.tampilkan()
    
        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break
        
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()