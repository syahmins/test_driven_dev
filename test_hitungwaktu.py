from datetime import datetime, timedelta, date

# periksa waktu untuk saat ini
sekarang = str(datetime.now())
print('Tanggal/waktu saat ini: ' + sekarang)

# hitung waktu (hari, minggu, bulan, tahun)

# n hari lagi
TambahHari = 5
CariTanggal = datetime.now() + timedelta(days=TambahHari)
print(TambahHari, 'hari lagi adalah tanggal: ' + str(CariTanggal))

# n bulan lagi
TambahBulan = 150
JumlahBulan = TambahBulan / 30
CariBulan = datetime.now() + timedelta(days=TambahBulan)
print(int(JumlahBulan), 'bulan lagi adalah tanggal: ' + str(CariBulan))

# n minggu dan n hari
TambahMinggu = 3
TambahHari2 = 4
MingguHari = datetime.now() + timedelta(weeks=TambahMinggu, days=TambahHari2)
print(int(TambahMinggu), 'minggu dan ', TambahHari2, 'hari dari sekarang adalah ', MingguHari)

# menghitung berapa hari yang sudah terlampaui
# nyd=new year date. Formatnya date(today.year, bulanawaltahun, tanggalawaltahun)
today = date.today()
nyd = date(today.year, 1, 1)


# jika tahun baru sudah terlewati
if nyd < today:
    print('Tahun baru sudah lewat sejak %d hari yang lalu' % (today - nyd).days)

# jika tahun baru belum terlewati
if nyd > today:
    print('Tahun baru akan tiba %d hari lagi' % (today + nyd).days)