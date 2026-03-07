from Database import get_user_rentals, get_equipment, get_user
# ==========================================
# Sub Menu READ Riwayat Penyewaan
# ==========================================
import datetime

def view_invoice(userid):
    lebar_nama = 40
    lebar_jumlah = 8
    lebar_lama = 12
    lebar_total = 15
    
    total_lebar = 4 + lebar_nama + lebar_jumlah + lebar_lama + lebar_total + 15  # tambah 5 untuk garis vertikal2
    tanggal_sewa = str(datetime.date.today())
    user_data = get_user(userid)
    penyewaan_user = get_user_rentals(userid, "active")

    print("\n" + "="*total_lebar)
    print("🌿 ARUNIKA RENTAL OUTDOOR 🌿".center(total_lebar))
    print("INVOICE".center(total_lebar))
    print("="*total_lebar)
    print()
    print(f"RENTER      : {user_data['nama']}")
    print("RENTAL DATE : " + tanggal_sewa)
    if penyewaan_user:
        id_aktif = penyewaan_user[0].get("id_transaksi", "N/A")
        print(f"TRANSACTION ID : {id_aktif}")
        
    print("="*total_lebar)
    if not penyewaan_user:
        print("⚠️   You have not made any rentals yet.\n".center(total_lebar))
    else:
        # header tabel dengan garis vertikal
        print(f"| {'No':<3} | {'Equipment Name':<{lebar_nama}} | {'Quantity':<{lebar_jumlah}} | {'Duration (days)':<{lebar_lama}} | {'Total (Rp)':<{lebar_total - 3}} |")
        print("-"*total_lebar)
        
        for idx, t in enumerate(penyewaan_user, start=1):
            kode = t["kode_barang"]
            jumlah = t["jumlah"]
            lama = t["lama_sewa"]
            total = t["total_harga"]
            
            barang = get_equipment(kode)
            nama_barang = barang["nama"] if barang else "Unknown"
            if len(nama_barang) > lebar_nama - 1:
                nama_barang = nama_barang[:lebar_nama-4] + "..."
            
            print(f"| {idx:<3} | {nama_barang:<{lebar_nama}} | {jumlah:<{lebar_jumlah}} | {lama:<{lebar_lama + 3}} | {total:<{lebar_total - 3},} |")

        total_semua = sum(t["total_harga"] for t in penyewaan_user)
        print("-"*total_lebar)
        # total semua tepat di kolom Total(Rp)
        print(f"| {'Grand Total':<{total_lebar - lebar_total - 4}}{total_semua:>{lebar_total},} |")
        print("="*total_lebar)
        print("\n" + "Thank you for renting!".center(total_lebar) + "\n")

    # Sub-menu
    while True:
        width = 60
        print("\n" + "=" * width)
        print("INVOICE".center(width))
        print("=" * width)

        print()
        print("1. View Invoice Again")
        print("0. Back to Main Menu")
        print()

        print("=" * width)
        pilih = input("Select option (0-1): ")

        if pilih == "1":
            view_invoice(userid)
            break
        elif pilih == "0":
            return
        else:
            print("❌ Invalid choice. Please select again.")
