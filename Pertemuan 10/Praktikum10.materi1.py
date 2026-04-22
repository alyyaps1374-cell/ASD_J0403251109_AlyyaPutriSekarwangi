#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 1: BST
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

#Mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

# LATIHAN 2: Traversal Inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Hasil inorder:")
inorder(root)

# LATIHAN 3: Search BST
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
# Uji pencarian
key = 10

if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")



# PENJELASAN:
# Pertama, program membangun struktur "pohon" dari sebuah daftar angka menggunakan
# fungsi insert. Angka yang lebih kecil selalu dilempar ke cabang kiri,
# sedangkan yang lebih besar ditaruh di cabang kanan. Setelah pohonnya terbentuk, fungsi
# inorder membaca seluruh isinya dengan cara menyisir dari dahan paling kiri, lalu ke tengah,
# baru ke kanan. Efeknya, hasil yang tercetak otomatis berurutan dari angka terkecil hingga terbesar.
# Terakhir, fungsi search mencoba melacak keberadaan angka 10 dengan menelusuri cabang pohon dari
# pucuk paling atas. Karena program terus turun ke cabang kiri dan tetap tidak menemukan angka
# 10 sampai jalurnya buntu, akhirnya dicetak pesan bahwa datanya tidak ditemukan.