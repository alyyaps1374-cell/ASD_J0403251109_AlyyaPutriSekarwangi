# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Alyya Putri Sekarwangi
# NIM : J0403251109
# Kelas : B1
# ==========================================================

# ==============================
# Konstanta nama file
# ==============================
nama_file = "datatugas_pt2.txt"

# ===========================================
# Fungsi: Menampilkan Barang
# ===========================================

#membuat fungsi
def baca_data(nama_file):
    data_dict = {}   #inisialisasi dictionary
    with open("datatugas_pt2.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #hilangkan \n
            kode, nama, stok = baris.split(",") #pisahkan jadi satuan

            #simpan sebagai list
            data_dict[kode] = {
                "nama" : nama,
                "stok" : int(stok)   
            }
    return data_dict


def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data kosong")
        return
    #membuat tabel
    print("==== Daftar Barang ====")
    print(f"{'kode' : <10} | {'nama' : <12} | {'stok' : >5}")
    print("-" * 34)
    
    for kode in sorted(data_dict):
        nama=data_dict[kode]["nama"]
        stok=data_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<12} | {stok: >5}")

# ===========================================
# Fungsi: Mencari Barang Berdasarkan Kode
# ===========================================

def cari_data(data_dict):
    #meminta input kode barang
    cari_kode = input("Masukkan Kode Barang yang Ingin Dicari: ").strip()

    if cari_kode in data_dict:
        nama = data_dict[cari_kode]["nama"]
        stok = data_dict[cari_kode]["stok"]

        print("=== Data Ditemukan! ===")
        print(f"Nama: {nama}")
        print(f"Kode: {cari_kode}")
        print(f"stok: {stok}")

    else:
        print("Data Tidak Ditemukan")

# ===========================================
# Fungsi: Menambah Barang Baru
# ===========================================

def tambah_data(data_dict):
    namaB = input("Masukkan Nama Barang: ") 
    kodeB = input("Masukkan Kode Barang: ") #meminta input
    if kodeB in data_dict:
        print("Kode Sudah Digunakan")
    else:
        stokB = int(input("Masukkan Stok Barang: "))  
        data_dict[kodeB] = {
        "nama": namaB,
        "stok": stokB
    }
        #menyimpan ke file
        with open(nama_file, "w", encoding="utf-8") as file:
            for kode in sorted(data_dict.keys()):
                nama = data_dict[kode]["nama"]
                stok = data_dict[kode]["stok"]
                file.write(f"{kode},{nama},{stok}\n")

        print("Data Berhasil Ditambahkan")

# ===========================================
# Fungsi: Update Stok Barang
# ===========================================

def update_stok(data_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in data_dict:
        print("Kode Barang Tidak Ditemukan, Update Dibatalkan")
        return

    stok = data_dict[kode]["stok"]  

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    try:
        pilihan = input("Masukkan pilihan (1/2): ")
        jumlah = int(input("Masukkan jumlah: "))
        if pilihan == "1":          
            stokbaru = stok + jumlah
        elif pilihan == "2":        
            stokbaru = stok - jumlah
        else:
            print("Pilihan tidak valid")
            return
    except ValueError:
        print("Nilai harus berupa angka, update dibatalkan")
        return
    
    if stokbaru < 0:
        print("Jumlah tidak boleh kurang dari 0")
        return

    data_dict[kode]["stok"] = stokbaru

    print(f"Update Berhasil. Nilai {kode} berubah dari {stok} menjadi {stokbaru}")

# ===============================
# Fungsi: Menyimpan data ke file
# ===============================

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):  
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# =========================
# Program Utama
# =========================

def main():

    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            tambah_data(buka_data)

        elif pilihan == "4":
            update_stok(buka_data)

        elif pilihan == "5":
            simpan_stok(nama_file, buka_data)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()