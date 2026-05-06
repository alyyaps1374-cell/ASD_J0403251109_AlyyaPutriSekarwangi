#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Materi 2: Implementasi Bellman Ford dalam Phyton.
# ==========================================================

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    # Relaksasi berulang
    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():
                
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

#PENJELASAN: 
# Kode ini mengimplementasikan algoritma Bellman-Ford untuk mencari jalur terpendek dari 
# node awal ke semua node lain dalam graph. Alurnya dimulai dengan menginisialisasi jarak 
# ke semua node dengan nilai tak terhingga (inf), kecuali node awal yang disetel menjadi 0.
# Setelah itu, kode melakukan proses relaksasi dengan mengevaluasi seluruh sisi 
# di dalam graf sebanyak total node dikurangi satu (len(graph) - 1). Pada setiap evaluasi,
# jika jarak menuju suatu node ditambah bobot jalurnya ternyata lebih kecil/singkat dari 
# jarak node tetangganya yang tersimpan saat ini, maka nilai jarak tetangga tersebut akan
# diperbarui ke nilai yang baru. Pada akhirnya, fungsi akan mengembalikan dictionary yang
# berisi data jarak terpendek dari node awal ke masing-masing node di dalam graf tersebut.
