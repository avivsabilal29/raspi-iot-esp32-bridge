import requests
import time
import mysql.connector

def sendLocalDatabase():
    # Membuat koneksi ke database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # Ganti dengan username Anda
    password="123456seven",  # Ganti dengan password Anda
    database="parking"  # Ganti dengan nama database Anda
    )
    data = getSensorInfo(url, token)
    mycursor = mydb.cursor()
    # Perintah SQL untuk melakukan update data berdasarkan id
    sql = "UPDATE parkingSensor SET response = %s, device = %s, distance = %s, min = %s, max = %s, status = %s WHERE id = %s"
    # Menyiapkan data untuk diupdate
    data_to_update = (data["response"], data["device"], data["distance"], data["min"], data["max"], data["status_parking"], data["id"])
    # Melakukan update data
    mycursor.execute(sql, data_to_update)

    # Melakukan commit perubahan
    mydb.commit()

    # Menampilkan jumlah baris yang telah diupdate
    print(mycursor.rowcount, "baris telah diupdate.")

    # Menutup koneksi
    mycursor.close()
    mydb.close()


# Fungsi untuk mengirim permintaan GET dengan nilai acak
def getSensorInfo(url, token):
    # Membuat URL dengan token dan nilai acak
    request_url = f"{url}{token}"
    # Mengirim permintaan GET
    response = requests.get(request_url)
    # Mengecek status respons
    if response.status_code == 200:
        # Mem-parsing respons JSON
        data = response.json()["data"]
        parsed_data = {
            "id": 1,
            "response" : response.status_code,
            "device": response.json()["device"],
            "status": response.json()["status"],
            "message": response.json()["message"],
            "distance": data["distance"],
            "min": data["minimum_distance"],
            "max": data["maximum_distance"],
            "status_parking": data["status_parking"]
        }
        return parsed_data
    else:
        print("Gagal mengirim permintaan.")
        return None

# URL untuk mengirimkan permintaan GET
url = "http://192.168.1.27"
# Token Blynk Anda
token = "/api/get/sensor/info"

# Loop untuk mengirimkan permintaan secara berulang-ulang
while True:
    sendLocalDatabase()
    time.sleep(1)
