#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==================================================================
# Praktikum 13 - Graph III: Implementasi Sederhana Algoritma Prim
# ==================================================================

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

# Pertanyaan Analisis:
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
# Node yang awal digunakan adalah node A
# 2. Edge mana yang dipilih pertama kali?
# Edge yang pertama kali dpiilih adalah edge antara A dan C
# 3. Bagaimana Prim menentukan edge berikutnya?
# Dengan cara melihat edge yang terhubung dengan node yang sudah dipilih dengan
# bobot terkecil
# 4. Berapa total bobot MST yang dihasilkan?
# Total bobot yang dihasilkan adalah 6
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Prim lebih berorientasi pada pengembangan tree dari node awal
# ke node-node di sekitarnya, sedangkan kruskal berfokus
# pada pemilihan edge secara global.