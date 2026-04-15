#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 3: Membuat Traversal Preorder
# ==========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi preorder : Root => left => right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")  #root
        preorder(node.left)       #kiri
        preorder(node.right)      #kanan

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
print("Hasil Traversal Preorder: ")
preorder(root)


#penjelasan:
# Secara konsep, preorder memiliki aturan pembacaan simpul yang sangat khas,
# yaitu dengan urutan: kunjungi simpul saat ini (root), lalu telusuri seluruh
# cabang kiri hingga ujung (left), dan terakhir telusuri cabang kanan (right).
# Berdasarkan struktur pohon yang dibuat dalam kode ini, penelusuran akan
# dimulai dengan mencetak pucuk utama "A", kemudian program akan bergerak ke bawah
# untuk menyelesaikan seluruh rantai di cabang kiri terlebih dahulu (mencetak "B",
# turun lagi mencetak "D", lalu ke sebelahnya mencetak "E"), dan setelah sebelah kiri
# habis, barulah berpindah untuk membaca cabang bagian kanan (mencetak "C"). Sehingga,
# jika dijalankan, urutan data yang dihasilkan akan menampilkan pola: A, B, D, E, C.