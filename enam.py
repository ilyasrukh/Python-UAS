def ff():
    print ("Tugas Kalkulator")
#fungsi penjumlahan
def penjumlahan(a,b):
    penjumlahan = a+b
    return penjumlahan
#fungsi pengurangan
def pengurangan(a,b):
    pengurangan = a-b
    return pengurangan
#fungsi perkalian
def perkalian(a,b):
    perkalian = a*b
    return perkalian
#fungsi pembagian
def pembagian(a,b):
    pembagian = a/b
    return pembagian

lagi= 'y'
while lagi=='y':
    #menu operasi
    print ("\n\t Program Kalkulator \n")
    print (" 1. Penjumlahan \n 2. Pengurangan \n 3. Perkalian \n 4. Pembagian \n")
    #meminta input user
    a = int(input("Masukkan Bilangan 1: "))
    b = int(input("Masukkan Bilangan 2: "))
    c = input("Masukkan pilihan anda [1/2/3/4] : ")
    if (c=='1'):
        print (a,"+",b,"=", penjumlahan(a,b))
    elif (c=='2'):
        print (a,"-",b,"=", pengurangan(a,b))
    elif (c=='3'):
        print (a,"*",b,"=", perkalian(a,b))
    elif (c=='4'):
        print (a,"/",b,"=", pembagian(a,b))
    else :
        print ("Pilihan anda tidak tersedia")


    lagi= input("Ulang lagi [y/t]? ")
