#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Implementasi DFS
# ==========================================================

#Struktur Data Utk Membuat Antrian, kita gunakan dari library collections bawaan python
from collections import deque


#Implementasi Graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
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

#set visited
visited = set()

#menjalankan dfs dari a
dfs(graph,"A",visited)
