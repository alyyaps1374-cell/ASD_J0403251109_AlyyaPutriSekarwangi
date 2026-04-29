#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)
# ==========================================================

graph = {
 'Rumah': ['Sekolah', 'Toko'],
 'Sekolah': ['Perpustakaan'],
 'Toko': ['Pasar'],
 'Perpustakaan': [],
 'Pasar': []
}

from collections import deque  #menggunakan library collections bawaan python

def bfs(graph,start):    #Ini adlh fungsi utk melakukan penelusuran graph dengan BFS
    #Graph : dictionary yg menyimpan struktur dari daftar graph
    #Start: node awal penelusuran

    queue = deque()  #queue digunakan utk menyimpan node yg akan diproses
    visited = set()  #var yg digunakan utk menyimpan node yg sudah diproses

    queue.append(start)    #masukkan node awal ke queue

    visited.add(start)  #tandai node awal sbg node yg sudah dikunjungi

    while queue:
        node = queue.popleft()   #mengambil node paling depan dari queue

        #tampilkan node yg sedang dikunjungi
        print(node,end=" ")

        for neighbor in graph[node]:  #periksa semua tetangga dari node yg diambil
            if neighbor not in visited:
                visited.add(neighbor)     #tandai sbg sudah dikunjungi
                queue.append(neighbor)     #masukkan tetangga ke queue utk diproses nanti

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

#Pertanyaan Analisis
#1. Node mana yang dikunjungi pertama? 
# Node yang dikunjungi pertama adalah Rumah. Karena rumah dipakai sebagai parameter start

#2. Mengapa BFS cocok untuk mencari jalur terdekat? 
# Karena algoritma ini menelusuri secara melebar/horizontal, yaitu level demi level. 
# BFS memeriksa dulu semua yang jaraknya '1' langkah dari rumah, lalu yang selanjutnya. 

#3. Apa perbedaan urutan BFS jika struktur graph diubah?
# BFS beroperasi menggunakan queue (First in first out), artinya yang masuk
# pertama akan dieksekusi pertama, seperti antrian. Maka misalnya struktur graph diubah
# menjadi 'Rumah': ['Toko', 'Sekolah'], maka 'Toko' dan cabang-cabangnya ('Pasar')
# akan masuk ke antrean dan diproses mendahului 'Sekolah'.




