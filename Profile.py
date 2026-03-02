# ==========================================
# Sub Menu READ Data Personal
# ==========================================
from Database import users
from Menu_Auth import input_password, is_alnum

width = 60 

# UPDATE Data Personal 
def ubah_data_personal(userid):
    user = next((u for u in users if u["userid"] == userid), None)
    if not user:
        print("❌ User data not found.")
        return userid 

    while True:
        print("\n" + "=" * width)
        print("UPDATE PERSONAL DATA".center(width))
        print("=" * width)

        print()
        print("Data that can be changed:")
        print(f"1. UserID  : {user['userid']}")
        print(f"2. Password: {user['password']}")
        print("0. Back")
        print()

        print("=" * width)
        pilih = input("Select data to change: ")

        if pilih == "1":
            print("\n------- Update User ID -------")
            print()
            while True:
                new_userid = input("Enter New User ID: ")

                if len(new_userid) < 6 or len(new_userid) > 20:
                    print("❌ User Id must be at least 6 characters and at most 20 characters")
                    continue

                if not is_alnum(new_userid):
                    print("❌ User Id can only contain letters and numbers")
                    continue

                has_letter = False
                has_digit = False
                for c in new_userid:
                    if c.isalpha():
                        has_letter = True
                    elif c.isdigit():
                        has_digit = True
                
                if not (has_letter and has_digit):
                    print("❌ User Id must contain letters and numbers")
                    continue

                is_duplicate = False
                for u in users:
                    if u["userid"] == new_userid and u["userid"] != userid:
                        print("❌ User ID already used by another user.")
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    while True:
                        confirm = input(f"Change UserID from '{userid}' to '{new_userid}'? (Y/N): ").lower()

                        if confirm == 'y':
                            user['userid'] = new_userid
                            print()
                            print("✅ User ID changed successfully.")
                            return new_userid 

                        elif confirm == 'n':
                            print("❌ Change cancelled.")
                            return userid

                        else:
                            print("❌ Invalid input! Enter Y or N.")
                else:
                    continue

        elif pilih == "2":
            print("\n------- Update Password -------")
            print()
            password_baru = input_password()
            while True:
                confirm = input("Change Password? (Y/N): ").lower()

                if confirm == 'y':
                    user['password'] = password_baru
                    print()
                    print("✅ Password changed successfully.")
                    break

                elif confirm == 'n':
                    print("❌ Change cancelled.")
                    break

                else:
                    print("❌ Invalid input! Enter Y or N.")

        elif pilih == "0":
            break
        
        else:
            print()
            print("❌ Invalid choice.")
            
    return userid


# Sub Menu DELETE Akun 

def hapus_akun(userid):
    print("\n WARNING: Account will be deleted permanently!")
    
    while True:
        konfirmasi = input("Are you sure you want to delete this account? (Y/N): ").lower()

        if konfirmasi == 'y':
            for i in range(len(users)):
                if users[i]['userid'] == userid:
                    del users[i]  # Hapus user dari list
                    print()
                    print("✅ Account deleted successfully.")
                    print("\nYou have logged out. Thank you! 🌿")
                    return True

        elif konfirmasi == 'n':
            print()
            print("❌ Deletion cancelled.")
            return False

        else:
            print("❌ Invalid input! Enter Y or N.")

def tampilkan_data_personal(userid):
    while True:
        print("\n" + "=" * width)
        print("MY PERSONAL DATA".center(width))
        print("=" * width)

        print()
        user_data = next((u for u in users if u["userid"] == userid), None)
        
        if not user_data:
            print("\nUser data not found.")
            return None 
        print(f"UserID   : {user_data['userid']}")
        print(f"Name     : {user_data['nama']}")
        print(f"Email    : {user_data['email']}")
        print(f"Gender   : {user_data['gender']}")
        print(f"Age      : {user_data['usia']}")
        print(f"Job      : {user_data['pekerjaan']}")
        print(f"Hobbies  : {user_data['hobi']}")
        print(f"Phone No : {user_data['nohp']}")
        print("Address  :")
        print(f"  City    : {user_data['alamat']['kota']}")
        print(f"  RT/RW   : {user_data['alamat']['rt']}/{user_data['alamat']['rw']}")
        print(f"  Zip Code: {user_data['alamat']['zipc']}")
        print("Coordinates :")
        print(f"  Lat     : {user_data['geo']['lat']}")
        print(f"  Lon     : {user_data['geo']['lon']}")
        print()
        print("=" * width)
        print("1. Update Data (ID & Password)")
        print("2. Delete Account")
        print("0. Back to Main Menu")
        print()
        print("=" * width)
        
        pilih = input("Select option (0-2): ")

        if pilih == "1":
            # ID Baru 
            newuserid = ubah_data_personal(userid)
            # Cek apakah ID berubah
            if newuserid != userid:
                userid = newuserid
                
        elif pilih == "2":
            if hapus_akun(userid):
                return None 
            
        elif pilih == "0":
            return userid
            
        else:
            print("❌ Invalid choice")

