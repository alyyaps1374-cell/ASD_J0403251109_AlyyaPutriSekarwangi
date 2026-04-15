#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 6: Struktur Organisasi Perusahaan
# ==========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat tree struktur organisasi
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

#Fungsi preorder : Root => left => right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")  #root
        preorder(node.left)       #kiri
        preorder(node.right)      #kanan

#menjalankan traversal preorder
print("Struktur Organisasi (Preorder): ")
preorder(root)


# Penjelasan:
# Kode ini merupakan contoh penerapan struktur data Binary
# Tree pada studi kasus nyata, yaitu untuk memodelkan hierarki
# struktur organisasi. Pohon biner dibangun dengan "Direktur" sebagai
# simpul akar (root), yang memiliki bawahan "Manajer A" di cabang kiri
# dan "Manajer B" di cabang kanan. Struktur ini kemudian dilanjutkan ke
# level staf di bawah masing-masing manajer. Selanjutnya, kode menggunakan
# metode Preorder Traversal (Akar → Kiri → Kanan) untuk membaca urutan hierarki
# tersebut. Sesuai aturannya, penelusuran akan dimulai dari pimpinan tertinggi,
# kemudian menyelami seluruh divisi sebelah kiri beserta jajaran stafnya hingga
# selesai, sebelum akhirnya berpindah untuk membaca divisi sebelah kanan. Jika
# dieksekusi, program akan menghasilkan urutan pembacaan struktur: Direktur,
# Manajer A, Staff 1, Staff 2, Manajer B, Staff 3.