#===============================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan dasar 1: Membaca seluruh isi file
#===============================================================================

#membuka file dengan mode read ("r")
with open("DataMahasiswa.txt","r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter:", len(isi_file))
print("Jumlah Baris:", isi_file.count("\n")+1)


#Membuka file perbaris
print("===Membaca File Perbaris===")
jumlah_baris = 0
with open("DataMahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan baris baru
        print("Baris ke-", jumlah_baris)
        print("Isinya: ", baris)

#===============================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan dasar 2 : Parsing baris menjadi kolom data
#===============================================================================

with open("DataMahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #Sparsing data berdasarkan karakter
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)

#===============================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan dasar 3 : Membaca FIle dan Menyimpan ke List
#===============================================================================

data_list = [] #list untuk menampung data mahasiswa

with open("DataMahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan sebagai list " [nim, nama, nilai]"
        data_list.append([nim,nama,int(nilai)])

print("==== Data Mahasiswa dalam LIST===")
print(data_list)

print("==== Jumlah Record dalam LIST===")
print("Jumlah Record", len(data_list)) 


print("===Menampilkan Data Record===")
print("Contoh Record Pertama: ")

#===============================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan dasar 4 : Membaca File dan Menyimpan ke Dictionary
#===============================================================================

data_dict = {} #Membuat variabel untuk dictionary

with open("DataMahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary
        data_dict[nim] = {  #key
            "nama": nama,   #value
            "nilai": int(nilai)
 
        }
print("===Data Mahasiswa dalam Dictionary===")
print(data_dict)