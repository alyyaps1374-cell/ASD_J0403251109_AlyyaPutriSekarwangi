#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 1: Membuat Node Tree
# ==========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#Pembahasan :
# Kelas Node dalam kode itu merepresentasikan karakteristik utama dari pohon biner, di mana setiap simpul dirancang untuk menyimpan sebuah informasi atau data,
# sekaligus memiliki maksimal dua buah cabang untuk terhubung ke simpul di bawahnya (yaitu child kiri dan child kanan). Selanjutnya, pembuatan variabel root dengan
# nilai "A" mencerminkan pembuatan titik awal atau pucuk tertinggi dari pohon tersebut. Hasil eksekusi pada bagian akhir pada dasarnya membuktikan konsep awal pembentukan
# pohon, di mana simpul akar (root) yang baru lahir akan berdiri tunggal dengan nilai datanya, sementara kedua cabangnya masih berstatus kosong (None) karena belum ada simpul
# anak yang ditambahkan untuk membentuk hierarki ke bawah.