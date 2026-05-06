#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==============================================================
# Latihan 5
# ==============================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
 'Bogor': {'Jakarta': 5, 'Depok': 2},
 'Depok': {'Jakarta': 2},
 'Jakarta': {'Bandung': 7},
 'Depok': {'Bandung': 6},
 'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

        return distances

node_awal = 'Bogor'

hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

# Pertanyaan Analisis
# Jawaban Analisis:

# 1. Node awal yang digunakan apa?
# Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Depok dengan total jarak 2 (tidak termasuk rute Bogor ke Bogor itu sendiri).

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Bandung dengan total jarak terpendeknya mencapai 8.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma mulai dari 'Bogor' (jarak 0) dan mengecek tetangganya: Depok (jarak 2) dan Jakarta (jarak 5). 
# Karena Depok memiliki jarak paling kecil di antrean (2), program mengevaluasi Depok terlebih dahulu. 
# Dari Depok, program menemukan rute ke Jakarta dengan jarak total 2 + 2 = 4 (karena 4 lebih cepat dari 5, 
# jarak rekor ke Jakarta di-update menjadi 4) dan rute ke Bandung dengan total 2 + 6 = 8. 
# Program kemudian mengambil Jakarta dari antrean (jarak 4). Dari Jakarta ke Bandung butuh +7 (total 11). 
# Karena 11 lebih besar dari rekor Bandung saat ini (8), rute ini diabaikan. 
# Terakhir program mengecek Bandung (8) yang tidak punya rute lanjutan. Proses selesai 
# dan program mengembalikan jarak minimum akhir.