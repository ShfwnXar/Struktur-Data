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

    # Meminta inputan pengguna
    nama_produk = input("Masukkan nama produk yang ingin dicari: ")

    # Pencarian data
    cari_laptop_berdasarkan_nama(nama_produk)

except FileNotFoundError:
    print(f"File di {file_path} tidak ditemukan. Silakan periksa jalurnya dan coba lagi.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
