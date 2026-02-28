#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Contoh Backtracking: Kombinasi Biner dengan Batas '1'
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    
    # Pruning: jika jumlah angka '1' melebihi batas, hentikan cabang ini
    if jumlah_1 > batas:
        return
    
    # Base case: jika panjang kombinasi sudah mencapai n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi memilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Rekursi memilih '1' (menambah jumlah_1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# Pemanggilan fungsi dengan panjang 4 dan maksimal dua angka '1'
biner_batas(4, 2)