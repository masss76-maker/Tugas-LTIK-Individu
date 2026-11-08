import random

# ==============================================================
# DATABASE INTERNAL MAHASISWA & AKUN UPI CONNECT
# ==============================================================
DATABASE_UPI_CIBIRU = [
    # Prodi RPL (Rekayasa Perangkat Lunak)
    {"nama": "Dimas Nugraha", "prodi": "RPL", "hobi": "coding", "gender": "L", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    {"nama": "Nadia Utami", "prodi": "RPL", "hobi": "coding", "gender": "P", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    {"nama": "Putri Amalia", "prodi": "RPL", "hobi": "musik", "gender": "P", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    
    # Prodi Tekkom (Teknik Komputer)
    {"nama": "Ahmad Fauzi", "prodi": "Tekkom", "hobi": "game", "gender": "L", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    {"nama": "Rayhan Rafif", "prodi": "Tekkom", "hobi": "ngopi", "gender": "L", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    
    # Prodi PMM (Pertukaran Mahasiswa Merdeka)
    {"nama": "Siti Sarah", "prodi": "PMM", "hobi": "musik", "gender": "P", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    {"nama": "Budi Santoso", "prodi": "PMM", "hobi": "traveling", "gender": "L", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    
    # Prodi PGSD (Pendidikan Guru Sekolah Dasar)
    {"nama": "Rina Marlina", "prodi": "PGSD", "hobi": "membaca", "gender": "P", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    {"nama": "Dendi Wijaya", "prodi": "PGSD", "hobi": "futsal", "gender": "L", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    
    # Prodi PGPAUD (Pendidikan Guru PAUD)
    {"nama": "Hasna Julpa", "prodi": "PGPAUD", "hobi": "lari", "gender": "P", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"},
    {"nama": "Rizky Ramadhan", "prodi": "PGPAUD", "hobi": "musik", "gender": "L", "username": "upiconnect06", "password": "semuahubunganterhubungselamanya"}
]


# 1. FUNGSI UTAS: FITUR REGISTER (SIGN-UP)
def fitur_register():
    print("\n==============================================")
    print("         MENU PENDAFTARAN AKUN BARU           ")
    print("==============================================")
    
    nama = input("Masukkan Nama Lengkap Anda: ").strip()
    prodi = input("Masukkan Program Studi (RPL/Tekkom/PMM/PGSD/PGPAUD): ").strip()
    hobi = input("Masukkan Hobi Anda (coding/game/musik/lari): ").strip().lower()
    gender = input("Masukkan Gender Anda (L/P): ").strip().upper()
    
    print("----------------------------------------------")
    username = input("Buat Username Baru: ").strip()
    password = input("Buat Password Baru: ").strip()

    akun_baru = {
        "nama": nama,
        "prodi": prodi,
        "hobi": hobi,
        "gender": gender,
        "username": username,
        "password": password
    }
    
    DATABASE_UPI_CIBIRU.append(akun_baru)
    
    print("\n[SUKSES] Akun Anda berhasil didaftarkan!")
    print("Silakan kembali ke menu utama untuk mencoba Login.\n")

# ==============================================================
# 2. FUNGSI UTAS: FITUR LOGIN & AUTENTIKASI
# ==============================================================
def fitur_login():
    print("\n==============================================")
    print("          MENU LOGIN UTAMA AKUN UPI           ")
    print("==============================================")
    
    input_user = input("Masukkan Username: ").strip()
    input_pass = input("Masukkan Password: ").strip()
    
    for akun in DATABASE_UPI_CIBIRU:
        if akun["username"] == input_user and akun["password"] == input_pass:
            print(f"\n[SUKSES] Login Berhasil! Selamat datang, {akun['nama']}.\n")
            return True, akun 
            
    print("[GAGAL] Username atau Password salah atau tidak ditemukan!\n")
    return False, None

# ==============================================================
# 3. FUNGSI UTAS: ENGINE PENCARIAN TEMAN
# ==============================================================
# ==============================================================
# 3. FUNGSI UTAS: ENGINE PENCARIAN TEMAN (DENGAN FITUR RANDOM INPUT)
# ==============================================================
def menu_cari_teman():
    while True:
        print("==============================================")
        print("   FITUR: CARI TEMAN (GENDER, HOBI, & PRODI)  ")
        print("   *Ketik 'random' jika ingin diacak sistem   ")
        print("==============================================")
        
        input_gender = input("Masukkan Gender yang dicari (L/P/random): ").strip().lower()
        cari_hobi = input("Masukkan Hobi yang dicari (coding/game/musik/lari/random): ").strip().lower()
        cari_prodi = input("Masukkan Prodi yang dicari (RPL/Tekkom/PMM/PGSD/PGPAUD/random): ").strip().lower()
        
        if input_gender == "random":
            cari_gender = random.choice(["L", "P"])
            print(f"-> [Sistem] Mengacak Gender menjadi: {cari_gender}")
        else:
            cari_gender = input_gender.upper()

        if cari_hobi == "random":
            cari_hobi = random.choice(["coding", "game", "musik", "lari"])
            print(f"-> [Sistem] Mengacak Hobi menjadi: {cari_hobi}")

        if cari_prodi == "random":
            cari_prodi = random.choice(["rpl", "tekkom", "pmm", "pgsd", "pgpaud"])
            print(f"-> [Sistem] Mengacak Prodi menjadi: {cari_prodi.upper()}")
        
        print(f"\n[Searching] Mencari Gender: [{cari_gender}], Hobi: [{cari_hobi}], Prodi: [{cari_prodi.upper()}]...")
        print("--------------------------------------------------")
        
        jumlah_ditemukan = 0
        
        for mahasiswa in DATABASE_UPI_CIBIRU:
            if (mahasiswa["gender"] == cari_gender and 
                mahasiswa["hobi"] == cari_hobi and 
                mahasiswa["prodi"].lower() == cari_prodi):
                
                jumlah_ditemukan = jumlah_ditemukan + 1
                print(f"{jumlah_ditemukan}. Nama  : {mahasiswa['nama']}")
                print(f"   Prodi : {mahasiswa['prodi']}")
                print(f"   Hobi  : {mahasiswa['hobi'].capitalize()}")
                print(f"   Gender: {mahasiswa['gender']}")
                print("-" * 30)
                
        if jumlah_ditemukan == 0:
            print("Maaf, belum ada teman yang cocok dengan kriteria tersebut.")
        else:
            print(f"Berhasil menemukan {jumlah_ditemukan} teman yang cocok!")
            
        print("==============================================")
        pilihan_ulang = input("Apakah kamu ingin mencari teman lagi? (ya/tidak): ").strip().lower()
        print()
        
        if pilihan_ulang == 'tidak' or pilihan_ulang == 'n':
            break


# ==============================================================
# 4. FUNGSI UTAS: FITUR CARI TEMAN RANDOM (FITUR BARU)
# ==============================================================
def fitur_cari_random():
    print("\n==============================================")
    print("       FITUR: CARI TEMAN RANDOM INSTAN        ")
    print("==============================================")
    print("[System] Mengocok database UPI Cibiru...")
    print("----------------------------------------------")
    
    teman_acak = random.choice(DATABASE_UPI_CIBIRU)
    
    print("🎉 Boom! Kami menemukan rekan acak untukmu:")
    print(f"👉 Nama   : {teman_acak['nama']}")
    print(f"👉 Prodi  : {teman_acak['prodi']}")
    print(f"👉 Hobi   : {teman_acak['hobi'].capitalize()}")
    print(f"👉 Gender : {teman_acak['gender']}")
    print("==============================================")
    
    input("Tekan Enter untuk kembali ke menu...")
    print()

# ==============================================================
# 5. FUNGSI INDUK UTAMA (MAIN CONTROLLER)
# ==============================================================
def main():
    while True:
        print("==============================================")
        print("          WELCOME TO UPI CONNECT              ")
        print("==============================================")
        print(" 1. Login Akun")
        print(" 2. Register (Daftar Akun Baru)")
        print(" 3. Cari Teman Random (Gacha Global)")
        print(" 4. Exit (Keluar Aplikasi)")
        print("==============================================")
        
        pilihan_menu = input("Pilih nomor menu (1/2/3/4): ").strip()
        
        if pilihan_menu == "1":
            status_login, user_login = fitur_login()
            if status_login:
                menu_cari_teman()
        elif pilihan_menu == "2":
            fitur_register()
        elif pilihan_menu == "3":
            fitur_cari_random()  
        elif pilihan_menu == "4":
            print("Terima kasih telah menggunakan UPI Connect. Sampai jumpa!")
            print("==============================================")
            break
        else:
            print("[PERINGATAN] Pilihan menu tidak valid! Gunakan angka 1, 2, 3, atau 4.\n")

main()
