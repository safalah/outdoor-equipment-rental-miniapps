from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

# import fungsi dari file python lama (Menu_Auth, Equipment, dll)
from Menu_Auth import login as login_cli, register as register_cli
from Equipment_Management import menu_admin_equipment
from Rents_Management import menu_admin_rents
from Profile import tampilkan_data_personal
from Invoice import view_invoice
from Renter import menu_lihat_barang, buat_penyewaan, ubah_penyewaan, batalkan_penyewaan, pengembalian_barang
from Database import (
    get_all_equipment, get_equipment, add_rental, get_user_rentals, 
    update_rental, update_rental_status, get_last_transaction_id, 
    update_equipment, get_user, update_userid, update_password, delete_user, add_equipment, 
    delete_equipment, get_all_rentals, get_rentals_by_status, delete_rental, create_user, check_userid
)
from Validators import validate_registration
import datetime
from Database import db # Import db from Database.py

app = Flask(__name__)
app.secret_key = "supersecret"

# ===== Flask-SQLAlchemy Configuration =====
# 'sqlite:///tugas_project.db' will automatically point to the 'instance' folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tugas_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# ===== Helper for AJAX uniqueness check =====
@app.route("/check_userid")
def check_userid_availability():
    userid = request.args.get('userid', '')
    exists = check_userid(userid)
    return jsonify({"exists": exists})

# ===== Menu Awal =====
@app.route("/")
def menu_awal():
    return render_template("menu.html")

# ===== Register =====
@app.route("/register", methods=["GET","POST"])
def register_route():
    if request.method=="POST":
        # Validasi data
        is_valid, error_msg = validate_registration(request.form)
        
        if not is_valid:
            return render_template("register.html", error=error_msg, form_data=request.form)

        # ambil data dari form
        userid = request.form["userid"]
        password = request.form["password"]
        email = request.form["email"]
        role = request.form["role"]
        nama = request.form["nama"]
        gender = request.form["gender"]
        usia = int(request.form["usia"])
        pekerjaan = request.form["pekerjaan"]
        hobi = ",".join([h.strip() for h in request.form["hobi"].split(",") if h.strip() != ""])
        kota = request.form["kota"]
        rt = request.form["rt"]
        rw = request.form["rw"]
        zipc = request.form["zipc"]
        lat = request.form["lat"]
        lon = request.form["lon"]
        nohp = request.form["nohp"]

        # Simpan ke Database
        create_user(
            userid, password, email, role, nama, gender, usia, pekerjaan,
            hobi, kota, rt, rw, zipc, lat, lon, nohp
        )

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login_route"))

    return render_template("register.html")


# ===== Login =====
@app.route("/login", methods=["GET","POST"])
def login_route():
    # Inisialisasi counter percobaan di session jika belum ada
    if "login_attempts" not in session:
        session["login_attempts"] = 0

    if request.method=="POST":
        if session["login_attempts"] >= 5:
            return render_template("login.html", error="You have failed 5 times. Please try again later.")

        userid_input = request.form["userid"]
        password_input = request.form["password"]

        user = get_user(userid_input)

        if user:
            if user["password"] == password_input:
                # Reset counter saat login berhasil
                session["login_attempts"] = 0
                session["userid"] = user["userid"]
                session["role"] = user["role"]
                
                if user["role"].lower()=="admin":
                    return redirect(url_for("admin_menu"))
                else:
                    return redirect(url_for("rental_menu"))
            else:
                session["login_attempts"] += 1
                error = f"Wrong Password (Failed Attempts: {session['login_attempts']} times)"
                return render_template("login.html", error=error)
        else:
            session["login_attempts"] += 1
            error = f"ID not registered. (Failed Attempts: {session['login_attempts']} times)"
            return render_template("login.html", error=error)

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("menu_awal"))

# ===== Admin Menu =====
@app.route("/admin")
def admin_menu():
    if "userid" not in session:
        return redirect(url_for("login_route"))
    return render_template("admin_menu.html")

# ===== Renter / User Menu =====
@app.route("/user")
def rental_menu():
    if "userid" not in session:
        return redirect(url_for("login_route"))
    return render_template("rental_menu.html")

# ===== Admin Sub-menu =====
@app.route("/admin/equipment")
def admin_equipment():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    mode = request.args.get("mode","menu")

    return render_template(
        "equipment_management.html",
        mode=mode
    )

@app.route("/admin/equipment/view")
def admin_view_equipment():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    search_query = request.args.get('search','')

    if search_query:
        item = get_equipment(search_query)
        equipments = [item] if item else []
    else:
        equipments = get_all_equipment()

    return render_template(
        "view_equipment.html",
        equipments=equipments,
        search_query=search_query,
        role="admin"
    )


@app.route("/admin/equipment/add", methods=["POST"])
def admin_add_equipment():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    kode = request.form["kode"].upper()
    jenis = request.form["jenis"]
    nama = request.form["nama"]
    harga = int(request.form["harga"])
    stok = int(request.form["stok"])

    add_equipment(kode, jenis, nama, harga, stok)

    return redirect(url_for("admin_equipment"))


@app.route("/admin/equipment/update", methods=["POST"])
def admin_update_equipment():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    kode = request.form["kode"].upper()
    jenis = request.form["jenis"]
    nama = request.form["nama"]
    harga = int(request.form["harga"])
    stok = int(request.form["stok"])

    update_equipment(kode, jenis, nama, harga, stok)

    return redirect(url_for("admin_equipment"))

@app.route("/admin/equipment/delete", methods=["POST"])
def admin_delete_equipment():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    kode = request.form["kode"].upper()

    delete_equipment(kode)

    return redirect(url_for("admin_equipment"))

@app.route("/admin/rents")
def admin_rents():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    mode = request.args.get("mode","menu")
    status = request.args.get("status","all")

    rentals = []

    if mode in ["view_table","delete"]:

        # FILTER STATUS
        if status == "all":
            data = get_all_rentals()
        else:
            data = get_rentals_by_status(status)

        for r in data:

            user = get_user(r["userid"])
            renter = user["nama"] if user else "Unknown"

            barang = get_equipment(r["kode_barang"])
            nama_barang = barang["nama"] if barang else "Unknown"

            r["renter"] = renter
            r["nama_barang"] = nama_barang

            rentals.append(r)

    return render_template(
        "rents_management.html",
        mode=mode,
        rentals=rentals,
        status=status
    )

@app.route("/admin/rents/delete", methods=["POST"])
def admin_delete_rent_by_status():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    id_transaksi = request.form["id_transaksi"]
    userid = request.form["userid"]
    kode_barang = request.form["kode_barang"]

    delete_rental(id_transaksi, userid, kode_barang)

    return redirect(url_for("admin_rents", mode="delete"))


# ===== Renter Sub-menu =====
@app.route("/user/equipment")
def user_equipment():
    if "userid" not in session: return redirect(url_for("login_route"))
    search_query = request.args.get('search', '')
    if search_query:
        item = get_equipment(search_query)
        equipments = [item] if item else []
    else:
        equipments = get_all_equipment()
    return render_template("view_equipment.html", equipments=equipments, search_query=search_query, role="user")

@app.route("/user/rental/create", methods=["GET", "POST"])
def user_create_rental():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    active_rentals = get_user_rentals(userid, "active")
    info_user = "ℹ️ You have previous transactions." if active_rentals else "ℹ️ You do not have any transactions yet."
    
    if request.method == "POST":
        kode_barang = request.form.get("kode_barang")
        jumlah = int(request.form.get("jumlah"))
        lama_sewa = int(request.form.get("lama_sewa"))
        confirm = request.form.get("confirm")

        barang = get_equipment(kode_barang)
        if not barang:
            return render_template("create_rental.html", error="❌ Equipment not found.", info_user=info_user, active_rentals=active_rentals)
        
        if barang["stok"] < jumlah and not confirm:
            return render_template("create_rental.html", error="⚠️ Sorry, Equipment is out of stock or insufficient.", info_user=info_user, active_rentals=active_rentals)

        total_harga = barang["harga"] * jumlah * lama_sewa

        if confirm == "yes":
            # Logika ID Transaksi
            last_id = get_last_transaction_id()
            counter = 0
            if last_id and last_id.startswith("arunika"):
                try: counter = int(last_id.replace("arunika", ""))
                except: counter = 0
            
            transaksi_aktif = [t for t in active_rentals if t['status'] == 'active']
            if transaksi_aktif:
                id_transaksi = transaksi_aktif[0]["id_transaksi"]
            else:
                id_transaksi = f"arunika{counter + 1:02d}"

            add_rental(id_transaksi, userid, kode_barang, jumlah, lama_sewa, total_harga, "active")
            update_equipment(barang['kode'], barang['jenis'], barang['nama'], barang['harga'], barang['stok'] - jumlah)
            return redirect(url_for("user_create_rental"))

        confirm_data = {
            "nama": barang["nama"],
            "kode_barang": kode_barang,
            "jumlah": jumlah,
            "lama_sewa": lama_sewa,
            "total_harga": total_harga
        }
        return render_template("create_rental.html", confirm_data=confirm_data, info_user=info_user, active_rentals=active_rentals)

    return render_template("create_rental.html", info_user=info_user, active_rentals=active_rentals)

@app.route("/user/rental/update", methods=["GET", "POST"])
def user_update_rental():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    active_rentals = get_user_rentals(userid, "active")

    if request.method == "POST":
        action = request.form.get("action")
        id_transaksi = request.form.get("id_transaksi")
        kode_barang = request.form.get("kode_barang")
        
        if action == "edit":
            target_trans = next((t for t in active_rentals if t["id_transaksi"] == id_transaksi and t["kode_barang"] == kode_barang), None)
            return render_template("update_rental.html", active_rentals=active_rentals, target_trans=target_trans)
        
        elif action == "save":
            new_jumlah = int(request.form.get("new_jumlah"))
            new_lama = int(request.form.get("new_lama"))
            
            target_trans = next((t for t in active_rentals if t["id_transaksi"] == id_transaksi and t["kode_barang"] == kode_barang), None)
            if target_trans:
                alat = get_equipment(kode_barang)
                stok_sementara = alat['stok'] + target_trans['jumlah']
                if new_jumlah > stok_sementara:
                    return render_template("update_rental.html", active_rentals=active_rentals, error="❌ Insufficient stock.")
                
                total_baru = alat['harga'] * new_jumlah * new_lama
                update_rental(id_transaksi, userid, kode_barang, new_jumlah, new_lama, total_baru, "active")
                update_equipment(alat['kode'], alat['jenis'], alat['nama'], alat['harga'], stok_sementara - new_jumlah)
                return redirect(url_for("user_update_rental"))

    return render_template("update_rental.html", active_rentals=active_rentals)

@app.route("/user/rental/cancel", methods=["GET", "POST"])
def user_cancel_rental():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    active_rentals = get_user_rentals(userid, "active")

    if request.method == "POST":
        id_transaksi = request.form.get("id_transaksi")
        kode_barang = request.form.get("kode_barang")
        target_trans = next((t for t in active_rentals if t["id_transaksi"] == id_transaksi and t["kode_barang"] == kode_barang), None)
        
        if target_trans:
            alat = get_equipment(kode_barang)
            if alat:
                update_equipment(alat['kode'], alat['jenis'], alat['nama'], alat['harga'], alat['stok'] + target_trans['jumlah'])
            update_rental_status(id_transaksi, userid, kode_barang, "cancelled")
            return redirect(url_for("user_cancel_rental"))

    return render_template("cancel_rental.html", active_rentals=active_rentals)

@app.route("/user/rental/return", methods=["GET", "POST"])
def user_return_rental():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    active_rentals = get_user_rentals(userid, "active")

    if request.method == "POST":
        id_transaksi = request.form.get("id_transaksi")
        kode_barang = request.form.get("kode_barang")
        target_trans = next((t for t in active_rentals if t["id_transaksi"] == id_transaksi and t["kode_barang"] == kode_barang), None)
        
        if target_trans:
            alat = get_equipment(kode_barang)
            if alat:
                update_equipment(alat['kode'], alat['jenis'], alat['nama'], alat['harga'], alat['stok'] + target_trans['jumlah'])
            update_rental_status(id_transaksi, userid, kode_barang, "returned")
            return redirect(url_for("user_return_rental"))

    return render_template("rental_return.html", active_rentals=active_rentals)

@app.route("/user/invoice")
def user_invoice():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    user_data = get_user(userid)
    rentals = get_user_rentals(userid, "active")
    
    formatted_rentals = []
    total_semua = 0
    id_transaksi = "N/A"
    if rentals:
        id_transaksi = rentals[0]["id_transaksi"]
        for r in rentals:
            barang = get_equipment(r["kode_barang"])
            r["nama_barang"] = barang["nama"] if barang else "Unknown"
            total_semua += r["total_harga"]
            formatted_rentals.append(r)

    return render_template("view_invoice.html", 
                           user=user_data, 
                           rentals=formatted_rentals, 
                           total_semua=total_semua, 
                           id_transaksi=id_transaksi,
                           date=datetime.date.today().strftime("%Y-%m-%d"))

@app.route("/user/profile")
def user_profile():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    user_data = get_user(userid)
    return render_template("view_profile.html", user=user_data)

@app.route("/user/profile/update")
def user_update_menu():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    userid = session.get("userid")
    user_data = get_user(userid)

    return render_template("update_profile.html", user=user_data)

@app.route("/user/profile/delete", methods=["POST"])
def user_delete_profile():
    if "userid" not in session: return redirect(url_for("login_route"))
    userid = session.get("userid")
    delete_user(userid)
    session.clear()
    return redirect(url_for("menu_awal"))

@app.route("/user/profile/update_userid", methods=["POST"])
def update_profile_userid():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    old_userid = session["userid"]
    new_userid = request.form["new_userid"]

    update_userid(old_userid, new_userid)

    session["userid"] = new_userid

    return redirect(url_for("user_profile"))

@app.route("/user/profile/update_password", methods=["POST"])
def update_profile_password():

    if "userid" not in session:
        return redirect(url_for("login_route"))

    userid = session["userid"]
    new_password = request.form["new_password"]

    update_password(userid, new_password)

    return redirect(url_for("user_profile"))


if __name__=="__main__":
    app.run(debug=True)
    