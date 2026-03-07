from Database import get_all_equipment, get_equipment, add_equipment, update_equipment, delete_equipment
from Menu_Auth import is_alpha, is_int
#---------------------------------------
width = 60 

lebar_kode = 12
lebar_jenis = 26
lebar_nama = 40
lebar_harga = 15
lebar_stok = 12

# lihat semua barang 
def lihat_semua_barang():
    alat_outdoor = get_all_equipment()
    if not alat_outdoor:
        print("📭  Equipment list is still empty")
        return

    # Header tabel
    print("\n" + "=" * 111)
    print("🌿 ARUNIKA OUTDOOR RENTAL 🌿".center(111))
    print("RENTAL EQUIPMENT LIST • 1 DAY".center(111))
    print("=" * 111)

    print(f"┌{'─'*lebar_kode}┬{'─'*lebar_jenis}┬{'─'*lebar_nama}┬{'─'*lebar_harga}┬{'─'*lebar_stok}┐")
    print(f"│ {'Code':<{lebar_kode-1}}│ {'Equipment Type':<{lebar_jenis-1}}│ {'Equipment Name':<{lebar_nama-1}}│ {'Price (Rp)':<{lebar_harga-1}}│ {'Stock (pcs)':<{lebar_stok-1}}│")
    print(f"├{'─'*lebar_kode}┼{'─'*lebar_jenis}┼{'─'*lebar_nama}┼{'─'*lebar_harga}┼{'─'*lebar_stok}┤")

    # Isi tabel
    for barang in alat_outdoor:
        print(f"│ {barang['kode']:<{lebar_kode-1}}│ {barang['jenis']:<{lebar_jenis-1}}│ {barang['nama']:<{lebar_nama-1}}│ {barang['harga']:<{lebar_harga-1},}│ {barang['stok']:<{lebar_stok-1}}│")

    # Footer tabel
    print(f"└{'─'*lebar_kode}┴{'─'*lebar_jenis}┴{'─'*lebar_nama}┴{'─'*lebar_harga}┴{'─'*lebar_stok}┘")
    
# lihat barang berdasarkan input user (kode barang)
def lihat_barang_tertentu():
    kode = input("Enter Equipment code: ").upper()
    barang = get_equipment(kode)

    if barang:
        print("\n" + "=" * 111)
        print("🌿 ARUNIKA OUTDOOR RENTAL 🌿".center(111))
        print("RENTAL EQUIPMENT LIST • 1 DAY".center(111))
        print("=" * 111)

        print(f"┌{'─'*lebar_kode}┬{'─'*lebar_jenis}┬{'─'*lebar_nama}┬{'─'*lebar_harga}┬{'─'*lebar_stok}┐")
        print(f"│ {'Code':<{lebar_kode-1}}│ {'Equipment Type':<{lebar_jenis-1}}│ {'Equipment Name':<{lebar_nama-1}}│ {'Price (Rp)':<{lebar_harga-1}}│ {'Stock (pcs)':<{lebar_stok-1}}│")
        print(f"├{'─'*lebar_kode}┼{'─'*lebar_jenis}┼{'─'*lebar_nama}┼{'─'*lebar_harga}┼{'─'*lebar_stok}┤")

        # Isi tabel
        print(f"│ {barang['kode']:<{lebar_kode-1}}│ {barang['jenis']:<{lebar_jenis-1}}│ {barang['nama']:<{lebar_nama-1}}│ {barang['harga']:<{lebar_harga-1},}│ {barang['stok']:<{lebar_stok-1}}│")

        # Footer tabel
        print(f"└{'─'*lebar_kode}┴{'─'*lebar_jenis}┴{'─'*lebar_nama}┴{'─'*lebar_harga}┴{'─'*lebar_stok}┘")

    else:
        print("❌ Equipment with that code not found")



# Sub Menu CREATE Data Barang (Admin)
# ==========================================
def menu_add_barang():
    while True:
        print("\n" + "=" * width)
        print("📦 ADD NEW EQUIPMENT".center(width))
        print("=" * width)

        print()
        # Input Kode Barang
        while True:
            kode = input("Enter Equipment Code: ").upper()
            if len(kode) < 1:
                print("❌ Equipment code cannot be empty.")
                continue
            
            # Cek duplikat
            if get_equipment(kode):
                print("❌ Equipment code already used. Use another code.")
                continue
            break
        
        # Input Jenis Barang
        while True:
            jenis = input("Enter Equipment Type: ").title()
            if not is_alpha(jenis):
                print("❌ Equipment type can only contain letters.")
                continue
            break
            
        # Input Nama Barang
        while True:
            nama = input("Enter Equipment Name: ")
            if not nama.strip():
                print("❌ Equipment name cannot be empty.")
                continue
            break
            
        # Input Harga
        while True:
            harga_input = input("Enter Rental Price per Day: ")
            if not is_int(harga_input):
                print("❌ Price must be a number.")
                continue
            
            harga = int(harga_input)
            if harga <= 0:
                print("❌ Price must be greater than 0.")
                continue
            break
            
        # Input Stok
        while True:
            stok_input = input("Enter Stock Quantity: ")
            if not is_int(stok_input):
                print("❌ Stock must be a number.")
                continue
            
            stok = int(stok_input)
            if stok < 0:
                print("❌ Stock cannot be negative.")
                continue
            break

        # Konfirmasi
        print("\n------- NEW DATA CONFIRMATION -------")
        print(f"Code  : {kode}")
        print(f"Type  : {jenis}")
        print(f"Name  : {nama}")
        print(f"Price : Rp {harga:,}")
        print(f"Stock : {stok}")
        
        while True:
            konfirmasi = input("\nSave this Equipment data? (Y/N): ").lower()
            if konfirmasi == 'y':
                add_equipment(kode, jenis, nama, harga, stok)
                print("\n✅ Equipment added successfully.")
                break
            elif konfirmasi == 'n':
                print("\n❌ Equipment addition cancelled.")
                break
            else:
                print("❌ Invalid input! Enter Y or N.")
        
        # Menu lanjutan
        print("\n------- Admin Options -------")
        print()
        print("1. Add Another Equipment")
        print("0. Back to Admin Menu")
        lanjut = input("Select option (0-1): ")
        
        if lanjut == "1":
            continue
        else:
            return


# ==========================================
# Sub Menu UPDATE Data Barang (Admin)
# ==========================================
def menu_update_barang():
    while True:
        print("\n" + "=" * width)
        print("✏️  UPDATE EQUIPMENT".center(width))
        print("=" * width)

        print()
        kode_input = input("Enter Equipment Code to update (0 to cancel): ").upper()
        
        if kode_input == "0":
            return
            
        # Cari barang
        barang_target = get_equipment(kode_input)
        
        if not barang_target:
            print("❌ Equipment code not found.")
            continue
            
        print(f"\nData Found: {barang_target['nama']}")
        print(f"1. Equipment Name  : {barang_target['nama']}")
        print(f"2. Type       : {barang_target['jenis']}")
        print(f"3. Price      : Rp {barang_target['harga']:,}")
        print(f"4. Stock      : {barang_target['stok']}")
        
        print("\n------- SELECT DATA TO CHANGE -------")
        print("1. Change Name")
        print("2. Change Type")
        print("3. Change Price")
        print("4. Change Stock")
        print("0. Back")
        
        pilih = input("Select (0-4): ")
        
        updated = False
        
        new_nama = barang_target['nama']
        new_jenis = barang_target['jenis']
        new_harga = barang_target['harga']
        new_stok = barang_target['stok']

        if pilih == '1':
            while True:
                baru = input(f"Enter New Name [{barang_target['nama']}]: ")
                if not baru.strip():
                    print("❌ Name cannot be empty.")
                    continue
                if baru == barang_target['nama']:
                    print("❌ The name is already the same as the previous value. Please enter a different name.")
                    continue
                new_nama = baru
                updated = True
                break
                
        elif pilih == '2':
            while True:
                baru = input(f"Enter New Type [{barang_target['jenis']}]: ").title()
                if not is_alpha(baru):
                    print("❌ Type can only contain letters.")
                    continue
                if baru == barang_target['nama']:
                    print("❌ The type is already the same as the previous value. Please enter a different name.")
                    continue
                new_jenis = baru
                updated = True
                break
                
        elif pilih == '3':
            while True:
                baru_str = input(f"Enter New Price [{barang_target['harga']}]: ")
                if not is_int(baru_str):
                    print("❌ Price must be a number.")
                    continue
                harga_baru = int(baru_str)
                if harga_baru == barang_target['harga']:
                    print("❌ The price is already the same as the previous value. Please enter a different value.")
                    continue
                if harga_baru <= 0:
                    print("❌ Price must be greater than 0.")
                    continue
                new_harga = harga_baru
                updated = True
                break
                
        elif pilih == '4':
            while True:
                baru_str = input(f"Enter New Stock [{barang_target['stok']}]: ")
                if not is_int(baru_str):
                    print("❌ Stock must be a number.")
                    continue
                stok_baru = int(baru_str)
                if stok_baru == barang_target['stok']:
                    print("❌ The stock is already the same as the previous value. Please enter a different value.")
                    continue
                if stok_baru < 0:
                    print("❌ Stock cannot be negative.")
                    continue
                new_stok = stok_baru
                updated = True
                break
                
        elif pilih == '0':
            return
            
        else:
            print("❌ Invalid choice.")
            continue
            
        if updated:
            update_equipment(kode_input, new_jenis, new_nama, new_harga, new_stok)
            print("\n✅ Equipment data updated successfully.")
            
        # Menu lanjutan
        print("\n------- Admin Options -------")
        print()
        print("1. Update Another Equipment")
        print("0. Back to Admin Menu")
        lanjut = input("Select option (0-1): ")
        
        if lanjut == "1":
            continue
        else:
            return

# ==========================================
# Sub Menu READ Data Barang (Admin)
# ==========================================
def menu_read_barang():

    while True:
        print("\n" + "=" * width)
        print("📦  VIEW EQUIPMENT".center(width))
        print("=" * width)

        print()
        print("1. View All Equipments")
        print("2. View Specific Equipment (by Code)")
        print("0. Back to Admin Menu")
        print()

        print("=" * width)
        pilih = input("Select option (0-2): ")

        if pilih == "1":
            # Memanggil fungsi global yang sudah ada
            lihat_semua_barang()
            
        elif pilih == "2":
            # Memanggil fungsi global yang sudah ada
            lihat_barang_tertentu()
            
        elif pilih == "0":
            break
            
        else:
            print("❌ Invalid choice")


# ==========================================
# Sub Menu DELETE Data Barang (Admin)
# ==========================================
def menu_delete_barang():
    while True:
        print("\n" + "=" * width)
        print("🗑️  DELETE EQUIPMENT".center(width))
        print("=" * width)

        print()
        # Cek jika data barang kosong
        if not get_all_equipment():
            print("⚠️  Equipment list is currently empty.")
            print("ℹ️  Please add Equipments first in the 'Add Equipments' menu.")
            input("\nPress Enter to return...")
            return

        # Input Kode Barang
        print("Enter the Equipment Code to delete.")
        kode_input = input("Enter Equipment Code (0 to cancel): ").upper()

        if kode_input == "0":
            return

        if not kode_input.strip():
            print("❌ Equipment code cannot be empty.")
            continue

        # Mencari barang
        target_barang = get_equipment(kode_input)
        
        # Validasi apakah barang dEquipmentukan
        if not target_barang:
            print(f"❌ Equipment with code '{kode_input}' not found.")
            continue

        # Tampilkan data barang yang akan dihapus
        print("\n------- EQUIPMENT DETAILS -------")
        print(f"Code     : {target_barang['kode']}")
        print(f"Type     : {target_barang['jenis']}")
        print(f"Name     : {target_barang['nama']}")
        print(f"Price    : Rp {target_barang['harga']:,}")
        print(f"Stock    : {target_barang['stok']}")

        # Konfirmasi Penghapusan
        while True:
            konfirmasi = input("\nAre you sure you want to DELETE this Equipment? (Y/N): ").lower()

            if konfirmasi == 'y':
                delete_equipment(kode_input)
                print("\n✅ Equipment deleted successfully from the database.")
                break
                
            elif konfirmasi == 'n':
                print("\n❌ Deletion process cancelled.")
                break
                
            else:
                print("❌ Invalid input! Please enter 'Y' or 'N'.")

        # Menu Lanjutan (Looping)
        print("\n------- Admin Options -------")
        print()
        print("1. Delete Another Equipment")
        print("0. Back to Admin Menu")
        
        lanjut = input("Select option (0-1): ")
        
        if lanjut == "1":
            continue  # Kembali ke awal loop
        elif lanjut == "0":
            return   # Keluar fungsi
        else:
            print("❌ Invalid choice. Returning to Admin Menu...")
            return


        # Menu Lanjutan (Looping)
        print("\n------- Admin Options -------")
        print()
        print("1. Delete Another Equipment")
        print("0. Back to Admin Menu")
        
        lanjut = input("Select option (0-1): ")
        
        if lanjut == "1":
            continue  # Kembali ke awal loop
        elif lanjut == "0":
            return   # Keluar fungsi
        else:
            print("❌ Invalid choice. Returning to Admin Menu...")
            return
        

# Admin Sub Menu: Equipment Management
# ------------------------------------
def menu_admin_equipment(userid):
    while True:
        width = 60
        print("\n" + "=" * width)
        print("EQUIPMENT MANAGEMENT".center(width))
        print("=" * width)

        print()
        print("  [1] View All Equipment")
        print("  [2] Add Equipment")
        print("  [3] Update Equipment")
        print("  [4] Remove Equipment")
        print("  [0] Back")
        print()

        print("=" * width)
        pilih = input("Select option (0-4): ")
        if pilih == "1":
            menu_read_barang() 
        elif pilih == "2":
            menu_add_barang()
        elif pilih == "3":
            menu_update_barang()
        elif pilih == "4":
            menu_delete_barang()
        elif pilih == "0":
            print()
            break
        else:
            print()
            print("❌ Invalid input!")
