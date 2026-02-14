# ===============================
# HEADER & MENU
# ===============================
def show_menu():
    print()
    print("╔══════════════════════════════════════╗")
    print("║   🌿 ARUNIKA OUTDOOR RENTAL APP 🏕️    ║")
    print("║   Explore the peaks, gear up with us!║")
    print("╚══════════════════════════════════════╝")

    # SUBHEADER (lebih kecil, beda gaya)
    print()
    print("────────── MENU AUTENTIKASI ──────────")
    print()
    print("  1. Daftar")
    print("  2. Masuk")
    print("  3. Keluar")

def show_penyewa_menu():
    print()
    print("────────── MENU UTAMA ──────────")
    print()
    print("1. Lihat Daftar Alat Outdoor")
    print("2. Buat Penyewaan")
    print("3. Lihat Data Penyewaan Saya")
    print("4. Ubah Data Penyewaan")
    print("5. Batalkan Penyewaan")
    print("6. Tampilkan Data Personal User")
    print("7. Kembali")
    print("─────────────────────────────────")

# ==========================================
# DATA STORAGE
# ==========================================
# Data inisiasi user
users = [
    {
        "userid": "owner01", 
        "password": "Owner@1234", 
        "email": "owner1@arunika.com",
        "nama": "Yunita",
        "gender": "wanita",
        "usia": 25,
        "pekerjaan": "Dosen",
        "hobi": "Mendaki",
        "alamat": {"kota": "Bogor", "rt": "01", "rw": "01", "zipc": "44323"},
        "geo": {"lat": "2.9175", "lon": "10.6191"},
        "nohp": "081234567890"
    },{
        "userid": "abdul55", 
        "password": "User@2024", 
        "email": "abdulzsz@gmail.com",
        "nama": "Abdul",
        "gender": "pria",
        "usia": 20,
        "pekerjaan": "Mahasiswa",
        "hobi": "Fotografi",
        "alamat": {"kota": "Bandung", "rt": "02", "rw": "02", "zipc": "10110"},
        "geo": {"lat": "3.2088", "lon": "6.8456"},
        "nohp": "080987654321"
    }
]

data_penyewaan = [] 

# ==========================================
# BASIC VALIDATION
# ==========================================
def is_alpha(text):
    for c in text:
        if not (c.isalpha() or c == " "):
            return False
    return True


def is_alnum(text):
    for c in text:
        if not (c.isalpha() or c.isdigit()):
            return False
    return True


def is_int(text):
    return text.isdigit()


def is_float(text):
    try:
        float(text)
        return True
    except:
        return False

# ==========================================
# USER ID INPUT
# ==========================================
def input_userid():
    while True:
        userid = input("UserId ==> ")

        if len(userid) < 6:
            print("❌ User Id minimal 6 karakter")
            continue

        if len(userid) > 20:
            print("❌ User Id maksimal 20 karakter")
            continue

        if not is_alnum(userid):
            print("❌ User Id hanya boleh huruf dan angka")
            continue

        has_letter = False
        has_digit = False

        for c in userid:
            if c.isalpha():
                has_letter = True
            elif c.isdigit():
                has_digit = True

        if not (has_letter and has_digit):
            print("❌ User Id harus mengandung huruf dan angka")
            continue

        for u in users:
            if u["userid"] == userid:
                print("❌ User Id sudah digunakan")
                break
        else:
            return userid


# ==========================================
# PASSWORD VALIDATION
# ==========================================
def input_password():
    while True:
        password = input("Password ==> ")

        if len(password) < 8:
            print("❌ Password minimal 8 karakter")
            continue

        upper = lower = digit = special = False
        allowed_special = "/.,@#$%"

        for c in password:
            if c.isupper():
                upper = True
            elif c.islower():
                lower = True
            elif c.isdigit():
                digit = True
            elif c in allowed_special:
                special = True
            else:
                print("❌ Password mengandung karakter tidak valid")
                break
        else:
            if upper and lower and digit and special:
                return password
            else:
                print("❌ Password harus mengandung huruf besar, kecil, angka, dan karakter khusus")

# ==========================================
# EMAIL VALIDATION 
# ==========================================
def input_email():
    while True:
        email = input("Email ==> ")

        if email.count("@") != 1:
            print("Email Tidak Valid, Jumlah @ harus 1")
            continue

        username, domain = email.split("@")

        if username == "":
            print("Email Tidak Valid, Format Username salah")
            continue

        if not username[0].isalnum():
            print("Email Tidak Valid, Username harus diawali huruf atau angka")
            continue

        for c in username:
            if not (c.isalnum() or c == "_" or c == "."):
                print("Email Tidak Valid, Format Username salah")
                break
        else:
            if "." not in domain:
                print("Email Tidak Valid, Format Email salah (tidak ada ekstensi)")
                continue

            domain_parts = domain.split(".")

            if len(domain_parts) > 3:
                print("Email Tidak Valid, Maksimal 2 ekstensi")
                continue

            hosting = domain_parts[0]
            if not hosting.isalnum():
                print("Email Tidak Valid, Format Hosting salah")
                continue

            ext_valid = True
            for ext in domain_parts[1:]:
                if not ext.isalpha() or len(ext) > 5:
                    ext_valid = False
                    break

            if not ext_valid:
                print("Email Tidak Valid, Format Ekstensi salah")
                continue

            print("Alamat Email yg anda Masukkan Valid")
            return email

# ==========================================
# REGISTER FUNCTION
# ==========================================
def register():
    print("\n----------- Register -------")
    print("Masukkan Data :")

    userid = input_userid()
    password = input_password()
    email = input_email()

    # NAMA
    while True:
        nama = input("Nama ==> ")
        if is_alpha(nama):
            break
        print("❌ Nama hanya alfabet")

    # GENDER
    while True:
        gender = input("Pria/Wanita) ==> ").lower()
        if gender in ["pria", "wanita"]:
            break
        print("❌ Gender tidak valid")

    # USIA
    while True:
        usia = input("Usia ==> ")
        if is_int(usia) and 17 <= int(usia) <= 80:
            usia = int(usia)
            break
        print("❌ Usia harus 17–80")

    # PEKERJAAN
    while True:
        pekerjaan = input("Pekerjaan ==> ")
        if is_alpha(pekerjaan):
            break
        print("❌ Pekerjaan hanya alfabet")

    # HOBI
    while True:
        hobi = input("Hobi ==> ")
        clean = hobi.replace(" ", "").replace(",", "")

        if len(hobi.split(",")) > 1 and clean.isalpha():
            break

        print("❌ Hobi harus alfabet dan dipisahkan dengan koma")


    # ALAMAT
    print("\nAlamat :")
    while True:
        kota = input("Nama Kota ==> ")
        if is_alpha(kota):
            break

    while True:
        rt = input("RT ==> ")
        if is_int(rt):
            break

    while True:
        rw = input("RW ==> ")
        if is_int(rw):
            break

    while True:
        zipc = input("Zip Code ==> ")
        if is_int(zipc) and len(zipc) == 5:
            break
        print("❌ Zip Code harus 5 digit")

    # GEO
    while True:
        lat = input("Latitude ==> ")
        if is_float(lat):
            break
        print("❌ Hanya Float")

    while True:
        lon = input("Longitude ==> ")
        if is_float(lon):
            break
        print("❌ Hanya Float")

    # NO HP
    while True:
        nohp = input("No Hp ==> ")
        if is_int(nohp) and 11 <= len(nohp) <= 13:
            break
        print("❌ No Hp harus 11–13 digit")

    # SIMPAN DATA
    save = input("\nSimpan Data (Y/N): ").lower()
    if save == "y":
        users.append({
            "userid": userid,
            "password": password,
            "email": email,
            "nama": nama,
            "gender": gender,
            "usia": usia,
            "pekerjaan": pekerjaan,
            "hobi": hobi,
            "alamat": {"kota": kota, "rt": rt, "rw": rw, "zipc": zipc},
            "geo": {"lat": lat, "lon": lon},
            "nohp": nohp
        })
        print("✅ Data tersimpan")
    else:
        print("❌ Data tidak tersimpan")


# ==========================================
# LOGIN FUNCTION
# ==========================================
def login():
    percobaan = 0
    # Loop while untuk percobaan login maksimal 5 kali
    while percobaan < 5:
        print("\n──────────── LOGIN ────────────")
        userid_input = input("Masukkan ID : ") 
        password_input = input("Masukkan Password : ")
        user_found = False
        
        # Cek ID dari database
        for u in users:
            if u["userid"] == userid_input:
                user_found = True
                # Cek passwordnya
                if u["password"] == password_input:
                    print("\n🌿 Login berhasil. Selamat datang di Arunika!")
                    return userid_input
                else:
                    # Password salah
                    percobaan += 1
                    print(f"Password salah (Percobaan Gagal: {percobaan} kali)")
                    break 
        # ID tidak terdaftar
        if not user_found:
            percobaan += 1
            print(f"ID tidak terdaftar. (Percobaan Gagal: {percobaan} kali)")
    # Jika gagal 5 kali
    print("Anda telah gagal 5 kali")
    print("Silakan pilih menu lain")
    return False

# =====================================================
# LIST DATA ALAT OUTDOOR ARUNIKA
# Digunakan untuk:
# - Menampilkan daftar alat sewa
# - Pencarian alat berdasarkan kode barang
# - Harga berlaku untuk sewa 1 hari
# =====================================================

# ==========================================
# Sub Menu READ DATA ALAT OUTDOOR
# ==========================================

alat_outdoor = [
    # 1. Tas Carrier
    {"kode": "CARR-1-REI", "jenis": "Carrier", "nama": "Carrier Arei Toba 80L", "harga": 40000, "stok": 7},
    {"kode": "CARR-2-CON", "jenis": "Carrier", "nama": "Carrier Consina Tarebbi 60L", "harga": 30000, "stok": 5},
    {"kode": "CARR-3-EIG", "jenis": "Carrier", "nama": "Eiger Streamline 45L", "harga": 35000, "stok": 8},

    # 2. Tenda
    {"kode": "TEN-1-2P", "jenis": "Tenda", "nama": "Tenda Consina Kapasitas 2 Orang", "harga": 45000, "stok": 0},
    {"kode": "TEN-2-4P", "jenis": "Tenda", "nama": "Tenda Eiger Kapasitas 4 Orang", "harga": 60000, "stok": 5},
    {"kode": "TEN-3-8P", "jenis": "Tenda", "nama": "Tenda Rei Kapasitas 8 Orang", "harga": 70000, "stok": 7},

    # 3. Sepatu
    {"kode": "SPT-1-EIG", "jenis": "Sepatu", "nama": "Sepatu Gunung Eiger X-Trek", "harga": 35000, "stok": 2},
    {"kode": "SPT-2-ARE", "jenis": "Sepatu", "nama": "Sepatu Gunung Arei Ventura", "harga": 30000, "stok": 6},
    {"kode": "SPT-3-CON", "jenis": "Sepatu", "nama": "Sepatu Gunung Consina Alpine", "harga": 32000, "stok": 5},

    # 4. Sleeping Bag
    {"kode": "SB-1-ARC", "jenis": "Sleeping Bag", "nama": "Sleeping Bag Leuser Arctic", "harga": 16500, "stok": 6},
    {"kode": "SB-2-EXP", "jenis": "Sleeping Bag", "nama": "Sleeping Bag Avtech Explorer", "harga": 15000, "stok": 7},
    {"kode": "SB-3-POL", "jenis": "Sleeping Bag", "nama": "Sleeping Bag Rei Polar", "harga": 18000, "stok": 3},

    # 5. Trekking Pole
    {"kode": "TP-1-EIG", "jenis": "Trekking Pole", "nama": "Trekking Pole Eiger Carbon", "harga": 10000, "stok": 5},
    {"kode": "TP-2-CON", "jenis": "Trekking Pole", "nama": "Trekking Pole Consina Alpine", "harga": 10000, "stok": 7},
    {"kode": "TP-3-REI", "jenis": "Trekking Pole", "nama": "Trekking Pole Rei Explorer", "harga": 10000, "stok": 6},

    # 6. Hydropack
    {"kode": "HYD-1-EIG", "jenis": "Hydropack", "nama": "Hydropack Eiger 2L", "harga": 15000, "stok": 8},
    {"kode": "HYD-2-CON", "jenis": "Hydropack", "nama": "Hydropack Consina 2L", "harga": 13000, "stok": 6},
    {"kode": "HYD-3-REI", "jenis": "Hydropack", "nama": "Hydropack Rei 3L", "harga": 17000, "stok": 5},

    # 7. Jaket
    {"kode": "JKT-1-EIG", "jenis": "Jaket", "nama": "Jaket Gunung Eiger Windproof", "harga": 25000, "stok": 7},
    {"kode": "JKT-2-CON", "jenis": "Jaket", "nama": "Jaket Gunung Consina Mountain", "harga": 23000, "stok": 6},
    {"kode": "JKT-3-MTN", "jenis": "Jaket", "nama": "Jaket Elfs Mountain Pro", "harga": 23000, "stok": 5},

    # 8. Headlamp
    {"kode": "HL-1-EIG", "jenis": "Headlamp", "nama": "Headlamp Eiger X-Light", "harga": 10000, "stok": 8},
    {"kode": "HL-2-CON", "jenis": "Headlamp", "nama": "Headlamp Consina Beam", "harga": 9000, "stok": 6},
    {"kode": "HL-3-REI", "jenis": "Headlamp", "nama": "Headlamp Rei Flash", "harga": 9000, "stok": 7},

    # 9. Nesting
    {"kode": "NST-1-EIG", "jenis": "Nesting", "nama": "Nesting Eiger Cookset", "harga": 20000, "stok": 5},
    {"kode": "NST-2-CON", "jenis": "Nesting", "nama": "Nesting Consina Cookware", "harga": 18000, "stok": 6},
    {"kode": "NST-3-REI", "jenis": "Nesting", "nama": "Nesting Rei Outdoor Set", "harga": 19000, "stok": 2},

    # 10. Flysheet
    {"kode": "FLY-1-EIG", "jenis": "Flysheet", "nama": "Flysheet Eiger 3x4 m", "harga": 25000, "stok": 5},
    {"kode": "FLY-2-CON", "jenis": "Flysheet", "nama": "Flysheet Consina 3x4 m", "harga": 23000, "stok": 6},
    {"kode": "FLY-3-REI", "jenis": "Flysheet", "nama": "Flysheet Rei 4x6 m", "harga": 30000, "stok": 8},
]

# ==========================================
# Sub Menu READ Data Barang Alat Outdoor
# ==========================================
# Lihat sub menu read 
def menu_lihat_barang():
    while True:
        print()
        print("------- 📦 MENU LIHAT BARANG -------")
        print()
        print("1. Lihat semua barang")
        print("2. Lihat barang tertentu (berdasarkan kode)")
        print("3. Kembali")
        print()
        pilih = input(" Pilih menu (1-3): ")

        if pilih == "1":
            lihat_semua_barang()

        elif pilih == "2":
            lihat_barang_tertentu()

        elif pilih == "3":
            break

        else:
            print("❌ Pilihan tidak valid")

# lihat semua barang 
def lihat_semua_barang():
    if not alat_outdoor:
        print("📭 Daftar barang masih kosong")
        return

    print("\n" + "=" * 140)
    print("🌿 ARUNIKA OUTDOOR RENTAL 🌿".center(140))
    print("DAFTAR ALAT SEWA • 1 HARI".center(140))
    print("=" * 140)
    print(f"{'Kode':<14} {'Jenis Barang':<28} {'Nama Barang':<42} {'Harga (Rp)':>15} {'stok (pcs)': >15}")
    print("-" * 140)

    for barang in alat_outdoor:
        print(f"{barang['kode']:<14} "
              f"{barang['jenis']:<28} "
              f"{barang['nama']:<42} "
              f"{barang['harga']:>15,}"
              f"{barang['stok']:>15}")

# lihat barang berdasarkan input user (kode barang)
def lihat_barang_tertentu():
    if not alat_outdoor:
        print("📭 Daftar barang masih kosong")
        return

    kode = input("Masukkan kode barang: ").upper()

    for barang in alat_outdoor:
        if barang["kode"] == kode:
            print("\n✅ Barang ditemukan")
            print("-" * 40)
            print(f"Kode  : {barang['kode']}")
            print(f"Jenis : {barang['jenis']}")
            print(f"Nama  : {barang['nama']}")
            print(f"Harga : Rp {barang['harga']:,}")
            return

    print("❌ Barang dengan kode tersebut tidak ditemukan")


# ==========================================
# Sub Menu CREATE Buat Penyewaan
# ==========================================

def buat_penyewaan(userid):
    while True:
        transaksi_user = [t for t in data_penyewaan if t["userid"] == userid]

        # ================================
        # TEKS ADAPTIF (TAMPILAN)
        # ================================
        if transaksi_user:
            teks_menu_sewa = "Ajukan Penyewaan Tambahan"
            judul_sewa = "AJUKAN PENYEWAAN TAMBAHAN"
            info_user = "ℹ️   Anda telah memiliki transaksi sebelumnya."
        else:
            teks_menu_sewa = "Buat Penyewaan Baru"
            judul_sewa = "BUAT PENYEWAAN BARU"
            info_user = "ℹ️   Anda belum memiliki transaksi."

        print(f"\n{info_user}")

        # ================================
        # MENU UTAMA PENYEWAAN
        # ================================
        print("\n💰 ------- Menu Penyewaan -------")
        print()
        print(f"1. {teks_menu_sewa}")
        print("2. Kembali ke Menu Utama")

        pilih = input("Pilih menu (1-2): ")

        # =================================
        # BUAT PENYEWAAN BARU
        # =================================
        if pilih == "1":
            print()
            print(f"------- 📋 {judul_sewa} -------")
            print()
            kode_barang = input("Masukkan Kode Barang: ")

            barang_dipilih = None
            for alat in alat_outdoor:
                if alat["kode"] == kode_barang:
                    barang_dipilih = alat
                    break

            if barang_dipilih is None:
                print("❌ Barang tidak ditemukan.")
                continue

            if barang_dipilih["stok"] <= 0:
                print("⚠️   Maaf, stok barang habis.")
                continue

            print(
                f"Barang: {barang_dipilih['nama']} | "
                f"Stok: {barang_dipilih['stok']} | "
                f"Harga: Rp {barang_dipilih['harga']}"
            )

            # jumlah sewa
            while True:
                try:
                    jumlah = int(input("Masukkan jumlah barang: "))
                    if jumlah <= 0:
                        print("❌ Jumlah minimal 1.")
                    elif jumlah > barang_dipilih["stok"]:
                        print(f"❌ Melebihi stok. Sisa stok: {barang_dipilih['stok']}")
                    else:
                        break
                except ValueError:
                    print("❌ Input harus angka.")

            # lama sewa
            while True:
                try:
                    lama_sewa = int(input("Masukkan lama sewa (hari): "))
                    if lama_sewa > 0:
                        break
                    print("❌ Lama sewa minimal 1 hari.")
                except ValueError:
                    print("❌ Input harus angka.")

            total_harga = barang_dipilih["harga"] * jumlah * lama_sewa

            # konfirmasi
            print("\n------- Konfirmasi Sewa -------")
            print()
            print(f"Barang      : {barang_dipilih['nama']}")
            print(f"Jumlah      : {jumlah}")
            print(f"Lama Sewa   : {lama_sewa} hari")
            print(f"Total Harga : Rp {total_harga:,}")

            konfirmasi = input("Lanjutkan penyewaan? (Y/N): ").lower()

            if konfirmasi == "y":
                transaksi = {
                    "userid": userid,
                    "kode_barang": kode_barang,
                    "jumlah": jumlah,
                    "lama_sewa": lama_sewa,
                    "total_harga": total_harga
                }

                data_penyewaan.append(transaksi)
                barang_dipilih["stok"] -= jumlah
                print("\n✅ Transaksi berhasil disimpan.")
            else:
                print("\n❌ Transaksi dibatalkan.")

        # =================================
        # KEMBALI KE MENU UTAMA
        # =================================
        elif pilih == "2":
            return

        else:
            print("❌ Pilihan tidak valid.")



# ==========================================
# Sub Menu READ Riwayat Penyewaan
# ==========================================

def lihat_riwayat_sewa(userid):
    lebar_nama = 40
    lebar_jumlah = 8
    lebar_lama = 12
    lebar_total = 15

    total_lebar = 4 + lebar_nama + lebar_jumlah + lebar_lama + lebar_total  # total seluruh tabel

    print("\n" + "="*total_lebar)
    print("🌿 ARUNIKA RENTAL OUTDOOR 🌿".center(total_lebar))
    print("RIWAYAT PENYEWAAN".center(total_lebar))
    print("="*total_lebar + "\n")
    
    penyewaan_user = [t for t in data_penyewaan if t.get("userid") == userid]

    if not penyewaan_user:
        print("⚠️   Anda belum melakukan penyewaan apapun.\n".center(total_lebar))
    else:
        # header tabel
        print(f"{'No':<4}{'Nama Barang':<{lebar_nama}}{'Jumlah':<{lebar_jumlah}}{'Lama (hari)':<{lebar_lama}}{'Total (Rp)':>{lebar_total}}")
        print("-"*total_lebar)
        
        for idx, t in enumerate(penyewaan_user, start=1):
            kode = t["kode_barang"]
            jumlah = t["jumlah"]
            lama = t["lama_sewa"]
            total = t["total_harga"]
            
            nama_barang = next((a["nama"] for a in alat_outdoor if a["kode"] == kode), "Unknown")
            if len(nama_barang) > lebar_nama - 1:
                nama_barang = nama_barang[:lebar_nama-4] + "..."
            
            print(f"{idx:<4}{nama_barang:<{lebar_nama}}{jumlah:<{lebar_jumlah}}{lama:<{lebar_lama}}{total:>{lebar_total},}")

        total_semua = sum(t["total_harga"] for t in penyewaan_user)
        print("-"*total_lebar)
        # total semua tepat di kolom Total(Rp)
        print(f"{'Total Semua':<{total_lebar - lebar_total}}{total_semua:>{lebar_total},}")
        print("="*total_lebar)
        print("\n" + "Terima kasih telah menyewa!".center(total_lebar) + "\n")

    # Sub-menu
    while True:
        print("\n------- Menu Riwayat Penyewaan -------")
        print()
        print("1. Lihat Ulang Riwayat")
        print("2. Kembali ke Menu Utama")
        pilih = input("Pilih menu (1-2): ")

        if pilih == "1":
            lihat_riwayat_sewa(userid)
            break
        elif pilih == "2":
            return
        else:
            print("❌ Pilihan tidak valid. Silakan pilih lagi.")



    
# ==========================================
# Sub Menu UPDATE Penyewaan
# ==========================================

def ubah_penyewaan(userid):
    while True:
        print("\n------- ✏️  UBAH DATA PENYEWAAN -------\n")
        
        transaksi_user = [t for t in data_penyewaan if t["userid"] == userid]

        # Cek data
        if not transaksi_user:
            print("\n⚠️   Anda belum memiliki data penyewaan untuk diubah.")
            return

        # Menampilkan daftar
        print(f"{'ID':<4} {'Nama Barang':<35} {'Jml':<5} {'Lama':<5} {'Total':<10}")
        print("-" * 65)
        for idx, t in enumerate(transaksi_user, start=1):
            # Mencari nama barang dari kode
            nama = next((a["nama"] for a in alat_outdoor if a["kode"] == t["kode_barang"]), "Unknown")
            print(f"{idx:<4} {nama:<35} {t['jumlah']:<5} {t['lama_sewa']:<5} {t['total_harga']:<10,}")

        # Meminta ID yang akan diubah
        try:
            id_input = input("\nMasukkan ID penyewaan yang ingin diubah (0 untuk batal): ")
            if id_input == "0":
                return
            id_penyewaan = int(id_input)
        except ValueError:
            print("❌ Input harus berupa angka.")
            continue

        # Mencari data penyewaan berdasarkan ID
        if 1 <= id_penyewaan <= len(transaksi_user):
            index_transaksi = id_penyewaan - 1
            transaksi_temp = transaksi_user[index_transaksi] # Data copy untuk referensi
            
            target_trans = next((t for t in data_penyewaan if t == transaksi_temp), None)
            
            if not target_trans:
                print("❌ Terjadi kesalahan sistem saat memuat data.")
                continue
        else:
            print("❌ ID penyewaan tidak ditemukan.")
            continue

        alat = next((a for a in alat_outdoor if a["kode"] == target_trans["kode_barang"]), None)
        if not alat:
            print("❌ Data alat terkait tidak ditemukan di database.")
            continue

        print(f"\nData Saat Ini: {alat['nama']}")
        print(f"Jumlah Sewa: {target_trans['jumlah']} unit")
        print(f"Lama Sewa : {target_trans['lama_sewa']} hari")
        
        # Meminta data baru
        print("\nApa yang ingin diubah?")
        print()
        print("1. Jumlah Sewa")
        print("2. Lama Sewa")
        pilih_ubah = input("Pilih (1/2): ")

        new_jumlah = target_trans['jumlah']
        new_lama = target_trans['lama_sewa']
        valid_update = False
        stok_baru = alat['stok']

        if pilih_ubah == '1':
            while True:
                try:
                    input_jumlah = input("Masukkan jumlah baru: ")
                    new_jumlah = int(input_jumlah)
                    if new_jumlah <= 0:
                        print("❌ Jumlah minimal 1.")
                        continue
                    break
                except ValueError:
                    print("❌ Input harus berupa angka.")

            # cek data sama
            if new_jumlah == target_trans['jumlah']:
                print("\n⚠️  Jumlah sewa yang dimasukkan sama dengan data sebelumnya.")
                print("ℹ️  Tidak ada perubahan yang dilakukan.")
                continue

            stok_db = alat['stok']
            stok_sementara = stok_db + target_trans['jumlah']
            
            if new_jumlah > stok_sementara:
                print(f"❌ Stok tidak mencukupi untuk perubahan. Maksimal tambah: {stok_sementara}")
            else:
                stok_baru = stok_sementara - new_jumlah
                valid_update = True

        elif pilih_ubah == '2':
            while True:
                try:
                    input_lama = input("Masukkan lama sewa baru (hari): ")
                    new_lama = int(input_lama)
                    if new_lama <= 0:
                        print("❌ Lama sewa minimal 1 hari.")
                        continue
                    break
                except ValueError:
                    print("❌ Input harus berupa angka.")
            
                        # 🔴 TAMBAHAN: cek data sama
            if new_lama == target_trans['lama_sewa']:
                print("\n⚠️  Lama sewa yang dimasukkan sama dengan data sebelumnya.")
                print("ℹ️  Tidak ada perubahan yang dilakukan.")
                continue
            
            valid_update = True
        else:
            print("❌ Pilihan tidak valid.")
            continue

        if valid_update:
            total_baru = alat['harga'] * new_jumlah * new_lama
            
            print("\n------- Konfirmasi Perubahan -------")
            print()
            print(f"Barang       : {alat['nama']}")
            print(f"Jumlah       : {target_trans['jumlah']} -> {new_jumlah}")
            print(f"Lama Sewa    : {target_trans['lama_sewa']} -> {new_lama} hari")
            print(f"Total Harga  : Rp {target_trans['total_harga']:,} -> Rp {total_baru:,}")
            
            konfirmasi = input("Simpan perubahan? (Y/N): ").lower()
            if konfirmasi == 'y':
                target_trans['jumlah'] = new_jumlah
                target_trans['lama_sewa'] = new_lama
                target_trans['total_harga'] = total_baru
                alat['stok'] = stok_baru
                print()
                print("✅ Data berhasil diperbarui.")
            else:
                print("❌ Perubahan dibatalkan.")

        # Menu lanjutan
        while True:
            print("\n------- Menu Lanjutan -------")
            print()
            print("1. Ubah Penyewaan Lain")
            print("2. Kembali ke Menu Utama")
            pilih_menu = input("Pilih menu (1-2): ")
            if pilih_menu == "1":
                break
            elif pilih_menu == "2":
                return
            else:
                print("❌ Pilihan tidak valid.")


# ==========================================
# Sub Menu DELETE Penyewaan
# ==========================================

def batalkan_penyewaan(userid):
    while True:
        print("\n------- 🗑️  HAPUS DATA PENYEWAAN -------\n")

        # ambil transaksi milik user
        transaksi_user = [t for t in data_penyewaan if t["userid"] == userid]

        if not transaksi_user:
            print("⚠️   Anda belum memiliki data penyewaan.")
            return

        # tampilkan daftar penyewaan
        print(f"{'ID':<4} {'Nama Barang':<30} {'Jml':<5} {'Lama':<5} {'Total':<10}")
        print("-" * 60)
        for idx, t in enumerate(transaksi_user, start=1):
            nama = next(
                (a["nama"] for a in alat_outdoor if a["kode"] == t["kode_barang"]),
                "Unknown"
            )
            print(f"{idx:<4} {nama:<30} {t['jumlah']:<5} {t['lama_sewa']:<5} {t['total_harga']:<10,}")

        # pilih ID penyewaan
        pilihan = input("\nMasukkan ID penyewaan yang ingin dibatalkan (0 untuk kembali): ")

        if pilihan == "0":
            return

        if not pilihan.isdigit():
            print("❌ Input harus berupa angka.")
            continue

        id_pilih = int(pilihan)

        if not (1 <= id_pilih <= len(transaksi_user)):
            print("❌ ID penyewaan tidak valid.")
            continue

        transaksi_target = transaksi_user[id_pilih - 1]

        # cari alat terkait
        alat = next(
            (a for a in alat_outdoor if a["kode"] == transaksi_target["kode_barang"]),
            None
        )

        # konfirmasi
        print("\n------- KONFIRMASI PEMBATALAN -------")
        print()
        print(f"Barang    : {alat['nama'] if alat else 'Unknown'}")
        print(f"Jumlah    : {transaksi_target['jumlah']}")
        print(f"Lama Sewa : {transaksi_target['lama_sewa']} hari")
        print(f"Total     : Rp {transaksi_target['total_harga']:,}")

        konfirmasi = input("Yakin ingin membatalkan penyewaan ini? (Y/N): ").lower()

        if konfirmasi == "y":
            # kembalikan stok
            if alat:
                alat["stok"] += transaksi_target["jumlah"]

            # hapus data penyewaan
            data_penyewaan.remove(transaksi_target)
            print("\n✅ Penyewaan berhasil dibatalkan.")
        else:
            print("\n❌ Pembatalan dibatalkan.")

        # ===== MENU LANJUTAN =====
        print("\n------- Menu Lanjutan -------")
        print()
        print("1. Batalkan Penyewaan Lain")
        print("2. Kembali ke Menu Utama")
        lanjut = input("Pilih menu (1-2): ")

        if lanjut == "2":
            return
        elif lanjut == "1":
            continue
        else:
            print("❌ Pilihan tidak valid, kembali ke menu utama.")
            return


# ==========================================
# Sub Menu READ Data Personal
# ==========================================

def tampilkan_data_personal(userid):
    while True:
        print("\n------- DATA PERSONAL SAYA -------")
        print()
        
        # Mencari data user
        user_data = next((u for u in users if u["userid"] == userid), None)
        
        if not user_data:
            print("\nData user tidak ditemukan.")
            return False

        # Menampilkan data
        print(f"UserID   : {user_data['userid']}")
        print(f"Nama     : {user_data['nama']}")
        print(f"Email    : {user_data['email']}")
        print(f"Gender   : {user_data['gender']}")
        print(f"Usia     : {user_data['usia']}")
        print(f"Pekerjaan: {user_data['pekerjaan']}")
        print(f"Hobi     : {user_data['hobi']}")
        print(f"No HP    : {user_data['nohp']}")
        print("Alamat   :")
        print(f"  Kota    : {user_data['alamat']['kota']}")
        print(f"  RT/RW   : {user_data['alamat']['rt']}/{user_data['alamat']['rw']}")
        print(f"  Zip Code: {user_data['alamat']['zipc']}")
        print("Koordinat :")
        print(f"  Lat     : {user_data['geo']['lat']}")
        print(f"  Lon     : {user_data['geo']['lon']}")

        # MENU LANJUTAN
        print("\n─────────────────────────────")
        print("1. Ubah Data (ID & Password)")
        print("2. Hapus Akun")
        print("3. Kembali ke Menu Utama")
        print("─────────────────────────────")
        
        pilih = input("Pilih Menu (1-3): ")

        if pilih == "1":
            ubah_data_personal(userid)
        elif pilih == "2":
            # Jika hapus akun berhasil (return True)
            if hapus_akun(userid):
                return True  
        elif pilih == "3":
            return False  
            
        else:
            print("❌ Pilihan tidak valid")

# UPDATE Data Personal 

def ubah_data_personal(userid):
    user = next((u for u in users if u["userid"] == userid), None)
    if not user:
        print("❌ Data user tidak ditemukan.")
        return

    while True:
        print("\n------- UBAH DATA PERSONAL -------")
        print()
        print("Data yang bisa diubah:")
        print(f"1. UserID  : {user['userid']}")
        print(f"2. Password: {'*' * len(user['password'])}")
        print("0. Kembali")

        pilih = input("Pilih data yang ingin diubah: ")

        if pilih == "1":
            # Ubah UserID
            print("\n------- Update User ID -------")
            print()
            while True:
                new_userid = input("Masukkan User ID Baru: ")

                if len(new_userid) < 6 or len(new_userid) > 20:
                    print("❌ User Id minimal 6 karakter dan maksimal 20 karakter")
                    continue

                if not is_alnum(new_userid):
                    print("❌ User Id hanya boleh huruf dan angka")
                    continue

                has_letter = False
                has_digit = False
                for c in new_userid:
                    if c.isalpha():
                        has_letter = True
                    elif c.isdigit():
                        has_digit = True
                
                if not (has_letter and has_digit):
                    print("❌ User Id harus mengandung huruf dan angka")
                    continue

                is_duplicate = False
                for u in users:
                    if u["userid"] == new_userid and u["userid"] != userid:
                        print("❌ User ID sudah digunakan oleh pengguna lain.")
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    confirm = input(f"Ubah UserID dari '{userid}' ke '{new_userid}'? (Y/N): ").lower()
                    if confirm == 'y':
                        user['userid'] = new_userid
                        print()
                        print("✅ User ID berhasil diubah.")
                        break # Keluar loop input

        elif pilih == "2":
            # Ubah Password
            print("\n------- Update Password -------")
            print()
            password_baru = input_password()
            confirm = input("Ubah Password? (Y/N): ").lower()
            if confirm == 'y':
                user['password'] = password_baru
                print()
                print("✅ Password berhasil diubah.")

        elif pilih == "0":
            break
        
        else:
            print()
            print("❌ Pilihan tidak valid.")

# Sub Menu DELETE Akun 

def hapus_akun(userid):
    print("\n PERINGATAN: Akun akan dihapus permanen!")
    
    konfirmasi = input("Yakin ingin menghapus akun ini? (Y/N): ").lower()

    if konfirmasi == 'y':
        for i in range(len(users)):
            if users[i]['userid'] == userid:
                del users[i]  # Hapus user dari list
                print()
                print("✅ Akun berhasil dihapus.")
                print("\nAnda telah keluar. Terima kasih! 🌿")
                return True
    else:
        print()
        print("❌ Penghapusan dibatalkan.")
    
    return False

# ==========================================
# Menu Penyewa
# ==========================================

def menu_penyewa(userid):
    while True:
        show_penyewa_menu()
        pilih = input("Pilih Menu (1-7): ")
        
        if pilih == "1":
            menu_lihat_barang()
        elif pilih == "2":
            buat_penyewaan(userid)
        elif pilih == "3":
            lihat_riwayat_sewa(userid)
        elif pilih == "4":
            ubah_penyewaan(userid)
        elif pilih == "5":
            batalkan_penyewaan(userid)
        elif pilih == "6":
            akun_terhapus = tampilkan_data_personal(userid)
            if akun_terhapus:
                break
        elif pilih == "7":
            print()
            print("Anda telah keluar. Terima kasih! 🌿")
            break
        else:
            print()
            print("❌ Pilihan tidak valid")

# ==========================================
# Menu
# ==========================================
def menu():
    while True:
        show_menu()
        pilih = input("\n Pilih menu (1-3) : ")

        if pilih == "1":
            register()
        elif pilih == "2":
            user_login = login()
            if user_login:
                menu_penyewa(user_login)
        elif pilih == "3":
            print()
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print()
            print("❌ Pilihan tidak valid")

# ==========================================
# RUN PROGRAM
# ==========================================
menu()