from Database import check_userid

# 1. BASIC VALIDATION HELPERS
def is_alpha(text):
    if not text: return False
    for c in text:
        if not (c.isalpha() or c == " "):
            return False
    return True

def is_alnum(text):
    if not text: return False
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

# 2. USER ID VALIDATION
def validate_userid(userid):
    if len(userid) < 6:
        return False, "User Id must be at least 6 characters"
    if len(userid) > 20:
        return False, "User Id must be at most 20 characters"
    if not is_alnum(userid):
        return False, "User Id can only contain letters and numbers (no spaces or symbols)"
    
    has_letter = any(c.isalpha() for c in userid)
    has_digit = any(c.isdigit() for c in userid)
    
    if not (has_letter and has_digit):
        return False, "User Id must contain at least 1 letter and 1 number"
    
    if check_userid(userid):
        return False, "User Id already taken"
    
    return True, ""

# 3. PASSWORD VALIDATION
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    allowed_special = "/.,@#$%"
    special = any(c in allowed_special for c in password)
    
    # Check if any character is NOT allowed
    for c in password:
        if not (c.isalnum() or c in allowed_special):
            return False, f"Invalid character '{c}' in password. Only /.,@#$% are allowed as special characters."
    
    if upper and lower and digit and special:
        return True, ""
    else:
        return False, "Password must contain uppercase, lowercase, numbers, and special characters (/.,@#$%)"

# 4. EMAIL VALIDATION
def validate_email(email):
    if email.count("@") != 1:
        return False, "Invalid Email, must contain exactly one '@'"
    
    username, domain = email.split("@")
    
    # Username rules
    if not username:
        return False, "Invalid Email, Username cannot be empty"
    if not username[0].isalnum():
        return False, "Invalid Email, Username must start with a letter or number"
    for c in username:
        if not (c.isalnum() or c == "_" or c == "."):
            return False, "Invalid Email, Username can only contain letters, numbers, '_' and '.'"
            
    # Domain rules
    if "." not in domain:
        return False, "Invalid Email, Domain must have an extension"
    
    domain_parts = domain.split(".")
    hosting = domain_parts[0]
    extensions = domain_parts[1:]
    
    if len(extensions) > 2:
        return False, "Invalid Email, Maximum 2 extensions allowed"
        
    if not is_alnum(hosting):
        return False, "Invalid Email, Hosting name must be alphanumeric"
        
    for ext in extensions:
        if not ext.isalpha():
            return False, "Invalid Email, Extension must contain letters only"
        if len(ext) > 5:
            return False, "Invalid Email, Extension cannot exceed 5 characters"
            
    return True, ""

# 5-13. REGISTRATION COMPOSITE VALIDATION
def validate_registration(data):
    # UserID
    valid, msg = validate_userid(data.get("userid", ""))
    if not valid: return False, msg
    
    # Password
    valid, msg = validate_password(data.get("password", ""))
    if not valid: return False, msg
    
    # Email
    valid, msg = validate_email(data.get("email", ""))
    if not valid: return False, msg
    
    # Role
    if data.get("role", "").lower() not in ["admin", "renter"]:
        return False, "Invalid Role (must be admin or renter)"
        
    # Name
    if not is_alpha(data.get("nama", "")):
        return False, "Name must be letters and spaces only"
        
    # Gender
    if data.get("gender", "").lower() not in ["male", "female"]:
        return False, "Invalid Gender (must be male or female)"
        
    # Age
    usia_str = data.get("usia", "")
    if not is_int(usia_str):
        return False, "Age must be a number"
    usia = int(usia_str)
    if usia < 17 or usia > 80:
        return False, "Age must be between 17 and 80 years old"
        
    # Job
    if not is_alpha(data.get("pekerjaan", "")):
        return False, "Job must be letters and spaces only"
        
    # Hobbies
    hobi = data.get("hobi", "")
    hobi_list = [h.strip() for h in hobi.split(",") if h.strip() != ""]
    # Check for empty elements manually (e.g., "reading,,gaming")
    raw_hobi_list = [h.strip() for h in hobi.split(",")]
    if "" in raw_hobi_list:
        return False, "Hobbies cannot contain empty elements"
    
    if len(hobi_list) < 3:
        return False, "Minimum 3 hobbies required"
    
    for h in hobi_list:
        if not is_alpha(h):
            return False, f"Hobby '{h}' must contain letters and spaces only"
        
    # City
    if not is_alpha(data.get("kota", "")):
        return False, "City name must be letters and spaces only"
        
    # RT
    if not is_int(data.get("rt", "")):
        return False, "RT must be a number"
        
    # RW
    if not is_int(data.get("rw", "")):
        return False, "RW must be a number"
        
    # Zip Code
    zipc = data.get("zipc", "")
    if not is_int(zipc):
        return False, "Zip Code must be a number"
    if len(zipc) != 5:
        return False, "Zip Code must be exactly 5 digits"
        
    # Latitude
    lat = data.get("lat", "")
    if any(c.isalpha() for c in lat):
        return False, "Latitude cannot contain letters"
    if not is_float(lat):
        return False, "Latitude must be a decimal number"
    if "." not in lat:
        return False, "Latitude must contain a decimal point (.)"
        
    # Longitude
    lon = data.get("lon", "")
    if any(c.isalpha() for c in lon):
        return False, "Longitude cannot contain letters"
    if not is_float(lon):
        return False, "Longitude must be a decimal number"
    if "." not in lon:
        return False, "Longitude must contain a decimal point (.)"
        
    # Phone Number
    nohp = data.get("nohp", "")
    if not is_int(nohp):
        return False, "Phone Number can only contain numbers"
    if not (11 <= len(nohp) <= 13):
        return False, "Phone Number must be 11 to 13 digits"
        
    return True, ""
