#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 4: Rotasi Kanan pada BST Tidak Seimbang
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

# Fungsi rotasi kanan
def rotate_right(y):
    # y adalah root lama (dalam kasus ini 30)
    x = y.left # x adalah child kiri y (dalam kasus ini 20)
    T2 = x.right # subtree kanan milik x disimpan sementara

    # Proses rotasi
    x.right = y # y menjadi child kanan dari x
    y.left = T2 # child kiri y diganti dengan T2

    # x menjadi root baru
    return x        

# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10 (Left-Left)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)


# PENJELASAN:
# Kode ini adalah proses penyeimbangan struktur Binary Search Tree (BST)
# yang condong ke kiri (30 -> 20 -> 10) dengan menggunakan algoritma rotasi kanan. 
# Melalui fungsi rotate_right, keseimbangan pohon diperbaiki dengan cara 
# mengangkat node 20 menjadi root utama yang baru. Akibat rotasi tersebut, 
# root lama yaitu node 30 bergeser turun menjadi child kanan dari 20, sementara 
# node 10 tetap pada posisinya semula sebagai child kiri. Terakhir, fungsi preorder
# dan tampil_struktur digunakan untuk memvisualisasikan dan membuktikan perubahan 
# struktur pohon dari yang awalnya memanjang ke kiri menjadi seimbang.