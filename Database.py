# ==========================================
# DATA STORAGE (Flask-SQLAlchemy Version)
# ==========================================
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy object (will be bound to app in app.py)
db = SQLAlchemy()

# 1. Definisi Model (Tabel)
class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    role = db.Column(db.String)
    nama = db.Column(db.String)
    gender = db.Column(db.String)
    usia = db.Column(db.Integer)
    pekerjaan = db.Column(db.String)
    hobi = db.Column(db.String)
    kota = db.Column(db.String)
    rt = db.Column(db.Integer)
    rw = db.Column(db.Integer)
    zipc = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    nohp = db.Column(db.String)

class Item(db.Model):
    __tablename__ = 'items'
    kode = db.Column(db.String, primary_key=True)
    jenis = db.Column(db.String)
    nama = db.Column(db.String)
    harga = db.Column(db.Float)
    stok = db.Column(db.Integer)

class Rental(db.Model):
    __tablename__ = 'rentals'
    id_transaksi = db.Column(db.String, primary_key=True)
    userid = db.Column(db.String)
    kode_barang = db.Column(db.String)
    jumlah = db.Column(db.Integer)
    lama_sewa = db.Column(db.Integer)
    total_harga = db.Column(db.Float)
    status = db.Column(db.String, default='active')

# Helper function: Mengubah object SQLAlchemy menjadi Dictionary
# Ini penting agar kompatibel dengan kode lama yang mengharapkan return dict
def model_to_dict(model):
    if model is None:
        return None
    columns = model.__table__.columns.keys()
    return {c: getattr(model, c) for c in columns}

def models_to_list(models):
    return [model_to_dict(m) for m in models]

# ==========================================
# FUNGSI CRUD (SUDAH Dikonversi ke db.session)
# ==========================================

def create_user(userid, password, email, role, nama, gender, usia, pekerjaan, hobi, kota, rt, rw, zipc, lat, lon, nohp):
    """
    Simpan user baru ke database SQLite.
    """
    try:
        new_user = User(
            userid=userid, password=password, email=email, role=role, 
            nama=nama, gender=gender, usia=usia, pekerjaan=pekerjaan, 
            hobi=hobi, kota=kota, rt=rt, rw=rw, zipc=zipc, 
            lat=lat, lon=lon, nohp=nohp
        )
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def check_userid(userid):
    result = User.query.filter_by(userid=userid).first()
    return result is not None
    
def get_user(userid):
    result = User.query.filter_by(userid=userid).first()
    return model_to_dict(result)

def update_userid(old_userid, new_userid):
    try:
        user = User.query.filter_by(userid=old_userid).first()
        if user:
            user.userid = new_userid
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def update_password(userid, password):
    try:
        User.query.filter_by(userid=userid).update({"password": password})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def delete_user(userid):
    try:
        User.query.filter_by(userid=userid).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def get_all_equipment():
    result = Item.query.order_by(Item.jenis.asc()).all()
    return models_to_list(result)

def get_equipment(kode):
    result = Item.query.filter_by(kode=kode).first()
    return model_to_dict(result)

def add_equipment(kode, jenis, nama, harga, stok):
    try:
        new_item = Item(kode=kode, jenis=jenis, nama=nama, harga=harga, stok=stok)
        db.session.add(new_item)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def update_equipment(kode, jenis, nama, harga, stok):
    try:
        Item.query.filter_by(kode=kode).update({
            "jenis": jenis, "nama": nama, "harga": harga, "stok": stok
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def delete_equipment(kode):
    try:
        Item.query.filter_by(kode=kode).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def get_all_rentals():
    result = Rental.query.all()
    return models_to_list(result)

def get_rentals_by_status(status):
    result = Rental.query.filter_by(status=status).all()
    return models_to_list(result)

def get_user_rentals(userid, status=None):
    query = Rental.query.filter_by(userid=userid)
    if status:
        query = query.filter_by(status=status)
    result = query.all()
    return models_to_list(result)

def add_rental(id_transaksi, userid, kode_barang, jumlah, lama_sewa, total_harga, status='active'):
    try:
        new_rental = Rental(
            id_transaksi=id_transaksi, userid=userid, kode_barang=kode_barang,
            jumlah=jumlah, lama_sewa=lama_sewa, total_harga=total_harga, status=status
        )
        db.session.add(new_rental)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def update_rental(id_transaksi, userid, kode_barang, jumlah, lama_sewa, total_harga, status):
    try:
        Rental.query.filter_by(id_transaksi=id_transaksi).update({
            "jumlah": jumlah, "lama_sewa": lama_sewa, 
            "total_harga": total_harga, "status": status
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def update_rental_status(id_transaksi, userid, kode_barang, status):
    try:
        Rental.query.filter_by(id_transaksi=id_transaksi).update({
            "status": status
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def delete_rental(id_transaksi, userid, kode_barang):
    try:
        Rental.query.filter_by(id_transaksi=id_transaksi).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def get_last_transaction_id():
    result = Rental.query.order_by(Rental.id_transaksi.desc()).first()
    if result:
        return result.id_transaksi
    return None
