#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)
# ==========================================================

#Struktur Data Utk Membuat Antrian, kita gunakan dari library collections bawaan python
from collections import deque


#Implementasi Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph,node,visited):  #fungsi utk melakukan penelusuran graph pakai DFS
    #graph : dict yang menyimpan graph
    #node : menyimpan node yang sedang dikunjungi
    #visited : menyimpan node yang sudah dikunjungi

    visited.add(node)   #tandai node saat ini sbg node yg sudah dikunjungi

    #tampilkan node yg sedang dikunjungi
    print(node, end=" ")

    for neighbor in graph[node]:    #periksa tetangga dari node yg sedang dikunjungi
        if neighbor not in visited:
            dfs(graph,neighbor,visited)  #lakukan dfs secara rekursif ke tetangga tersebut

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

#Pertanyaan Analisis
#1. Mengapa DFS masuk ke node terdalam terlebih dahulu? 
# Karena DFS bekerja dengan Stack (Last in first out) yang seperti
# tumpukan.

#2. Apa yang terjadi jika urutan neighbor diubah? 
# Jika urutan neighbor diubah maka outputnya pun akan berubah.
# karena DFS akan selalu mengambil elemen pertama dari 
# daftar tetangga yang tersedia. Misalnya jika kita ubah
# menjadi 'A': ['C', 'B'] maka outputnya akan menjadi (A C F B D E)

#3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# Jika struktur graph di sini dijalankan menggunakan BFS maka
# hasilnya akan (A B C D E F), jika menggunakan DFS maka
# hasilnya akan (A B D E C F). Ini terjadi karena BFS bekerja
# dengan cara horizontal, maka dia akan menelusuri node ke samping dulu
# semua yang selevel, baru turun ke bawah. Sedangkan DFS bekerja secara vertikal.