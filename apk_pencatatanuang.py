saldo=0

def cek_saldo():
    print ("Saldo anda Rp {} " .format(saldo))

def tarik_tunai(jumlah_tarik_tunai):
    global saldo

    print ("Saldo anda Rp {} " .format(saldo))
    saldo=saldo-jumlah_tarik_tunai
    print ("Saldo anda sekarang Rp {}".format(saldo))

def setor_tunai(jumlah_setor_tunai):
    global saldo

    print ("Saldo anda Rp {} " .format(saldo))
    saldo=saldo+jumlah_setor_tunai
    print ("Saldo anda sekarang Rp {}".format(saldo))

pilihan = None
jumlah = None
menu = None

while True :
    print ("""
    SELMAT DATANG DI APLIKASI PENCATATAN UANG
    =========================================
    1. Cek Saldo
    2. Tarik Tunai
    3. Setor Tunai
    4. Keluar
    """)

    menu = int(input("Silahkan masukkan menu : "))
    if menu==1:
        print (""" 
        PILIH SIMPANAN TABUNGAN
        =======================
        1. Tabungan Pribadi
        2. Tabungan Umum
        """)
        pilihan = int (input("Silahkan masukkan pilihan :  "))
        if pilihan==1:
           cek_saldo()
        elif pilihan==2:
            cek_saldo()
        else :
            print ("Pilihan salah, silahkan coba lagi!")
    elif menu==2:
        print (""" 
        PILIH SIMPANAN TABUNGAN
        =======================
        1. Tabungan Pribadi
        2. Tabungan Umum
        """)
        pilihan = int (input("Silahkan masukkan pilihan :  "))
        if pilihan==1:
            jumlah=int(input("Masukkan jumlah tarik tunai : "))
            tarik_tunai(jumlah)
        elif pilihan==2:
            jumlah=int(input("Masukkan jumlah tarik tunai : "))
            tarik_tunai(jumlah)
        else :
            print ("Pilihan salah, silahkan coba lagi!")
    elif menu==3:
        print (""" 
        PILIH SIMPANAN TABUNGAN
        =======================
        1. Tabungan Pribadi
        2. Tabungan Umum
        """)
        pilihan = int (input("Silahkan masukkan pilihan :  "))
        if pilihan==1:
            jumlah=int(input("Masukkan jumlah setor tunai: "))
            setor_tunai(jumlah)
        elif pilihan==2:
            jumlah=int(input("Masukkan jumlah setor tunai: "))
            setor_tunai(jumlah)
        else :
            print ("Pilihan salah, silahkan coba lagi!")
    elif menu==4:
        print ("Terimakasih")
    else :
        print ("Menu salah, silahkan coba lagi!")


