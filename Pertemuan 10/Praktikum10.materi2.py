#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 2: Membuat BST yang Tidak Seimbang
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


root = None
# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

# PENJELASAN:
# Kode ini membangun dan menampilkan struktur data Binary Search Tree (BST)
# menggunakan sekumpulan data yang diurutkan secara naik, yaitu 10, 20, dan 30. 
# Karena data dimasukkan dari nilai terkecil hingga terbesar, BST yang dihasilkan 
# menjadi tidak seimbang dan condong ke arah kanan. Dalam struktur ini, 
# angka 10 bertindak sebagai root, angka 20 menjadi child kanan dari 10, dan angka 30 
# menjadi child kanan dari 20. Setelah struktur pohon terbentuk, program memanggil fungsi 
# preorder untuk mencetak nilai node dengan urutan penelusuran root-kiri-kanan. Terakhir, 
# fungsi tampil_struktur dieksekusi untuk memvisualisasikan hierarki pohon tersebut, 
# yang akan secara jelas memperlihatkan bahwa semua node hanya memiliki percabangan ke arah kanan.