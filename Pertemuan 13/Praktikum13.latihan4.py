#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==================================================================
# Praktikum 13: Studi Kasus: Jaringan Kabel Antar Gedung
# ==================================================================

# ==========================================================
# Program Minimum Spanning Tree menggunakan Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_biaya = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses pemilihan edge
for biaya, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, biaya))
        total_biaya += biaya

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_biaya)

# Pertanyaan Analisis:
# 1. Algoritma apa yang digunakan?
# Algoritma Kruskal
# 2. Edge mana saja yang dipilih?
# Edge yang dipilih adalah:
# GedungC - GedungD = 1
# GedungA - GedungC = 2
# GedungB - GedungD = 3
# 3. Berapa total biaya minimum?
# Total biaya minimum adalah 6
# 4. Mengapa MST cocok digunakan pada kasus ini?
# Karena tujuan kasus ini adalah menghubungkan seluruh 
# gedung dengan biaya pemasangan kabel seminimal mungkin tanpa
# membuat jalur yang tidak diperlukan. Dengan MST, semua 
# gedung tetap terhubung tetapi total biaya menjadi paling efisien.