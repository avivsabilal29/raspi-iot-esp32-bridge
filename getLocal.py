import mysql.connector

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

# Menggunakan fungsi untuk mendapatkan data dari database lokal
data_from_database = getLocalDatabaseData()

# Membuat list untuk menyimpan data dalam bentuk dictionary
data_list = []

# Menyusun data dari hasil query ke dalam dictionary dan dimasukkan ke dalam list
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
    data_list.append(data_dict)

# Menampilkan data dalam list
for data in data_list:
    print(data)
