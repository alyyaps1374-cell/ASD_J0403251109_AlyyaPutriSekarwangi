#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Materi 2: Implementasi Prim
# ==========================================================

import heapq
graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])

    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
       
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
    for neighbor, w in graph[v].items():
        if neighbor not in visited:
            heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
 print(edge)
print("Total bobot =", total)

#Penjelasan Alur:
# Memulai dari sebuah simpul awal (dalam hal ini 'A') yang langsung ditandai dan dimasukkan ke dalam himpunan `visited`.
# Semua sisi yang terhubung dengan simpul awal tersebut kemudian dievaluasi dan dimasukkan ke dalam antrean prioritas
# menggunakan modul `heapq` agar sisi dengan bobot terkecil selalu mudah diambil. Selanjutnya, program melakukan
# perulangan untuk secara berulang mengekstrak sisi dengan bobot paling kecil dari antrean, jika simpul tujuan dari
# sisi tersebut belum pernah dikunjungi, simpul tersebut akan ditambahkan ke himpunan `visited`, sisinya dicatat
# ke dalam daftar jalur `mst`, dan bobotnya ditambahkan ke variabel `total_weight`. Setelah itu, program akan memeriksa
# tetangga dari simpul baru `v` tersebut dan memasukkan sisi-sisinya yang menuju simpul yang belum dikunjungi ke
# dalam antrean prioritas, lalu proses ini terus berulang hingga semua simpul berhasil terhubung membentuk pohon rentang minimum.