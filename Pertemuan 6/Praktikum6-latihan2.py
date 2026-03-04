#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 2
# ==========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1 
        
        while j >= 0 and ( ) :
            data[j+1] = data[j]
            j -= 1
        
        ( )
    return data

### SOAL ###
# 1. Lengapi kondisi agar menjadi sorting ascending.
# 2. Ubah agar menjadi descending.

### JAWABAN ###
# 1
def ascending(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1 
        
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data

angka = [8,7,5,2,4]
print("Data awal: ",angka)
print("Hasil sorting: ",ascending(angka))

# 2
def descending(data):
    for i in range(1, len(data)):
        
        key = data[i]
        j = i - 1 
        
        while j >= 0 and data[j] < key:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data

angka = [8,7,5,2,4]
print("\nData awal: ",angka)
print("Hasil sorting: ",descending(angka))