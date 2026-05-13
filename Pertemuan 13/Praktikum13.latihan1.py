#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Pertanyaan Analisis
# 1. Apa perbedaan graph awal dan spanning tree?
# Graph awal memiliki cycle sedangkan spanning tree tidak
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Karena akan menyebabkan penggunaan edge berlebih, meningkatjan biaya total, dan
# akan membuat koneksi tidak efisien.
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Karena spanning tree tidak berbentuk cycle (menghindari cycle), artinya
# akan ada egde yang dihapus atau dihilangkan untuk memutus cycle tersebut.