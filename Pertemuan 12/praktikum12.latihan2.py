#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
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
    
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
                        
# Pertanyaan Analisis
# Tuliskan jawaban sebagai komentar di bagian bawah program.
# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B? 4

# 2. Berapa jarak terpendek dari A ke C? 2

# 3. Berapa jarak terpendek dari A ke D? 3

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Karena akumulasi/total bobot rute A -> C -> D adalah 3 (2 + 1), 
# yang mana nilainya lebih kecil dan cepat dibandingkan total 
# bobot rute A -> B -> D yang mencapai 9 (4 + 5).

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# priority_queue berfungsi untuk secara otomatis mengurutkan 
# node berdasarkan jarak terpendeknya. Dengan begitu, algoritma 
# akan selalu memilih dan memproses node terdekat yang belum 
# dievaluasi terlebih dahulu, sehingga mempercepat pencarian 
# dan menjamin keakuratan rute minimum.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Dijkstra berasumsi bahwa jarak total akan selalu bertambah (atau setidaknya tetap) 
# setiap kali melewati sebuah jalur baru. Begitu suatu node diproses dari priority queue, 
# Dijkstra menganggap jarak terpendek ke node tersebut sudah mutlak dan final (tidak akan dievaluasi ulang). 
# Jika ada bobot negatif di langkah-langkah berikutnya, jarak yang tadinya dianggap final tersebut 
# bisa jadi salah karena ternyata ada jalan memutar bersiklus negatif yang bisa membuatnya lebih kecil lagi.