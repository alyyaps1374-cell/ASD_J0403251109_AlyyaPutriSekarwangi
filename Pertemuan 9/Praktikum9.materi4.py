#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 4: Membuat Traversal Inorder
# ==========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi inorder : left => Root => right
def inorder(node):
    if node is not None:
        inorder(node.left)  #kiri
        print(node.data, end=" ")    #root
        inorder(node.right)         #kanan

#membuat tree
#membuat sebuah node root
root = Node("A")
 
#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal inorder
print("Hasil Traversal Inorder: ")
inorder(root)

# Penjelasan:
# Secara konsep, aturan pembacaan inorder memiliki urutan penelusuran yang spesifik yaitu
# selesaikan cabang sebelah kiri hingga ujung paling bawah terlebih dahulu (left), kemudian
# kunjungi simpul induknya (root), dan terakhir telusuri cabang sebelah kanan (right).
# Berdasarkan hierarki pohon yang dibangun dalam kode ini, program akan langsung menyelam
# ke ujung kiri untuk mencetak "D", naik untuk mencetak induknya yaitu "B", lalu bergeser ke
# kanan mencetak "E". Setelah seluruh sisi kiri selesai, program akan naik ke pucuk tertinggi
# untuk mencetak "A", dan diakhiri dengan melangkah ke cabang kanan untuk mencetak "C". Sehingga,
# jika dieksekusi, hasil penelusuran ini akan menampilkan pola urutan: D, B, E, A, C.