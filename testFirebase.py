import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Inisialisasi Firebase Admin SDK dengan credential file
cred = credentials.Certificate("/home/rnd/parking/parking-ezz-firebase-adminsdk-hm6sq-63e2f47eeb.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parking-ezz-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Mendapatkan referensi ke Realtime Database
ref = db.reference('/parking1')

# Data yang akan dikirim
data = {
    'field1': '20',
    'field2': '11'
}

# Mengirim data ke Realtime Database
ref.set(data)

print("Data berhasil dikirim ke Realtime Database.")
