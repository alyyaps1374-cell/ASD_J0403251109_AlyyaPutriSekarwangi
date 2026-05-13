#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==================================================================
# Praktikum 13: Buat Program MST dengan Kasus Baru
# ==================================================================

# Representasi weighted graph
# Format data: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_bobot = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
for bobot, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, bobot))
        total_bobot += bobot

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot minimum
print("Total bobot minimum =", total_bobot)

# Pertanyaan Analisis:
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# Kasus yang dipilih adalah jaringan jalan antar kota
# 2. Algoritma apa yang digunakan?
# Algoritma Kruskal
# 3. Edge mana saja yang dipilih dalam MST?
# Edge yang dipilih: 
# 'Bogor' - 'Depok'
# 'Depok' -  'Jakarta'
# 'Depok' - 'Bandung'
# 4. Berapa total bobot MST?
# Total bobot minimum adalah 9
# 5. Mengapa edge tertentu tidak dipilih?
# Karena sudah ada jalur lain dengan bobot lebih kecil
# untuk menghubungkan semua kota. Selain itu, pemilihan
# edge tersebut dapat membuat cycle dan menyebabkan total bobot menjadi lebih besar.