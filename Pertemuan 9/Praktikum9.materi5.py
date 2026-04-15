#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 5: Membuat Traversal Postorder
# ==========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi Postorder : left => right => root
def postorder(node):
    if node is not None:
        postorder(node.left)  #kiri
        postorder(node.right)  #kanan
        print(node.data, end=" ")  #root

#membuat tree
#membuat sebuah node root
root = Node("A")
 
#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal preorder
print("Hasil Traversal Postorder: ")
postorder(root)

# Penjelasan:
# Secara konsep, aturan pembacaan postorder berkebalikan dengan preorder,
# di mana urutannya adalah telusuri cabang sebelah kiri hingga ujung (left),
# kemudian telusuri cabang sebelah kanan (right), dan terakhir barulah kunjungi
# simpul induknya (root). Berdasarkan struktur pohon pada kode ini, program
# akan menyelam ke ujung paling kiri untuk mencetak "D", lalu bergeser ke anak
# kanan dari cabang yang sama untuk mencetak "E", kemudian baru naik mencetak
# induknya yaitu "B". Setelah seluruh sisi kiri dari pohon utama diselesaikan,
# program akan beralih ke cabang kanan utama untuk mencetak "C", dan penelusuran
# diakhiri dengan mencetak simpul pucuk tertinggi yaitu "A". Sehingga, jika dijalankan,
# hasil akhir dari penelusuran ini akan menampilkan pola urutan: D, E, B, C, A.