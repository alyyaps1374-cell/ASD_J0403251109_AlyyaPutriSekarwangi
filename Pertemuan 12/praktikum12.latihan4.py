#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum sementara ke semua node
    distances = {node: float('inf') for node in graph}
    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Priority queue untuk memilih node dengan jarak terkecil
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Ambil node dengan jarak terpendek
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak lebih besar dari rekor jarak saat ini, lewati
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua lokasi tetangga
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight
            
            # Jika rute ini lebih cepat, perbarui rekornya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================
# Pertanyaan Analisis
# ==========================================

# Jawaban Analisis:

# 1. Lokasi mana yang paling dekat dari Gerbang?
# Kantin dengan waktu tempuhnya hanya 2 menit dari Gerbang.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 7 menit. Rute tercepatnya adalah: Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7 menit). 

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Tidak selalu. Sebagai contoh, dari Kantin menuju Aula terdapat jalur langsung dengan 
# waktu tempuh 7 menit. Namun, jika kita mengambil jalur transit/memutar melewati Lab 
# terlebih dahulu (Kantin -> Lab -> Aula), waktu tempuhnya justru lebih cepat yaitu 
# hanya 5 menit (4 + 1). Oleh karena itu, kita tidak bisa berasumsi bahwa jalur yang memutar selalu lebih lama.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Karena algoritma Dijkstra sangat efisien untuk mencari rute terpendek dari satu titik awal
# ke semua titik lain dalam jaringan. Selain itu, kasus lokasi 
# kampus ini direpresentasikan dengan graf berbobot positif (waktu tempuh tidak mungkin bernilai negatif), 
# yang merupakan syarat mutlak agar algoritma Dijkstra dapat bekerja dengan akurat.