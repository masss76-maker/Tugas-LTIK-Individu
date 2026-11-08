# Latihan Soal N0 1
# ini adalah program untuk mengubah nilai angka menjadi nilai huruf berdasarkan kriteria tertentu.
# Mengambil input nilai dari user
nilai = float(input("Masukkan nilai angka: "))

# Proses pengecekan kondisi nilai
if nilai >= 90:
    nilai_huruf = "A"
elif nilai >= 80:
    nilai_huruf = "B"
elif nilai >= 70:
    nilai_huruf = "C"
else:
    nilai_huruf = "D"

# Menampilkan hasil
print(f"Nilai Huruf: {nilai_huruf}")


# Latihan Soal N0 2
print("PROGRAM SELEKSI MODEL CATWALK")

# Mengambil input dari user
gender = input("Masukkan Jenis Kelamin (Pria/Wanita): ").strip().lower()
umur = int(input("Masukkan Umur: "))
tinggi = int(input("Masukkan Tinggi Badan (cm): "))
iq = int(input("Masukkan Skor IQ: "))

# Inisialisasi status awal
layak = False

# Pengecekan kondisi utama
if 18 <= umur <= 25 and iq >= 130:
    if gender == "wanita" and tinggi >= 170:
        layak = True
    elif gender == "pria" and tinggi >= 175:
        layak = True

# Menampilkan hasil prediksi
if layak:
    #print("\nHasil: Selamat! Anda MEMENUHI SYARAT menjadi model catwalk.")
    print("\nHasil: Selamat! Anda MEMENUHI SYARAT menjadi model catwalk.")
else:
    #print("\nHasil: Maaf, Anda BELUM MEMENUHI SYARAT menjadi model catwalk.")
    print("\nHasil: Maaf, Anda BELUM MEMENUHI SYARAT menjadi model catwalk.")

# Latihan Soal N0 3

# Mengambil input data nilai tugas, UTS, dan UAS dari user
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai rata-rata dari ketiga komponen ujian
rata_rata = (tugas + uts + uas) / 3

print("\nHASIL EVALUASI MAHASISWA")
print(f"Rata-rata Nilai: {rata_rata:.2f}")

# Pengecekan kondisi tingkat 1: Jika rata-rata >= 70
if rata_rata >= 70:
    # Pengecekan kondisi tingkat 2: Jika semua nilai >= 60
    if tugas >= 60 and uts >= 60 and uas >= 60:
        print(f"{nama_mahasiswa} kamu LULUS tanpa remedial")
    else:
        print(f"{nama_mahasiswa} kamu LULUS dengan remedial")

# Pengecekan kondisi tingkat 1: Jika rata-rata < 70
else:
    # Pengecekan kondisi tingkat 2: Jika rata-rata >= 50
    if rata_rata >= 50:
        print(f"{nama_mahasiswa} kamu TIDAK LULUS, boleh remedial")
    else:
        print(f"{nama_mahasiswa} kamu TIDAK LULUS dan tidak boleh remedial")

#print("hello world")



# Membuat variabel password asli
#password_benar = "rahasia123"

# Mencocokkan password (ceritanya pengguna mengetik "rahasia123")
#password_input = "rahasia123"

#if password_input == password_benar:
    #print("Akses Diterima! Selamat Datang.")
#else:
    #print("Akses Ditolak! Password Anda Salah.")

print("SIMULASI MESIN ATM")

pin_benar = "123456"
jumlah_salah = 0

# Komputer akan terus meminta PIN SELAMA jumlah salah masih di bawah 3
while jumlah_salah < 3:
    # Simulasi input pengguna (ceritanya pengguna salah mengetik PIN)
    input_pin = "999999" 
    
    if input_pin == pin_benar:
        print("PIN Benar! Selamat datang di menu ATM.")
        break
    else:
        jumlah_salah = jumlah_salah + 1
        sisa_kesempatan = 3 - jumlah_salah
        print(f"PIN Salah! Sisa kesempatan Anda: {sisa_kesempatan} kali.")

# Jika perulangan berhenti karena sudah salah 3 kali
if jumlah_salah == 3:
    print("AKUN ANDA DIBLOKIR! Silakan hubungi bank terdekat.")
