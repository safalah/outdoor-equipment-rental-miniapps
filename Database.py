# ==========================================
# DATA STORAGE (SQLAlchemy Version)
# ==========================================
from sqlalchemy import create_engine, Column, String, Integer, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Setup Koneksi ke SQLite
# File database akan dibuat otomatis bernama 'tugas_project.db' di folder yang sama
engine = create_engine('sqlite:///tugas_project.db', echo=False)
Base = declarative_base()

# 2. Definisi Model (Tabel)
class User(Base):
    __tablename__ = 'users'
    userid = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)
    role = Column(String)
    nama = Column(String)
    gender = Column(String)
    usia = Column(Integer)
    pekerjaan = Column(String)
    hobi = Column(String)
    kota = Column(String)
    rt = Column(Integer)
    rw = Column(Integer)
    zipc = Column(Integer)
    lat = Column(Float)
    lon = Column(Float)
    nohp = Column(String)

class Item(Base):
    __tablename__ = 'items'
    kode = Column(String, primary_key=True)
    jenis = Column(String)
    nama = Column(String)
    harga = Column(Float)
    stok = Column(Integer)

class Rental(Base):
    __tablename__ = 'rentals'
    # Kita jadikan id_transaksi sebagai Primary Key agar mudah dihandle ORM
    id_transaksi = Column(String, primary_key=True)
    userid = Column(String)
    kode_barang = Column(String)
    jumlah = Column(Integer)
    lama_sewa = Column(Integer)
    total_harga = Column(Float)
    status = Column(String, default='active')

# Membuat tabel di database (jika belum ada)
Base.metadata.create_all(engine)

# Membuat Session Factory
Session = sessionmaker(bind=engine)

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
# FUNGSI CRUD (SUDAH Dikonversi)
# ==========================================

def create_user(userid, password, email, role, nama, gender, usia, pekerjaan, hobi, kota, rt, rw, zipc, lat, lon, nohp):
    """
    Simpan user baru ke database SQLite.
    """
    session = Session()
    try:
        hobi_str = hobi  # hobi sudah dikirim sebagai string
        
        new_user = User(
            userid=userid, password=password, email=email, role=role, 
            nama=nama, gender=gender, usia=usia, pekerjaan=pekerjaan, 
            hobi=hobi_str, kota=kota, rt=rt, rw=rw, zipc=zipc, 
            lat=lat, lon=lon, nohp=nohp
        )
        session.add(new_user)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def check_userid(userid):
    session = Session()
    try:
        # .first() mengembalikan object atau None
        result = session.query(User).filter_by(userid=userid).first()
        return result is not None
    finally:
        session.close()
    
def get_user(userid):
    session = Session()
    try:
        result = session.query(User).filter_by(userid=userid).first()
        return model_to_dict(result)
    finally:
        session.close()

def update_userid(old_userid, new_userid):
    session = Session()
    try:
        # Mengupdate userid yang merupakan Primary Key
        user = session.query(User).filter_by(userid=old_userid).first()
        if user:
            user.userid = new_userid
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def update_password(userid, password):
    session = Session()
    try:
        session.query(User).filter_by(userid=userid).update({"password": password})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_user(userid):
    session = Session()
    try:
        session.query(User).filter_by(userid=userid).delete()
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all_equipment():
    session = Session()
    try:
        # order_by menggunakan atribut class, bukan string langsung (kecuali pakai col)
        result = session.query(Item).order_by(Item.jenis.asc()).all()
        return models_to_list(result)
    finally:
        session.close()

def get_equipment(kode):
    session = Session()
    try:
        result = session.query(Item).filter_by(kode=kode).first()
        return model_to_dict(result)
    finally:
        session.close()

def add_equipment(kode, jenis, nama, harga, stok):
    session = Session()
    try:
        new_item = Item(kode=kode, jenis=jenis, nama=nama, harga=harga, stok=stok)
        session.add(new_item)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def update_equipment(kode, jenis, nama, harga, stok):
    session = Session()
    try:
        session.query(Item).filter_by(kode=kode).update({
            "jenis": jenis, "nama": nama, "harga": harga, "stok": stok
        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_equipment(kode):
    session = Session()
    try:
        session.query(Item).filter_by(kode=kode).delete()
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all_rentals():
    session = Session()
    try:
        result = session.query(Rental).all()
        return models_to_list(result)
    finally:
        session.close()

def get_rentals_by_status(status):
    session = Session()
    try:
        result = session.query(Rental).filter_by(status=status).all()
        return models_to_list(result)
    finally:
        session.close()

def get_user_rentals(userid, status=None):
    session = Session()
    try:
        query = session.query(Rental).filter_by(userid=userid)
        if status:
            query = query.filter_by(status=status)
        result = query.all()
        return models_to_list(result)
    finally:
        session.close()

def add_rental(id_transaksi, userid, kode_barang, jumlah, lama_sewa, total_harga, status='active'):
    session = Session()
    try:
        new_rental = Rental(
            id_transaksi=id_transaksi, userid=userid, kode_barang=kode_barang,
            jumlah=jumlah, lama_sewa=lama_sewa, total_harga=total_harga, status=status
        )
        session.add(new_rental)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def update_rental(id_transaksi, userid, kode_barang, jumlah, lama_sewa, total_harga, status):
    session = Session()
    try:
        # Karena id_transaksi adalah Primary Key, kita filter by itu lalu update
        # (Asumsi id_transaksi unik global. Jika komposit, logika filter harus disesuaikan)
        session.query(Rental).filter_by(id_transaksi=id_transaksi).update({
            "jumlah": jumlah, "lama_sewa": lama_sewa, 
            "total_harga": total_harga, "status": status
        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def update_rental_status(id_transaksi, userid, kode_barang, status):
    session = Session()
    try:
        session.query(Rental).filter_by(id_transaksi=id_transaksi).update({
            "status": status
        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_rental(id_transaksi, userid, kode_barang):
    session = Session()
    try:
        # Filter berdasarkan PK id_transaksi sudah cukup untuk delete unik
        session.query(Rental).filter_by(id_transaksi=id_transaksi).delete()
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_last_transaction_id():
    session = Session()
    try:
        # ORDER BY DESC LIMIT 1
        result = session.query(Rental).order_by(Rental.id_transaksi.desc()).first()
        if result:
            return result.id_transaksi
        return None
    finally:
        session.close()