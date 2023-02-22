plat = input("Masukkan Plat Nomor : ").split()

try:
    nomor_plat = int(plat)
    nomor = ('Plat nomor tersebut diperuntukan untuk mobil' if nomor_plat == 0 and nomor_plat <= 3000 else(print('Plat nomor tersebut diperuntukan untuk motor' if nomor_plat== 3001 and nomor_plat <= 4000 else(print('Plat nomor tersebut diperuntukan untuk angkutan umum' if nomor_plat == 4001 and nomor_plat <= 5000  else(print('Plat nomor tidak terindikasi ketiga angkutan tersebut')))))))
    print(nomor)
except:
    print('Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan')