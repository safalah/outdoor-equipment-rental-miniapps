# ==========================================
# Sub Menu READ Data Personal
# ==========================================

from Database import get_user, update_userid, update_password, delete_user
from Menu_Auth import input_password, is_alnum

width = 60


# ==========================================
# UPDATE Data Personal
# ==========================================
def ubah_data_personal(userid):

    user = get_user(userid)

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

        # =============================
        # UPDATE USERID
        # =============================
        if pilih == "1":

            print("\n------- Update User ID -------\n")

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

                # cek duplicate di database
                existing_user = get_user(new_userid)

                if existing_user and new_userid != userid:
                    print("❌ User ID already used by another user.")
                    continue

                while True:

                    confirm = input(
                        f"Change UserID from '{userid}' to '{new_userid}'? (Y/N): "
                    ).lower()

                    if confirm == "y":

                        update_userid(userid, new_userid)

                        print()
                        print("✅ User ID changed successfully.")

                        return new_userid

                    elif confirm == "n":

                        print("❌ Change cancelled.")
                        return userid

                    else:
                        print("❌ Invalid input! Enter Y or N.")

        # =============================
        # UPDATE PASSWORD
        # =============================
        elif pilih == "2":

            print("\n------- Update Password -------\n")

            password_baru = input_password()

            while True:

                confirm = input("Change Password? (Y/N): ").lower()

                if confirm == "y":

                    update_password(userid, password_baru)

                    print()
                    print("✅ Password changed successfully.")
                    break

                elif confirm == "n":

                    print("❌ Change cancelled.")
                    break

                else:
                    print("❌ Invalid input! Enter Y or N.")

        elif pilih == "0":
            break

        else:
            print("\n❌ Invalid choice.")

    return userid


# ==========================================
# DELETE ACCOUNT
# ==========================================
def hapus_akun(userid):

    print("\n WARNING: Account will be deleted permanently!")

    while True:

        konfirmasi = input(
            "Are you sure you want to delete this account? (Y/N): "
        ).lower()

        if konfirmasi == "y":

            delete_user(userid)

            print()
            print("✅ Account deleted successfully.")
            print("\nYou have logged out. Thank you! 🌿")

            return True

        elif konfirmasi == "n":

            print()
            print("❌ Deletion cancelled.")
            return False

        else:
            print("❌ Invalid input! Enter Y or N.")


# ==========================================
# TAMPILKAN DATA PERSONAL
# ==========================================
def tampilkan_data_personal(userid):

    while True:

        print("\n" + "=" * width)
        print("MY PERSONAL DATA".center(width))
        print("=" * width)

        print()

        user_data = get_user(userid)

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
        print(f"  City    : {user_data['kota']}")
        print(f"  RT/RW   : {user_data['rt']}/{user_data['rw']}")
        print(f"  Zip Code: {user_data['zipc']}")
        print("Coordinates :")
        print(f"  Lat     : {user_data['lat']}")
        print(f"  Lon     : {user_data['lon']}")

        print()
        print("=" * width)
        print("1. Update Data (ID & Password)")
        print("2. Delete Account")
        print("0. Back to Main Menu")
        print()
        print("=" * width)

        pilih = input("Select option (0-2): ")

        if pilih == "1":

            newuserid = ubah_data_personal(userid)

            if newuserid != userid:
                userid = newuserid

        elif pilih == "2":

            if hapus_akun(userid):
                return None

        elif pilih == "0":
            return userid

        else:
            print("❌ Invalid choice")