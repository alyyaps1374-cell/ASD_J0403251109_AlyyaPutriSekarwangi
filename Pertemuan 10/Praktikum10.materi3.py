#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 3: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    # y menjadi root baru
    return y        

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

# PENJELASAN:
# Kode ini adalah perbaikan Binary Search Tree (BST) 
# yang condong ke kanan (10 -> 20 -> 30) menggunakan algoritma rotasi kiri. 
# Fungsi rotate_left menyeimbangkan struktur ini dengan menjadikan node 20 
# sebagai root utama yang baru. Lalu, root lama (10) bergeser turun menjadi 
# child kiri dari 20, sementara node 30 tetap pada posisinya sebagai child kanan. 
# Terakhir, fungsi preorder dan tampil_struktur digunakan untuk menampilkan dan 
# membuktikan perubahan bentuk pohon dari yang awalnya miring memanjang menjadi seimbang secara visual.