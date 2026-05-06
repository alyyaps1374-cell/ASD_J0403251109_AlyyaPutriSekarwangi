#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Materi 1: Implementasi Dijkstra dalam Phyton.
# ==========================================================

import heapq
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')
print(hasil)

#PENJELASAN:
#Kode ini bekerja dengan menginisialisasi jarak ke semua titik sebagai tak terhingga kecuali
# titik awal yang bernilai nol, lalu memasukkan titik awal tersebut ke dalam sebuah antrean prioritas. 
# Program kemudian memasuki siklus perulangan di mana ia secara otomatis akan selalu mengambil titik 
# dengan jarak terpendek dari antrean untuk dievaluasi terlebih dahulu. Untuk setiap titik yang sedang 
# dievaluasi, program akan memeriksa semua titik tetangganya, menghitung total jarak tempuh dari titik awal, 
# dan jika rute baru ini ternyata lebih pendek dari rekor jarak yang pernah dicatat sebelumnya, 
# program akan memperbarui rekor tersebut lalu memasukkan titik tetangga itu kembali ke dalam antrean. 
# Siklus pencarian ini akan terus berulang hingga antrean kosong (semua kemungkinan rute telah dievaluasi), 
# dan pada akhirnya program akan mengembalikan kumpulan data yang berisi jarak paling minimum dari titik 
# awal ke setiap titik di dalam jaringan graph tersebut.