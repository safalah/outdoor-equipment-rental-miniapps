# ==========================================
# DATA STORAGE
# ==========================================
# Data inisiasi user
users = [
    {
        "userid": "owner01", 
        "password": "Owner@1234", 
        "email": "owner1@arunika.com",
        "role": "Admin",
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
        "role": "Renter",
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

# =====================================================
# LIST DATA ALAT OUTDOOR ARUNIKA
# Digunakan untuk:
# - Menampilkan daftar alat sewa
# - Pencarian alat berdasarkan kode barang
# - Harga berlaku untuk sewa 1 hari
# =====================================================
alat_outdoor = [
    # 1. Carrier
    {"kode": "CARR-1-REI", "jenis": "Carrier", "nama": "Arei Toba Carrier 80L", "harga": 40000, "stok": 7},
    {"kode": "CARR-2-CON", "jenis": "Carrier", "nama": "Consina Tarebbi Carrier 60L", "harga": 30000, "stok": 5},
    {"kode": "CARR-3-EIG", "jenis": "Carrier", "nama": "Eiger Streamline 45L", "harga": 35000, "stok": 8},

    # 2. Tent
    {"kode": "TEN-1-2P", "jenis": "Tent", "nama": "Consina 2-Person Tent", "harga": 45000, "stok": 1},
    {"kode": "TEN-2-4P", "jenis": "Tent", "nama": "Eiger 4-Person Tent", "harga": 60000, "stok": 5},
    {"kode": "TEN-3-8P", "jenis": "Tent", "nama": "Rei 8-Person Tent", "harga": 70000, "stok": 7},

    # 3. Shoes
    {"kode": "SPT-1-EIG", "jenis": "Shoes", "nama": "Eiger X-Trek Mountain Shoes", "harga": 35000, "stok": 2},
    {"kode": "SPT-2-ARE", "jenis": "Shoes", "nama": "Arei Ventura Mountain Shoes", "harga": 30000, "stok": 6},
    {"kode": "SPT-3-CON", "jenis": "Shoes", "nama": "Consina Alpine Mountain Shoes", "harga": 32000, "stok": 5},

    # 4. Sleeping Bag
    {"kode": "SB-1-ARC", "jenis": "Sleeping Bag", "nama": "Leuser Arctic Sleeping Bag", "harga": 16500, "stok": 6},
    {"kode": "SB-2-EXP", "jenis": "Sleeping Bag", "nama": "Avtech Explorer Sleeping Bag", "harga": 15000, "stok": 7},
    {"kode": "SB-3-POL", "jenis": "Sleeping Bag", "nama": "Rei Polar Sleeping Bag", "harga": 18000, "stok": 3},

    # 5. Trekking Pole
    {"kode": "TP-1-EIG", "jenis": "Trekking Pole", "nama": "Eiger Carbon Trekking Pole", "harga": 10000, "stok": 5},
    {"kode": "TP-2-CON", "jenis": "Trekking Pole", "nama": "Consina Alpine Trekking Pole", "harga": 10000, "stok": 7},
    {"kode": "TP-3-REI", "jenis": "Trekking Pole", "nama": "Rei Explorer Trekking Pole", "harga": 10000, "stok": 6},

    # 6. Hydropack
    {"kode": "HYD-1-EIG", "jenis": "Hydropack", "nama": "Eiger 2L Hydropack", "harga": 15000, "stok": 8},
    {"kode": "HYD-2-CON", "jenis": "Hydropack", "nama": "Consina 2L Hydropack", "harga": 13000, "stok": 6},
    {"kode": "HYD-3-REI", "jenis": "Hydropack", "nama": "Rei 3L Hydropack", "harga": 17000, "stok": 5},

    # 7. Jacket
    {"kode": "JKT-1-EIG", "jenis": "Jacket", "nama": "Eiger Windproof Mountain Jacket", "harga": 25000, "stok": 7},
    {"kode": "JKT-2-CON", "jenis": "Jacket", "nama": "Consina Mountain Jacket", "harga": 23000, "stok": 6},
    {"kode": "JKT-3-MTN", "jenis": "Jacket", "nama": "Elfs Mountain Pro Jacket", "harga": 23000, "stok": 5},

    # 8. Headlamp
    {"kode": "HL-1-EIG", "jenis": "Headlamp", "nama": "Eiger X-Light Headlamp", "harga": 10000, "stok": 8},
    {"kode": "HL-2-CON", "jenis": "Headlamp", "nama": "Consina Beam Headlamp", "harga": 9000, "stok": 6},
    {"kode": "HL-3-REI", "jenis": "Headlamp", "nama": "Rei Flash Headlamp", "harga": 9000, "stok": 7},

    # 9. Nesting
    {"kode": "NST-1-EIG", "jenis": "Nesting", "nama": "Eiger Cookset Nesting", "harga": 20000, "stok": 5},
    {"kode": "NST-2-CON", "jenis": "Nesting", "nama": "Consina Cookware Nesting", "harga": 18000, "stok": 6},
    {"kode": "NST-3-REI", "jenis": "Nesting", "nama": "Rei Outdoor Set Nesting", "harga": 19000, "stok": 2},

    # 10. Flysheet
    {"kode": "FLY-1-EIG", "jenis": "Flysheet", "nama": "Eiger 3x4 m Flysheet", "harga": 25000, "stok": 5},
    {"kode": "FLY-2-CON", "jenis": "Flysheet", "nama": "Consina 3x4 m Flysheet", "harga": 23000, "stok": 6},
    {"kode": "FLY-3-REI", "jenis": "Flysheet", "nama": "Rei 4x6 m Flysheet", "harga": 30000, "stok": 8},
]


data_penyewaan = [] 