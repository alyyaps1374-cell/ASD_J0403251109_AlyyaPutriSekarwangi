#=================================================
#Nama   : Alyya Putri Sekarwangi
#NIM    : J0403251109
#Kelas  : B1
#=================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    
    # Base case: jika panjang PIN sudah sesuai
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Rekursi untuk setiap kemungkinan angka
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


# Membuat PIN dengan panjang 3
buat_pin(3)