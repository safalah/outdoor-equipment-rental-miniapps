from Database import check_userid, get_user,create_user

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
            print("❌ User Id must be at least 6 characters")
            continue

        if len(userid) > 20:
            print("❌ User Id must be at most 20 characters")
            continue

        if not is_alnum(userid):
            print("❌ User Id can only contain letters and numbers")
            continue

        has_letter = False
        has_digit = False

        for c in userid:
            if c.isalpha():
                has_letter = True
            elif c.isdigit():
                has_digit = True

        if not (has_letter and has_digit):
            print("❌ User Id must contain letters and numbers")
            continue

        if check_userid(userid):
            print("❌ User Id already taken")
            continue
        else:
            return userid


# ==========================================
# PASSWORD VALIDATION
# ==========================================
def input_password():
    while True:
        password = input("Password ==> ")

        if len(password) < 8:
            print("❌ Password must be at least 8 characters")
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
                print("❌ Password contains invalid characters")
                break
        else:
            if upper and lower and digit and special:
                return password
            else:
                print("❌ Password must contain uppercase, lowercase, numbers, and special characters")

# ==========================================
# EMAIL VALIDATION 
# ==========================================
def input_email():
    while True:
        email = input("Email ==> ")

        if email.count("@") != 1:
            print("Invalid Email, @ count must be 1")
            continue

        username, domain = email.split("@")

        if username == "":
            print("Invalid Email, Invalid Username Format")
            continue

        if not username[0].isalnum():
            print("Invalid Email, Username must start with a letter or number")
            continue

        for c in username:
            if not (c.isalnum() or c == "_" or c == "."):
                print("Invalid Email, Invalid Username Format")
                break
        else:
            if "." not in domain:
                print("Invalid Email, Invalid Email Format (no extension)")
                continue

            domain_parts = domain.split(".")

            if len(domain_parts) > 3:
                print("Invalid Email, Maximum 2 extensions")
                continue

            hosting = domain_parts[0]
            if not hosting.isalnum():
                print("Invalid Email, Invalid Hosting Format")
                continue

            ext_valid = True
            for ext in domain_parts[1:]:
                if not ext.isalpha() or len(ext) > 5:
                    ext_valid = False
                    break

            if not ext_valid:
                print("Invalid Email, Invalid Extension Format")
                continue

            print("The Email Address you entered is Valid")
            return email

# ==========================================
# REGISTER FUNCTION
# ==========================================
def register():
    width = 60
    print("\n" + "=" * width)
    print("REGISTER".center(width))
    print("=" * width)
    print("Enter Data :")

    userid = input_userid()
    password = input_password()
    email = input_email()
    
    # ROLE 
    while True:
        role = input("Admin/Renter) ==> ").lower()
        if role in ["admin", "renter"]:
            break
        print("❌ Invalid Role")

    # NAMA
    while True:
        nama = input("Name ==> ")
        if is_alpha(nama):
            break
        print("❌ Name must be alphabetic only")

    # GENDER
    while True:
        gender = input("Male/Female) ==> ").lower()
        if gender in ["male", "female"]:
            break
        print("❌ Invalid Gender")

    # USIA
    while True:
        usia = input("Age ==> ")

        if not is_int(usia):
            print("❌ Age must be a number!")
            continue

        usia = int(usia)

        if usia < 17 or usia > 80:
            print("❌ Age must be between 17–80!")
            continue

        break

    # PEKERJAAN
    while True:
        pekerjaan = input("Job ==> ")
        if is_alpha(pekerjaan):
            break
        print("❌ Job must be alphabetic only")

    # HOBI
    while True:
        hobi = input("Hobbies (separate with commas) ==> ")

        # Pecah jadi list & bersihkan spasi kiri kanan
        hobi_list = [h.strip() for h in hobi.split(",")]

        # Hapus Equipment kosong (kalau user ngetik koma dobel)
        hobi_list = [h for h in hobi_list if h != ""]

        # Minimal 3 hobi
        if len(hobi_list) < 3:
            print("❌ Minimum 3 hobbies required!")
            continue

        # Validasi hanya huruf dan spasi
        if not all(h.replace(" ", "").isalpha() for h in hobi_list):
            print("❌ Hobbies can only contain letters and must be separated by commas!")
            continue

        break


    # ALAMAT
    print("\nAddress :")
    while True:
        kota = input("City Name ==> ")
        if is_alpha(kota):
            break
        print("❌ City name must be letters only!")

    while True:
        rt = input("RT ==> ")
        if is_int(rt):
            break
        print("❌ RT must be a number!")

    while True:
        rw = input("RW ==> ")
        if is_int(rw):
            break
        print("❌ RW must be a number!")

    while True:
        zipc = input("Zip Code ==> ")
        if not is_int(zipc):
            print("❌ Zip Code must be a number!")
        elif len(zipc) != 5:
            print("❌ Zip Code must be 5 digits!")
        else:
            break

    # GEO
    while True:
        lat = input("Latitude ==> ")

        # Kalau ada huruf
        if any(c.isalpha() for c in lat):
            print("❌ Latitude cannot contain letters!")
            continue

        if not is_float(lat):
            print("❌ Latitude must be a decimal number!")
            continue

        if "." not in lat:
            print("❌ Latitude must contain a decimal point!")
            continue

        break

    while True:
        lon = input("Longitude ==> ")

        if any(c.isalpha() for c in lon):
            print("❌ Longitude cannot contain letters!")
            continue

        if not is_float(lon):
            print("❌ Longitude must be a decimal number!")
            continue

        if "." not in lon:
            print("❌ Longitude must contain a decimal point!")
            continue

        break

    # NO HP
    while True:
        nohp = input("Phone Number ==> ")

        if not is_int(nohp):
            print("❌ Phone Number can only contain numbers!")
        elif not (11 <= len(nohp) <= 13):
            print("❌ Phone Number must be 11–13 digits!")
        else:
            break

    # SIMPAN DATA
    while True:
        save = input("\nSave Data (Y/N): ").lower()

        if save == "y":
            create_user(
                userid,
                password,
                email,
                role,
                nama,
                gender,
                usia,
                pekerjaan,
                ",".join(hobi_list),
                kota,
                rt,
                rw,
                zipc,
                lat,
                lon,
                nohp
            )

            print("\n✅ Data saved")
            break

        elif save == "n":
            print("\n❌ Data not saved")
            break

        else:
            print("\n❌ Invalid input! Enter Y or N.")


# ==========================================
# LOGIN FUNCTION
# ==========================================
def login():
    percobaan = 0

    while percobaan < 5:
        width = 60
        print("\n" + "=" * width)
        print("LOGIN".center(width))
        print("=" * width)

        userid_input = input("Enter ID : ")
        password_input = input("Enter Password : ")

        user = get_user(userid_input)

        if user:
            if user["password"] == password_input:
                print("\n🌿 Login successful. Welcome to Arunika!")
                return user
            else:
                percobaan += 1
                print(f"Wrong Password (Failed Attempts: {percobaan} times)")
        else:
            percobaan += 1
            print(f"ID not registered. (Failed Attempts: {percobaan} times)")

    print("You have failed 5 times")
    print("Please select another menu")
    return False



