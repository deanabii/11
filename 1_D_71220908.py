hujan = float(input("Masukkan nilai curah hujan : "))

curah = ('Cuaca Terang/Berawan' if hujan == 0 else(print('Curah hujan ringan' if hujan >= 0.5 and hujan <= 20 else(print('Curah hujan sedang' if hujan >= 21 and hujan <=50 else(print('Curah hujan lebat' if hujan>= 51 and hujan <= 100 else(print('Curah hujan ekstrem' if hujan >100 else(print("BENCANA ALAMM")))))))))))
print(curah)