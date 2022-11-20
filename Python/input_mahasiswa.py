# Jika ingin mengambil kode ini harap cantumkan sumbernya
# Dibuat pada tanggal 20 November 2022 oleh Zubair Adnan

print("====== Program Sederhana ======\n")

# Program input
nama = input("Masukan nama mahasiswa/i : ")
nim = input("Masukan NIM mahasiswa/i : ")
nilai = int(input("Masukan nilai mahasiswa : "))

# Program Proses

#Proses keterangan
keterangan = ("Tidak Lulus","Lulus")[nilai >= 60]

#Proses grade
if nilai == 100 or nilai >= 85:
    grade = "A"
elif nilai == 84 or nilai >= 75:
    grade = "B"
elif nilai == 74 or nilai >= 60:
    grade = "C"
elif nilai == 59 or nilai >= 30:
    grade = "D"
else:
    grade = "E"

#Proses predikat
if nilai == 100 or nilai >= 85:
    predikat = "Memuaskan"
elif nilai == 84 or nilai >= 75:
    predikat = "Bagus"
elif nilai == 74 or nilai >= 60:
    predikat = "Cukup"
elif nilai == 59 or nilai >= 30:
    predikat = "Kurang"
else:
    predikat = "Buruk"

# Program output
print("\n------ Hasil Output ------\n")
print("Nama Mahasiswa\t : %s" % nama)
print("Nim Mahasiswa\t : %s" % nim)
print("Nilai Mahasiswa\t : %d" % nilai)
print("Keterangan\t : %s"% keterangan)
print("Grade\t\t : %s"% grade)
print("Predikat\t : %s"% predikat)