import pandas as pd

# Berikan jalur yang benar menuju file CSV Anda
file_path = 'C:/Users/ASUS/PycharmProjects/pythonProject4/hargalaptop.csv'

try:
    # Memuat file CSV dengan delimiter titik koma dan encoding yang sesuai
    laptop_data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')

    # Menampilkan beberapa baris pertama dari dataframe untuk verifikasi
    print("Data berhasil dimuat. Berikut adalah beberapa baris pertama:")
    print(laptop_data.head())

    # Fungsi untuk mencari data berdasarkan nama produk
    def cari_laptop_berdasarkan_nama(nama_produk):
        hasil_pencarian = laptop_data[laptop_data['Product'].str.contains(nama_produk, case=False, na=False)]
        if not hasil_pencarian.empty:
            print(f"Data yang cocok dengan nama produk '{nama_produk}':")
            print(hasil_pencarian)
        else:
            print(f"Tidak ditemukan data yang cocok dengan nama produk '{nama_produk}'")

    # Fungsi untuk mencari data berdasarkan harga
    def cari_laptop_berdasarkan_harga(harga):
        hasil_pencarian = laptop_data[laptop_data['Price_in_euros'] == float(harga)]
        if not hasil_pencarian.empty:
            print(f"Data yang cocok dengan harga '{harga}':")
            print(hasil_pencarian)
        else:
            print(f"Tidak ditemukan data yang cocok dengan harga '{harga}'")

    # Meminta inputan pengguna
    while True:
        print("Masukkan jenis pencarian:")
        print("1. Product")
        print("2. Price_in_euros")
        print("3. Akhiri program")
        pilihan = input("Pilihan (1, 2, atau 3): ")

        if pilihan == '1':
            nama_produk = input("Masukkan nama produk yang ingin dicari: ")
            cari_laptop_berdasarkan_nama(nama_produk)
        elif pilihan == '2':
            harga = input("Masukkan harga (Price_in_euros) yang ingin dicari: ")
            cari_laptop_berdasarkan_harga(harga)
        elif pilihan == '3':
            print("Program berakhir.")
            break
        else:
            print("Jenis pencarian tidak valid. Silakan masukkan '1', '2', atau '3'.")

except FileNotFoundError:
    print(f"File di {file_path} tidak ditemukan. Silakan periksa jalurnya dan coba lagi.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
