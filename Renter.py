from Equipment_Management import lihat_barang_tertentu, lihat_semua_barang
from Database import get_equipment, update_equipment, add_rental, get_user_rentals, update_rental, update_rental_status, get_last_transaction_id

counter_id_transaksi = 0
width = 60
# ==========================================
# Sub Menu READ Data Barang Alat Outdoor
# ==========================================
# Lihat sub menu read 
def menu_lihat_barang():
    while True:
        print("\n" + "=" * width)
        print("📦 VIEW EQUIPMENT MENU".center(width))
        print("=" * width)

        print()
        print("1. View all equipment")
        print("2. View specific equipment (by code)")
        print("0. Back")
        print()

        print("=" * width)
        pilih = input("Select option (0-2): ")

        if pilih == "1":
            lihat_semua_barang()

        elif pilih == "2":
            lihat_barang_tertentu()

        elif pilih == "0":
            break

        else:
            print("❌ Invalid choice")


def buat_penyewaan(userid):
    global counter_id_transaksi # Akses variabel global counter
    
    # Inisialisasi counter dari database jika masih 0
    if counter_id_transaksi == 0:
        last_id = get_last_transaction_id()
        if last_id and last_id.startswith("arunika"):
            try:
                counter_id_transaksi = int(last_id.replace("arunika", ""))
            except:
                counter_id_transaksi = 0

    while True:
        transaksi_user = get_user_rentals(userid)

        # ================================
        # TEKS ADAPTIF (TAMPILAN)
        # ================================
        if transaksi_user:
            teks_menu_sewa = "Submit Additional Rental"
            judul_sewa = "SUBMIT ADDITIONAL RENTAL"
            info_user = "ℹ️   You have previous transactions."
        else:
            teks_menu_sewa = "Create New Rental"
            judul_sewa = "CREATE NEW RENTAL"
            info_user = "ℹ️   You do not have any transactions yet."

        print(f"\n{info_user}")

        # ================================
        # MENU UTAMA PENYEWAAN
        # ================================
        print("\n" + "=" * width)
        print("💰 CREATE RENTAL".center(width))
        print("=" * width)
        
        print()
        print(f"1. {teks_menu_sewa}")
        print("0. Back to Main Menu")
        print()

        print("=" * width)
        pilih = input("Select option (0-1): ")

        # =================================
        # BUAT PENYEWAAN BARU
        # =================================
        if pilih == "1":
            print("\n" + "=" * width)
            print(f"📋 {judul_sewa}".center(width))
            print("=" * width)
            print()

            kode_barang = input("Enter Equipment Code: ")

            barang_dipilih = get_equipment(kode_barang)

            if barang_dipilih is None:
                print("❌ Equipment not found.")
                continue

            if barang_dipilih["stok"] <= 0:
                print("⚠️   Sorry, Equipment is out of stock.")
                continue

            print(
                f"Equipment: {barang_dipilih['nama']} | "
                f"Stock: {barang_dipilih['stok']} | "
                f"Price: Rp {barang_dipilih['harga']}"
            )

            # jumlah sewa
            while True:
                try:
                    jumlah = int(input("Enter Equipment quantity: "))
                    if jumlah <= 0:
                        print("❌ Minimum quantity is 1.")
                    elif jumlah > barang_dipilih["stok"]:
                        print(f"❌ Exceeds stock. Remaining stock: {barang_dipilih['stok']}")
                    else:
                        break
                except ValueError:
                    print("❌ Input must be a number.")

            # lama sewa
            while True:
                try:
                    lama_sewa = int(input("Enter rental duration (days): "))
                    if lama_sewa > 0:
                        break
                    print("❌ Minimum rental duration is 1 day.")
                except ValueError:
                    print("❌ Input must be a number.")

            total_harga = barang_dipilih["harga"] * jumlah * lama_sewa

            # konfirmasi
            print("\n------- Rental Confirmation -------")
            print()
            print(f"Equipment        : {barang_dipilih['nama']}")
            print(f"Quantity    : {jumlah}")
            print(f"Duration    : {lama_sewa} days")
            print(f"Total Price : Rp {total_harga:,}")

            # CEK DUPLIKASI
            duplikasi = False
            for t in transaksi_user:
                if (
                    t["kode_barang"] == kode_barang and
                    t["jumlah"] == jumlah and
                    t["lama_sewa"] == lama_sewa and
                    t["status"] == "active"
                ):
                    duplikasi = True
                    break

            if duplikasi:
                print("\n⚠️   This Equipment with the same quantity and duration is already added in your active rentals. Please choose another Equipment or modify quantity/duration.")
                continue  # Kembali ke input Equipment baru

            # =========================
            # KONFIRMASI TRANSAKSI
            # =========================
            while True:
                konfirmasi = input("Proceed with rental? (Y/N): ").lower()

                if konfirmasi == "y":
                    # === LOGIKA ID TRANSAKSI ===
                    # Cek apakah user punya transaksi aktif (barang belum dikembalikan)
                    # Jika punya, pakai ID lama. Jika tidak, buat ID baru.
                    transaksi_aktif = [t for t in transaksi_user if t['status'] == 'active']
                    if transaksi_aktif:
                        # Ambil ID dari transaksi sebelumnya (asumsi 1 user 1 ID aktif)
                        id_transaksi = transaksi_aktif[0]["id_transaksi"]
                    else:
                        # Buat ID Baru
                        counter_id_transaksi += 1
                        id_transaksi = f"arunika{counter_id_transaksi:02d}" # Format arunika01, 02...
                    # ============================

                    add_rental(id_transaksi, userid, kode_barang, jumlah, lama_sewa, total_harga, "active")
                    # Update stok di DB
                    new_stok = barang_dipilih["stok"] - jumlah
                    update_equipment(barang_dipilih['kode'], barang_dipilih['jenis'], barang_dipilih['nama'], barang_dipilih['harga'], new_stok)
                    
                    print("\n✅ Transaction saved successfully.")
                    display_rentals(userid)
                    break

                elif konfirmasi == "n":
                    print("\n❌ Transaction cancelled.")
                    break

                else:
                    print("❌ Invalid input! Enter Y or N.")

        # =================================
        # KEMBALI KE MENU UTAMA
        # =================================
        elif pilih == "0":
            return

        else:
            print("❌ Invalid choice.")


# Tabel for show data transaction 
def display_rentals(userid):
    transaksi_user = get_user_rentals(userid, "active")
    
    # tampilkan daftar penyewaan
    lebar_kode = 12
    lebar_nama = 35
    lebar_qty = 5
    lebar_days = 5
    lebar_total = 15  # lebih lebar untuk total harga

    # Garis atas tabel
    print(f"┌{'─'*lebar_kode}┬{'─'*lebar_nama}┬{'─'*lebar_qty}┬{'─'*lebar_days}┬{'─'*lebar_total}┐")
    # Header
    print(f"│ {'Code':^{11}}│ {'Equipment Name':^{34}}│ {'Qty':^{4}}│ {'Days':^{4}}│ {'Total (Rp)':^{14}}│")
    # Garis header-isi
    print(f"├{'─'*lebar_kode}┼{'─'*lebar_nama}┼{'─'*lebar_qty}┼{'─'*lebar_days}┼{'─'*lebar_total}┤")

    # Isi tabel
    for t in transaksi_user:
        barang = get_equipment(t["kode_barang"])
        nama = barang["nama"] if barang else "Unknown"
        print(f"│ {t['kode_barang']:^{11}}│ {nama:^{34}}│ {t['jumlah']:^{4}}│ {t['lama_sewa']:^{4}}│ {t['total_harga']:^{14},}│")

    # Garis bawah tabel
    print(f"└{'─'*lebar_kode}┴{'─'*lebar_nama}┴{'─'*lebar_qty}┴{'─'*lebar_days}┴{'─'*lebar_total}┘")

# ==========================================
# Sub Menu UPDATE Penyewaan
# ==========================================
def ubah_penyewaan(userid):
    while True:
        print("\n" + "=" * width)
        print("✏️  UPDATE RENTAL DATA".center(width))
        print("=" * width)

        print()
        transaksi_user = get_user_rentals(userid, "active")

        # Cek data
        if not transaksi_user:
            print("\n⚠️   You do not have any rental data to update.")
            return

        # Menampilkan daftar
        display_rentals(userid)

        # Input Kode Barang
        kode_input = input("\nEnter Equipment Code to change (0 to cancel): ").upper()
        if kode_input == "0":
            return

        # Cari transaksi berdasarkan kode
        target_list = [t for t in transaksi_user if t["kode_barang"] == kode_input]

        if not target_list:
            print("❌ Equipment code not found in your rentals.")
            continue

        target_trans = None
        if len(target_list) > 1:
            print(f"\n⚠️  Found {len(target_list)} transactions with code {kode_input}.")
            print("Select specific transaction:")
            for i, t in enumerate(target_list, 1):
                print(f"{i}. Qty: {t['jumlah']}, Duration: {t['lama_sewa']} days, Total: {t['total_harga']}")
            try:
                idx_pilih = int(input("Select number (1-{}): ".format(len(target_list)))) - 1
                if 0 <= idx_pilih < len(target_list):
                    target_trans = target_list[idx_pilih]
                else:
                    print("❌ Invalid choice.")
                    continue
            except ValueError:
                print("❌ Input must be a number.")
                continue
        else:
            target_trans = target_list[0]

        alat = get_equipment(target_trans["kode_barang"])
        if not alat:
            print("❌ Related equipment data not found in database.")
            continue
        print()

        # LOOP MENU PILIHAN PERUBAHAN
        while True:
            print("-" * width)
            print("\nWhat do you want to change?")
            print()
            print("1. Rental Quantity")
            print("2. Rental Duration")
            print("3. Both Quantity & Duration")
            print("=" * width)
            pilih_ubah = input("Select (1/2/3): ")

            if pilih_ubah not in ['1', '2', '3']:
                print("❌ Invalid choice. Please select 1, 2, or 3.")
                continue  # langsung loop ke menu pilihan

            # inisialisasi nilai baru
            new_jumlah = target_trans['jumlah']
            new_lama = target_trans['lama_sewa']
            valid_update = False
            stok_baru = alat['stok']

            # Ubah Quantity
            if pilih_ubah in ['1', '3']:
                print()
                while True:
                    try:
                        input_jumlah = input("Enter new quantity: ")
                        new_jumlah = int(input_jumlah)
                        if new_jumlah <= 0:
                            print("❌ Minimum quantity is 1.")
                            continue
                        break
                    except ValueError:
                        print("❌ Input must be a number.")

                if new_jumlah != target_trans['jumlah']:
                    stok_sementara = alat['stok'] + target_trans['jumlah']
                    if new_jumlah > stok_sementara:
                        print(f"❌ Insufficient stock for change. Max addition: {stok_sementara}")
                        continue  # kembali ke menu pilihan
                    else:
                        stok_baru = stok_sementara - new_jumlah
                        valid_update = True
                elif pilih_ubah == '1':
                    print("\n⚠️  The rental quantity entered is the same as the previous data.")
                    print("ℹ️  No changes made.")
                    continue

            # Ubah Duration
            if pilih_ubah in ['2', '3']:
                print()
                while True:
                    try:
                        input_lama = input("Enter new rental duration (days): ")
                        new_lama = int(input_lama)
                        if new_lama <= 0:
                            print("❌ Minimum rental duration is 1 day.")
                            continue
                        break
                    except ValueError:
                        print("❌ Input must be a number.")

                if new_lama != target_trans['lama_sewa']:
                    valid_update = True
                elif pilih_ubah == '2':
                    print("\n⚠️  The rental duration entered is the same as the previous data.")
                    print("ℹ️  No changes made.")
                    continue

            # Jika ada perubahan valid, tampilkan konfirmasi
            if valid_update:
                total_baru = alat['harga'] * new_jumlah * new_lama

                print("\n------- Change Confirmation -------")
                print()
                print(f"Equipment       : {alat['nama']}")
                print(f"Quantity   : {target_trans['jumlah']} -> {new_jumlah}")
                print(f"Duration   : {target_trans['lama_sewa']} -> {new_lama} days")
                print(f"Total Price: Rp {target_trans['total_harga']:,} -> Rp {total_baru:,}")

                while True:
                    konfirmasi = input("Save changes? (Y/N): ").lower()
                    if konfirmasi == 'y':
                        # Update rental in DB
                        update_rental(target_trans['id_transaksi'], userid, target_trans['kode_barang'], new_jumlah, new_lama, total_baru, target_trans['status'])
                        # Update stok in DB
                        update_equipment(alat['kode'], alat['jenis'], alat['nama'], alat['harga'], stok_baru)
                        
                        print("\n✅ Data updated successfully.")
                        display_rentals(userid)
                        break
                    elif konfirmasi == 'n':
                        print("❌ Change cancelled.")
                        break
                    else:
                        print("❌ Invalid input! Enter Y or N.")

            # Menu lanjutan setelah update
            while True:
                print("\n------- Rental Options -------")
                print()
                print("1. Update Another Rental")
                print("0. Back to Main Menu")
                pilih_menu = input("Select option (0-1): ")
                if pilih_menu == "1":
                    break  # kembali ke while utama untuk pilih kode barang lagi
                elif pilih_menu == "0":
                    return  # keluar dari function
                else:
                    print("❌ Invalid choice.")
            break  # keluar dari while menu pilihan untuk kode barang ini


# ==========================================
# Sub Menu DELETE Penyewaan
# ==========================================

def batalkan_penyewaan(userid):
    while True:
        print("\n" + "=" * width)
        print("🗑️  DELETE RENTAL DATA".center(width))
        print("=" * width)

        print()
        transaksi_user = get_user_rentals(userid, "active")

        if not transaksi_user:
            print("⚠️   You do not have any rental data.")
            return

        # tampilkan daftar penyewaan
        display_rentals(userid)

        # Input Kode Barang
        kode_input = input("\nEnter Equipment Code to cancel (0 to go back): ").upper()

        if kode_input == "0":
            return

        # Cari transaksi berdasarkan Kode
        target_list = [t for t in transaksi_user if t["kode_barang"] == kode_input]

        if not target_list:
            print("❌ Equipment code not found in your rentals.")
            continue
        
        target_trans = None
        # Logika jika ada lebih dari 1 transaksi dengan kode yang sama
        if len(target_list) > 1:
            print(f"\n⚠️  Found {len(target_list)} transactions with code {kode_input}.")
            print("Select specific transaction to delete:")
            for i, t in enumerate(target_list, 1):
                print(f"{i}. Qty: {t['jumlah']}, Duration: {t['lama_sewa']} days")
            try:
                idx_pilih = int(input("Select number (1-{}): ".format(len(target_list)))) - 1
                if 0 <= idx_pilih < len(target_list):
                    target_trans = target_list[idx_pilih]
                else:
                    print("❌ Invalid choice.")
                    continue
            except ValueError:
                print("❌ Input must be a number.")
                continue
        else:
            target_trans = target_list[0]

        # cari alat terkait
        alat = get_equipment(target_trans["kode_barang"])

        # konfirmasi
        print("\n------- CANCELLATION CONFIRMATION -------")
        print()
        print(f"Equipment    : {alat['nama'] if alat else 'Unknown'}")
        print(f"Qty     : {target_trans['jumlah']}")
        print(f"Duration: {target_trans['lama_sewa']} days")
        print(f"Total   : Rp {target_trans['total_harga']:,}")
        
        while True:
            konfirmasi = input("Are you sure you want to cancel this rental? (Y/N): ").lower()

            if konfirmasi == "y":
                # kembalikan stok
                if alat:
                    new_stok = alat["stok"] + target_trans["jumlah"]
                    update_equipment(alat['kode'], alat['jenis'], alat['nama'], alat['harga'], new_stok)

                # update status penyewaan
                update_rental_status(target_trans['id_transaksi'], userid, target_trans['kode_barang'], "cancelled")
                
                print("\n✅ Rental cancelled successfully.")
                # ambil ulang list yang masih active
                transaksi_user = get_user_rentals(userid, "active")
                if not transaksi_user:
                     print("⚠️ You no longer have any active rentals.")
                else:
                    # tampilkan daftar penyewaan
                    display_rentals(userid)
                break

            elif konfirmasi == "n":
                print("\n❌ Cancellation cancelled.")
                break

            else:
                print("❌ Invalid input! Enter Y or N.")

        # ===== MENU LANJUTAN =====
        print("\n------- Rental Options -------")
        print()
        print("1. Cancel Another Rental")
        print("0. Back to Main Menu")
        lanjut = input("Select option (0-1): ")

        if lanjut == "0":
            return
        elif lanjut == "1":
            continue
        else:
            print("❌ Invalid choice, returning to main menu.")
            return
        
# ==========================================
# Sub Menu Pengembalian Barang
# ==========================================
def pengembalian_barang(userid):
    while True:
        print("\n" + "=" * width)
        print("🔄 RETURN RENTAL Equipment".center(width))
        print("=" * width)

        print()
        transaksi_user = get_user_rentals(userid, "active")

        if not transaksi_user:
            print("⚠️   You have no Equipments currently rented.")
            return
        
        display_rentals(userid)

        kode_input = input("\nEnter Equipment Code to return (0 to go back): ").upper()
        if kode_input == "0": return

        target_list = [t for t in transaksi_user if t["kode_barang"] == kode_input]
        
        if not target_list:
            print("❌ Equipment code not found.")
            continue

        target_trans = None
        if len(target_list) > 1:
            print(f"\n⚠️  Found {len(target_list)} transactions with code {kode_input}.")
            print("Select transaction to return:")
            for i, t in enumerate(target_list, 1):
                print(f"{i}. Qty: {t['jumlah']}, Duration: {t['lama_sewa']} days")
            try:
                idx_pilih = int(input("Select number: ")) - 1
                if 0 <= idx_pilih < len(target_list):
                    target_trans = target_list[idx_pilih]
                else:
                    print("❌ Invalid choice.")
                    continue
            except ValueError:
                print("❌ Input must be a number.")
                continue
        else:
            target_trans = target_list[0]

        alat = get_equipment(target_trans["kode_barang"])
        
        print("\n------- RETURN CONFIRMATION -------")
        print()
        print(f"Equipment    : {alat['nama'] if alat else 'Unknown'}")
        print(f"Qty     : {target_trans['jumlah']}")
        
        while True:
            konfirmasi = input("Confirm Equipment return? (Y/N): ").lower()
            if konfirmasi == "y":
                if alat: 
                    new_stok = alat["stok"] + target_trans["jumlah"] # Kembalikan stok
                    update_equipment(alat['kode'], alat['jenis'], alat['nama'], alat['harga'], new_stok)
                
                update_rental_status(target_trans['id_transaksi'], userid, target_trans['kode_barang'], "returned")
                
                print("\n✅ Equipment returned successfully. Thank you!")
                transaksi_user = get_user_rentals(userid, "active")
                if not transaksi_user:
                     print("⚠️ You no longer have any active rentals.")
                else:
                    # tampilkan daftar penyewaan
                    display_rentals(userid)
                break
            elif konfirmasi == "n":
                print("\n❌ Return cancelled.")
                break
            else: print("❌ Invalid input!")

        print("\n------- Rental Options -------")
        print()
        print("1. Return Another Equipment")
        print("0. Back to Main Menu")
        lanjut = input("Select option (0-1): ")
        if lanjut == "0":
            return
        elif lanjut == "1":
            continue
        else:
            print("❌ Invalid choice, returning to main menu.")
            return

