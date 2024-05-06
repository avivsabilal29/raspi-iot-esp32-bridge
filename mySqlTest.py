import mysql.connector

def upload_data(response, device, distance, min_value, max_value, status):
    try:
        # Membuat koneksi ke database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456seven",  # Ganti dengan password MySQL Anda
            database="parking"  # Ganti dengan nama database Anda
        )

        # Membuat kursor
        cursor = mydb.cursor()

        # Menjalankan perintah SQL untuk menyimpan data ke dalam tabel DeviceStatus
        sql = "INSERT INTO parkingSensor (response, device, distance, min, max, status) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (response, device, distance, min_value, max_value, status)
        cursor.execute(sql, val)

        # Melakukan commit perubahan
        mydb.commit()

        # Menutup koneksi
        cursor.close()
        mydb.close()

        print("Data berhasil diunggah ke tabel DeviceStatus.")

    except mysql.connector.Error as err:
        print("Error:", err)

# Contoh penggunaan:
upload_data(200, "Device1", 100, 50, 200, 1)
