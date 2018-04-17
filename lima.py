def fe():
    print("Modul Nomor Telephone")
#Buat Dictionary a dengan data Nama dan Nomor Telephone a saya ganti 1
dic1={'nama1' : 'Jane Doe', 'nama2' : 'John Smith', 'nama3' : 'Bob Stone',
      'telp1' : '+27 555 5367', 'telp2' : '+27 555 6254', 'telp3' : '+27 555 5689'}

print ' Name      Telephone Number'
print dic1['nama1'],'  ', dic1['telp1'],'\n', dic1['nama2'],'',dic1['telp2'],'\n', dic1['nama3'],' ',dic1['telp3']

#Mengubah Nomor Jane Doe
dic1['telp1']='+27 555 1024'
print'\nUbah nomor Telephone Jane Doe'
print ' Name      Telephone Number'
print dic1['nama1'],'  ', dic1['telp1'],'\n', dic1['nama2'],'',dic1['telp2'],'\n', dic1['nama3'],' ',dic1['telp3']

#Tambah Data Baru
dic1['nama4']='Anna Coper'
dic1['telp4']='+27 555 3237'
print '\n   Menambah Data Baru'
print ' Name      Telephone Number'
print dic1['nama1'],'  ', dic1['telp1'],'\n', dic1['nama2'],'',dic1['telp2'],'\n', dic1['nama3'],' ',dic1['telp3'],'\n',dic1['nama4'],'',dic1['telp4']

#Mencetak Nomor Telephone Bob Stone
print '\nCetak Nomor Telephone Bob Stone = ', dic1['telp3']

#Menampilkan semua Key
print '\nCetak semua KEY = ', dic1.keys()

#Menampilkan semua Value
print '\nCetak semua Values = ', dic1.values()
