#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Materi 1: Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
 (1, 'C', 'D'),
 (2, 'A', 'C'),
 (3, 'B', 'D'),
 (4, 'A', 'B'),
 (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()

mst = []
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected = set()

for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

#Penjelasan Alur:
#Pertama-tama kode ini mendefinisikan daftar sisi graf beserta bobotnya, 
# lalu mengurutkannya dari bobot terkecil menggunakan fungsi edges.sort().
# Setelah itu, program melakukan iterasi pada sisi-sisi yang sudah terurut
# dan menggunakan sebuah himpunan (set) bernama connected untuk melacak
# simpul (node) yang sudah dikunjungi guna mencegah terbentuknya siklus (cycle).
# Jika salah satu atau kedua simpul dari sebuah sisi belum ada di dalam himpunan
# connected, sisi tersebut dianggap aman lalu ditambahkan ke dalam daftar mst,
# nilai bobotnya diakumulasikan ke variabel total_weight, dan kedua simpul
# penyusunnya ditandai sebagai sudah terhubung dengan dimasukkan ke himpunan
# connected. Pada bagian akhir, program menampilkan daftar sisi yang terpilih
# sebagai jalur MST beserta total bobot keseluruhannya.
