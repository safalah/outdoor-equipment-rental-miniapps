# ==========================================
# ADMIN MAIN MENU (2) Rental Management
# ==========================================
from Database import get_all_rentals, get_rentals_by_status, delete_rental, get_equipment, get_user
width = 60

# Fungsi helper untuk menampilkan penyewaan berdasarkan status
def view_rent_by_status_admin(status_filter):
    lebar_nama = 40
    lebar_renter = 15
    lebar_jumlah = 6
    lebar_lama = 12
    lebar_total = 13
    total_lebar = 7 + lebar_renter + lebar_nama + lebar_jumlah + lebar_lama + lebar_total + 15

    penyewaan_filtered = get_rentals_by_status(status_filter)

    print("\n" + "="*total_lebar)
    print("🌿 ARUNIKA RENTAL OUTDOOR 🌿".center(total_lebar))
    print(f"RENTAL DATA ({status_filter.upper()})".center(total_lebar))
    print("="*total_lebar)

    if not penyewaan_filtered:
        print(f"⚠️  No {status_filter} rentals found.".center(total_lebar))
        return

    # Header tabel
    print(f"| {'No':<3} | {'Renter':<{lebar_renter}} | {'Equipment Name':<{lebar_nama}} | {'Qty':<{lebar_jumlah}} | {'Days':<{lebar_lama}} | {'Total (Rp)':<{lebar_total}} |")
    print("-"*total_lebar)

    for idx, t in enumerate(penyewaan_filtered, start=1):
        user = get_user(t["userid"])
        renter = user["nama"] if user else "Unknown"
        kode = t["kode_barang"]
        barang = get_equipment(kode)
        nama_barang = barang["nama"] if barang else "Unknown"
        if len(nama_barang) > lebar_nama - 1:
            nama_barang = nama_barang[:lebar_nama-4] + "..."
        print(f"| {idx:<3} | {renter:<{lebar_renter}} | {nama_barang:<{lebar_nama}} | {t['jumlah']:<{lebar_jumlah}} | {t['lama_sewa']:<{lebar_lama}} | {t['total_harga']:<{lebar_total},} |")

    print("="*total_lebar)


def display_all_rent():
    lebar_nama = 40
    lebar_renter = 15
    lebar_status = 10
    lebar_jumlah = 6
    lebar_lama = 12
    lebar_total = 10

    total_lebar = 5 + lebar_renter + lebar_status + lebar_nama + lebar_jumlah + lebar_lama + lebar_total + 20

    print("\n" + "="*total_lebar)
    print("🌿 ARUNIKA RENTAL OUTDOOR 🌿".center(total_lebar))
    print("ALL RENTAL DATA".center(total_lebar))
    print("="*total_lebar)

    data_penyewaan = get_all_rentals()
    if not data_penyewaan:
        print("⚠️   No rental data available.".center(total_lebar))
        return

    # Header tabel
    print(f"| {'No':<3} | {'Renter':<{lebar_renter}} | {'Status':<{lebar_status}} | {'Equipment Name':<{lebar_nama}} | {'Qty':<{lebar_jumlah}} | {'Days':<{lebar_lama}} | {'Total (Rp)':<{lebar_total}} |")
    print("-"*total_lebar)

    for idx, t in enumerate(data_penyewaan, start=1):
        user = get_user(t["userid"])
        renter = user["nama"] if user else "Unknown"
        status = t.get("status", "N/A")
        kode = t["kode_barang"]
        barang = get_equipment(kode)
        nama_barang = barang["nama"] if barang else "Unknown"
        if len(nama_barang) > lebar_nama - 1:
            nama_barang = nama_barang[:lebar_nama-4] + "..."
        jumlah = t["jumlah"]
        lama = t["lama_sewa"]
        total = t["total_harga"]

        print(f"| {idx:<3} | {renter:<{lebar_renter}} | {status:<{lebar_status}} | {nama_barang:<{lebar_nama}} | {jumlah:<{lebar_jumlah}} | {lama:<{lebar_lama}} | {total:<{lebar_total},} |")

    print("="*total_lebar)

def view_all_rent():
    display_all_rent()
    # Sub-menu admin
    while True:
        print("\n" + "=" * width)
        print("RENTS MANAGEMENT".center(width))
        print("=" * width)

        print()
        print("1. View Active Rentals")
        print("2. View Returned Rentals")
        print("3. View Cancelled Rentals")
        print("0. Back to Main Menu")
        print()

        print("=" * width)
        pilih = input("Select option (0-3): ")
        if pilih == "1":
            view_rent_by_status_admin("active")
        elif pilih == "2":
            view_rent_by_status_admin("returned")
        elif pilih == "3":
            view_rent_by_status_admin("cancelled")
        elif pilih == "0":
            return
        else:
            print("❌ Invalid choice. Please select again.")



def delete_rent_by_status(status_filter):
    lebar_nama = 40
    lebar_renter = 15
    lebar_jumlah = 6
    lebar_lama = 12
    lebar_total = 12
    total_lebar = 5 + lebar_renter + lebar_nama + lebar_jumlah + lebar_lama + lebar_total + 15

    # Filter data yang sesuai status
    penyewaan_filtered = get_rentals_by_status(status_filter)

    if not penyewaan_filtered:
        print(f"\n⚠️  No {status_filter} rentals to delete.".center(total_lebar))
        return

    print("\n" + "="*total_lebar)
    print(f"🌿 ARUNIKA RENTAL OUTDOOR 🌿".center(total_lebar))
    print(f"DELETE RENTALS ({status_filter.upper()})".center(total_lebar))
    print("="*total_lebar + "\n")

    # Tampilkan daftar sewa
    print(f"| {'No':<3} | {'Renter':<{lebar_renter}} | {'Equipment Name':<{lebar_nama}} | {'Qty':<{lebar_jumlah}} | {'Days':<{lebar_lama}} | {'Total (Rp)':>{lebar_total}} |")
    print("-"*total_lebar)

    for idx, t in enumerate(penyewaan_filtered, start=1):
        user = get_user(t["userid"])
        renter = user["nama"] if user else "Unknown"
        kode = t["kode_barang"]
        barang = get_equipment(kode)
        nama_barang = barang["nama"] if barang else "Unknown"
        if len(nama_barang) > lebar_nama - 1:
            nama_barang = nama_barang[:lebar_nama-4] + "..."
        print(f"| {idx:<3} | {renter:<{lebar_renter}} | {nama_barang:<{lebar_nama}} | {t['jumlah']:<{lebar_jumlah}} | {t['lama_sewa']:<{lebar_lama}} | {t['total_harga']:>{lebar_total},} |")

    print("="*total_lebar)

    # Pilih nomor sewa yang ingin dihapus
    while True:
        pilih = input("\nEnter rental No to delete (or '0' to cancel): ")
        if pilih == "0":
            print("❌ Cancel deletion.")
            return
        if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(penyewaan_filtered):
            print("❌ Invalid number. Please select again.")
            continue

        idx_delete = int(pilih) - 1
        rent_to_delete = penyewaan_filtered[idx_delete]
        delete_rental(rent_to_delete['id_transaksi'], rent_to_delete['userid'], rent_to_delete['kode_barang'])

        # Ambil nama renter dari database
        user = get_user(rent_to_delete['userid'])
        renter_name = user["nama"] if user else "Unknown"

        print(f"✅ Rental '{rent_to_delete['kode_barang']}' for renter '{renter_name}' has been deleted.")
        break

def delete_rent():
    # Sub-menu admin
    while True:
        display_all_rent()
        print("\n" + "=" * width)
        print("ADMIN MENU DELETE RENT".center(width))
        print("=" * width)

        print()
        print("1. Delete Returned Rentals")
        print("2. Delete Cancelled Rentals")
        print("0. Back to Main Menu")
        print()

        print("=" * width)
        pilih = input("Select option (0-2): ")
        if pilih == "1":
            delete_rent_by_status("returned")
        elif pilih == "2":
            delete_rent_by_status("cancelled")
        elif pilih == "0":
            return
        else:
            print("❌ Invalid choice. Please select again.")

            
# Admin Sub Menu: Rents Management
# ------------------------------------
def menu_admin_rents():
    while True:
        width = 60
        print("\n" + "=" * width)
        print("RENTS MANAGEMENT".center(width))
        print("=" * width)

        print()
        print("  [1] View All Rentals")
        print("  [2] Delete Rentals")
        print("  [0] Back")
        print()

        print("=" * width)
        pilih = input("Select menu (0-2): ")
        if pilih == "1":
            view_all_rent()
        elif pilih == "2":
            delete_rent()
        elif pilih == "0":
            print()
            break
        else:
            print()
            print("❌ Invalid input!")
