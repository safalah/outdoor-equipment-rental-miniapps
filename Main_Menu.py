# import function from Menu_Auth.py
from Menu_Auth import login, register
from Equipment_Management import menu_admin_equipment
from Rents_Management import menu_admin_rents
from Profile import tampilkan_data_personal
from Invoice import view_invoice
from Renter import menu_lihat_barang, buat_penyewaan, ubah_penyewaan, batalkan_penyewaan, pengembalian_barang

# ==========================================
# Menu Renter
# ==========================================
def menu_penyewa(userid):
    while True:
        width = 60
        print("\n" + "=" * width)
        print("🌿 ARUNIKA OUTDOOR RENTAL APP 🏕️".center(width))
        print("Explore the peaks, gear up with us!".center(width))
        print("-" * width)
        print("RENTER MENU".center(width))
        print("=" * width)

        print()
        print("  [1] View Equipment List")
        print("  [2] Create Rental")
        print("  [3] Update Rental")
        print("  [4] Cancel Rental")
        print("  [5] Return Equipment")
        print("  [6] View Invoice")
        print("  [7] View Personal Data")
        print("  [0] Back")
        print()

        print("=" * width)
        pilih = input("Select menu (0-7): ")
        
        if pilih == "1":
            menu_lihat_barang()
        elif pilih == "2":
            buat_penyewaan(userid)
        elif pilih == "3":
            ubah_penyewaan(userid) 
        elif pilih == "4":
            batalkan_penyewaan(userid)
        elif pilih == "5":
            pengembalian_barang(userid)
        elif pilih == "6" :
            view_invoice(userid)
        elif pilih == "7":
            hasil = tampilkan_data_personal(userid)
            if hasil is None:
                break
            else:
                userid = hasil
        elif pilih == "0":
            print()
            print("You’ve been signed out. Thank you! 🌿")
            break
        else:
            print()
            print("❌ Invalid input!")

# ==========================================
#               Menu Admin
# ==========================================
# Main Menu Admin 
# --------------------------
def main_menu_admin(userid):
    while True:
        width = 60
        print("\n" + "=" * width)
        print("🌿 ARUNIKA OUTDOOR RENTAL APP 🏕️".center(width))
        print("Explore the peaks, gear up with us!".center(width))
        print("-" * width)
        print("ADMINISTRATOR DASHBOARD".center(width))
        print("=" * width)

        print()
        print("  [1] Equipment Management")
        print("  [2] Rents Management")
        print("  [0] Logout")
        print()

        print("=" * width)
        pilih = input("Select menu (0-2): ")
        if pilih == "1":
            menu_admin_equipment(userid)
        elif pilih == "2":
            menu_admin_rents()
        elif pilih == "0":
            print()
            print("You’ve been signed out. Thank you! 🌿")
            break
        else:
            print()
            print("❌ Invalid input!")


# ==========================================
# Menu
# ==========================================
def menu():
    while True:
        width = 60
        print("\n" + "=" * width)
        print("🌿 ARUNIKA OUTDOOR RENTAL APP 🏕️".center(width))
        print("Explore the peaks, gear up with us!".center(width))
        print("=" * width)

        print()
        print("  [1] Register")
        print("  [2] Login")
        print("  [0] Exit")
        print()

        print("=" * width)
        pilih = input("Select option (0-2): ")
        if pilih == "1":
            register()
        elif pilih == "2":
            user_login = login()
            if user_login:
                if user_login["role"].lower() == "admin":
                    main_menu_admin(user_login["userid"])
                else:
                    menu_penyewa(user_login["userid"])
        elif pilih == "0":
            print()
            print("Thanks for using this apps!")
            break
        else:
            print()
            print("❌ Invalid input")


# ==========================================
# RUN PROGRAM
# ==========================================
menu()


