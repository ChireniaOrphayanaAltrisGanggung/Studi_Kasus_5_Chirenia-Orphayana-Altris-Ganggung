print("MENGHITUNG BIAYA PARKIR")

kendaraan = input("Masukan Jenis Kendaraan:")
jam_masuk = float(input("Masukan jam masuk:"))
jam_keluar = float(input("masukan jam keluar:"))
durasi = jam_keluar - jam_masuk

def hitung_biaya_parkir(kendaraan, durasi):
    if kendaraan.lower() == "mobil" :
        tarif_parkir = 5000
    elif kendaraan.lower() == "motor" :
        tarif_parkir = 3000


    biaya_parkir = tarif_parkir * durasi
    return biaya_parkir

biaya = hitung_biaya_parkir(kendaraan, durasi)

print("_______________________________")
print("JENIS KENDARAAN :", kendaraan)
print("JAM MASUK :", jam_masuk)
print("JAM KELUAR :", jam_keluar)
print("LAMA PARKIR :", durasi)
print("TOTAL BIAYA PARKIR :", biaya)