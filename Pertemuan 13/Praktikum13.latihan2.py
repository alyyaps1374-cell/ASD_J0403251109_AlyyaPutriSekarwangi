#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==================================================================
# Praktikum 13 - Graph III: Implementasi Sederhana Algoritma Kruskal
# ==================================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Pertanyaan Analisis 
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# Edge yang memiliki bobot paling kecil yaitu edge antara
# titik C dengan titik D, dengan bobot 1.
# 2.Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Karena tujuan algoritma Kruskal adalah menghasilkan Minimum Spanning
# Tree dengan total bobot seminimal mungkin. Dengan memilih edge terkecil 
# terlebih dahulu, algoritma dapat menghubungkan node-node menggunakan biaya
# paling rendah sebelum mempertimbangkan edge dengan bobot yang lebih besar. 
# Cara ini membantu memastikan total bobot akhir dari spanning tree menjadi 
# minimum selama edge yang dipilih tidak membentuk cycle.
# 3. Berapa total bobot MST yang dihasilkan?
# Total bobot yang akan dihasilkan adalah 6
# 4. Mengapa edge tertentu tidak dipilih?
# Edge yang tidak dipilih adalah edge yang akan membentuk cycle,
# hal ini dilakukan agar graph tetap terhubung secara efisien tanpa menghasilkan cycle.