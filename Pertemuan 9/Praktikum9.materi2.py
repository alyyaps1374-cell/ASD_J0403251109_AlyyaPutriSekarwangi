#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 2: Binary Tree Sederhana
# ==========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")
 
#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Membuat child level 3
root.right.left = Node("F")
root.right.right = Node("G")

#Menampilkan isi node
print("Data pada root:", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)
print("Child kiri dari C:", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)

#Penjelasan:
# Secara konsep, setelah menetapkan simpul akar (root) bernilai "A", kode ini mulai
# membangun percabangan ke bawah dengan menambahkan "B" sebagai anak kiri dan "C" sebagai
# anak kanan. Selanjutnya, struktur diperluas lagi dengan menambahkan "D" dan "E" sebagai
# cabang dari simpul "B", serta "F" dan "G" sebagai cabang dari simpul "C". Rangkaian perintah
# print di bagian akhir berfungsi untuk memvalidasi struktur tersebut, memastikan bahwa ketujuh
# data telah terhubung dengan benar dan membentuk sebuah pohon biner utuh yang memiliki kedalaman dua tingkat di bawah root.