import mysql.connector
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def getLocalDatabaseData():
    # Membuat koneksi ke database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  # Ganti dengan username Anda
        password="123456seven",  # Ganti dengan password Anda
        database="parking"  # Ganti dengan nama database Anda
    )

    mycursor = mydb.cursor()

    # Perintah SQL untuk mengambil data dari tabel parkingSensor
    sql = "SELECT * FROM parkingSensor"

    # Melakukan eksekusi perintah SQL
    mycursor.execute(sql)

    # Mendapatkan semua data hasil eksekusi perintah
    result = mycursor.fetchall()

    # Menutup kursor dan koneksi
    mycursor.close()
    mydb.close()

    return result

# Inisialisasi Firebase Admin SDK dengan credential file
cred = credentials.Certificate("/home/rnd/parking/parking-ezz-firebase-adminsdk-hm6sq-63e2f47eeb.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parking-ezz-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Menggunakan fungsi untuk mendapatkan data dari database lokal
data_from_database = getLocalDatabaseData()

# Mendapatkan instance Firebase Realtime Database
firebase_db = db.reference('/parking1/sensor')

# Mengirim data ke Realtime Database tanpa referensi
for data in data_from_database:
    data_dict = {
        "id": data[0],
        "response": data[1],
        "device": data[2],
        "distance": data[3],
        "min": data[4],
        "max": data[5],
        "status_parking": data[6]
    }
    firebase_db.set(data_dict)

print("Data berhasil dikirim ke Realtime Database tanpa referensi.")
