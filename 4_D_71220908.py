nama = str(input("Masukkan Nama Lengkap Anda: "))
prodi = str(input("Masukkan Prodi Anda: "))
nilai = input("Masukkan Nilai (dalam Huruf) yang Anda Dapat: ")

try:
    if nilai == 'A':
        print("Nilai anda adalah 4.0, tbl tbl serem bgt lohh")
    elif nilai == 'A-':
        print("Nilai anda adalah 3.75, kamu keren!")
    elif nilai == 'B+':
        print("Nilai anda adalah 3.25, Lumayanlah")
    elif nilai == 'B':
        print("Nilai anda adalah 3.0, Yuk bisa yukk dikit lagi")
    elif nilai == 'B-':
        print("Nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif nilai == 'C+':
        print("Nilai anda adlaah 2.25, Aduhh gimana nihhh")
    elif nilai == 'C':
        print("Nilai anda adalah 2.0, Kamu mau pindah jurusan kah?")
    elif nilai == 'D':
        print("Nilai anda adalah 1, apakah sudah anda pikirkan untuk pindah jurusan?")
    elif nilai == 'E':
        print("Nilai anda adalah 0, niat kuliah nggak sihh???")
except:
    print("Inputan nilai yang anda masukkan tidak valid")