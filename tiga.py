def fc():
    print("Modul Nilai Append")
i=0
nm = []
ni = []
tu = []
ut = []
ua = []
akhi = []

while True :
    na = raw_input("Nama\t\t: ")
    nm.append(na)
    nim = input("NIM\t\t: ")
    ni.append(nim)
    nilai_tugas = input("Nilai Tugas\t: ")
    tu.append(nilai_tugas)
    nilai_uts = input("Nilai UTS\t: ")
    ut.append(nilai_uts)
    nilai_uas = input("Nilai UAS\t: ")
    ua.append(nilai_uas)
    akhir = (nilai_tugas+nilai_uts+nilai_uas)/3
    akhi.append(akhir)

    data = ''
    while data!='y' and data!='t':
        data = raw_input("Tambah Data (y/t)? ")
    i+=1
    if(data == "t"):
        break


print "==============================================================="
print " No | Nama | NIM  | Tugas  | UTS  | UAS  | Akhir "
print "==============================================================="
for n in range(i):
     print (" | {n:2d} | {nm:11s} | {ni:5d} | {tu:5d} | {ut:5d} | {ua:5d} | {akhi:5d}". format(nm=nm[n], ni=ni[n], tu=tu[n], ut=ut[n], ua=ua[n], akhi=akhi[n], n=n+1))
     
