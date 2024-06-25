import pandas as pd

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
                if kunci.lower() in saat_ini.kunci.lower():
                    hasil.append(saat_ini.data)
                stack.append(saat_ini.kanan)
                stack.append(saat_ini.kiri)

        return hasil

# Memuat data laptop dari file CSV
file_path = 'C:/Users/ASUS/PycharmProjects/pythonProject4/hargalaptop.csv'
data_laptop = muat_data(file_path)

# Membuat instance dari PohonPencarianBiner untuk produk dan perusahaan
pohon_produk = PohonPencarianBiner()
pohon_perusahaan = PohonPencarianBiner()

# Memasukkan data ke dalam pohon
for index, row in data_laptop.iterrows():
    pohon_produk.masukkan(row['Product'], row)
    pohon_perusahaan.masukkan(row['Company'], row)

# Fungsi untuk mencari data berdasarkan nama produk atau perusahaan menggunakan DFS
def dfs_cari_laptop(pohon, kata_kunci, jenis_pencarian):
    hasil = pohon.dfs_cari(kata_kunci)
    if hasil:
        print(f"Data yang cocok dengan {jenis_pencarian} yang mengandung '{kata_kunci}':")
        for item in hasil:
            print(item)
    else:
        print(f"Tidak ditemukan data yang cocok dengan {jenis_pencarian} yang mengandung '{kata_kunci}'")

# Meminta input pengguna
jenis_pencarian = input("Masukkan jenis pencarian ('nama device' atau 'Perusahaan pembuat'): ")
kata_kunci = input(f"Masukkan nama {jenis_pencarian} yang ingin dicari: ")

# Pencarian data menggunakan DFS
if jenis_pencarian.lower() == 'nama device':
    dfs_cari_laptop(pohon_produk, kata_kunci, jenis_pencarian)
elif jenis_pencarian.lower() == 'perusahaan pembuat':
    dfs_cari_laptop(pohon_perusahaan, kata_kunci, jenis_pencarian)
else:
    print("Jenis pencarian tidak valid. Silakan masukkan 'nama device' atau 'Perusahaan pembuat'.")
