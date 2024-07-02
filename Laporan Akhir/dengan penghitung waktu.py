import pandas as pd
import time

# Fungsi untuk memuat data dari file CSV
def muat_data(file_path):
    return pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')

# Kelas TreeNode untuk struktur data pohon
class NodePohon:
    def __init__(self, kunci, data):
        self.kiri = None
        self.kanan = None
        self.kunci = kunci
        self.data = data

# Kelas BinarySearchTree untuk mengelola pohon
class PohonPencarianBiner:
    def __init__(self):
        self.akar = None

    def masukkan(self, kunci, data):
        if self.akar is None:
            self.akar = NodePohon(kunci, data)
        else:
            self._masukkan(self.akar, kunci, data)

    def _masukkan(self, node, kunci, data):
        if kunci < node.kunci:
            if node.kiri is None:
                node.kiri = NodePohon(kunci, data)
            else:
                self._masukkan(node.kiri, kunci, data)
        else:
            if node.kanan is None:
                node.kanan = NodePohon(kunci, data)
            else:
                self._masukkan(node.kanan, kunci, data)

    def dfs_cari(self, kunci):
        return self._dfs_cari(self.akar, kunci)

    def _dfs_cari(self, node, kunci):
        hasil = []
        stack = [node]

        while stack:
            saat_ini = stack.pop()
            if saat_ini is not None:
                if kunci.lower() in str(saat_ini.kunci).lower():
                    hasil.append(saat_ini.data)
                stack.append(saat_ini.kanan)
                stack.append(saat_ini.kiri)

        return hasil

# Memuat data laptop dari file CSV
file_path = 'C:/Users/ASUS/PycharmProjects/pythonProject4/hargalaptop.csv'
data_laptop = muat_data(file_path)

# Membuat instance dari PohonPencarianBiner untuk produk dan harga
pohon_produk = PohonPencarianBiner()
pohon_harga = PohonPencarianBiner()

# Memasukkan data ke dalam pohon
for index, row in data_laptop.iterrows():
    pohon_produk.masukkan(row['Product'], row)
    pohon_harga.masukkan(str(row['Price_in_euros']), row)

# Fungsi untuk mencari data berdasarkan nama produk atau harga menggunakan DFS
def dfs_cari_laptop(pohon, kata_kunci, jenis_pencarian):
    start_time = time.time()  # Mulai penghitungan waktu
    hasil = pohon.dfs_cari(kata_kunci)
    end_time = time.time()  # Akhir penghitungan waktu

    if hasil:
        print(f"Data yang cocok dengan {jenis_pencarian} yang mengandung '{kata_kunci}':")
        for item in hasil:
            print(item)
    else:
        print(f"Tidak ditemukan data yang cocok dengan {jenis_pencarian} yang mengandung '{kata_kunci}'")

    print(f"Waktu eksekusi: {end_time - start_time} detik")  # Tampilkan waktu eksekusi

# Meminta input pengguna
while True:
    print("Masukkan jenis pencarian:")
    print("1. Product")
    print("2. Price_in_euros")
    print("3. Akhiri program")
    jenis_pencarian = input("Pilihan (1, 2, atau 3): ")

    if jenis_pencarian == '1':
        kata_kunci = input("Masukkan Product yang ingin dicari: ")
        dfs_cari_laptop(pohon_produk, kata_kunci, 'Product')
    elif jenis_pencarian == '2':
        kata_kunci = input("Masukkan Price_in_euros yang ingin dicari: ")
        dfs_cari_laptop(pohon_harga, kata_kunci, 'Price_in_euros')
    elif jenis_pencarian == '3':
        print("Program berakhir.")
        break
    else:
        print("Jenis pencarian tidak valid. Silakan masukkan '1', '2', atau '3'.")
