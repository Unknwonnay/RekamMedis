import os
from time import process_time_ns
from traceback import print_tb

MAKSDATA = 10

NoRM            = ['/'] * MAKSDATA
Nama            = ['/'] * MAKSDATA
JenisKelamin    = ['/'] * MAKSDATA
TanggalPeriksa  = ['/'] * MAKSDATA
BeratBadan      = [0] * MAKSDATA
TinggiBadan     = [0] * MAKSDATA
Diagnosa        = ['/'] * MAKSDATA

def Test(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    NoRM[0]             = 'A-01'
    Nama[0]             = 'Aido'
    JenisKelamin[0]     = 'P'
    TanggalPeriksa[0]   = '01-01-2024'
    BeratBadan[0]       = 50
    TinggiBadan[0]      = 160
    Diagnosa[0]         = 'Demam'

    NoRM[1]             = 'A-02'
    Nama[1]             = 'Budi'
    JenisKelamin[1]     = 'L'
    TanggalPeriksa[1]   = '120225'
    BeratBadan[1]       = 76
    TinggiBadan[1]      = 170
    Diagnosa[1]         = 'Demam'

    
    NoRM[2]             = 'A-03'
    Nama[2]             = 'Yanto'
    JenisKelamin[2]     = 'L'
    TanggalPeriksa[2]   = '120225'
    BeratBadan[2]       = 60
    TinggiBadan[2]      = 150
    Diagnosa[2]         = 'Demam'

    
    NoRM[3]             = 'A-04'
    Nama[3]             = 'Gusti'
    JenisKelamin[3]     = 'L'
    TanggalPeriksa[3]   = '120225'
    BeratBadan[3]       = 80
    TinggiBadan[3]      = 160
    Diagnosa[3]         = 'Diare'

    BanyakData = 4
    return BanyakData

def MenuPilihan(Pilihan):
    print('+=====================+')
    print('|     REKAM MEDIS     |')
    print('+=====================+')
    print('|      1. Pasien      |')
    print('|      2. Dokter      |')
    print('|      0. Keluar      |')
    print('+=====================+')
    Pilihan = int(input('Pilihan ? '))

    while(Pilihan  < 0) or (Pilihan  > 2):
        print('Pilih yang ada di menu!')
        input()

        os.system('clear')
        print('+=====================+')
        print('|     REKAM MEDIS     |')
        print('+=====================+')
        print('|      1. Pasien      |')
        print('|      2. Dokter      |')
        print('|      0. Keluar      |')
        print('+=====================+')
        Pilihan = int(input('Pilihan ? '))
    
    return Pilihan

def MenuPasien(PilihanPasien):
    print('+================================+')
    print('|          MENU PASIEN           |')
    print('+================================+')
    print('|         1. Cari Data           |')
    print('|         0. Keluar              |')
    print('+================================+')
    PilihanPasien = int(input('Pilihan ? '))

    while(PilihanPasien  < 0) or (PilihanPasien  > 1):
        print('Pilih yang ada di menu!')
        input()

        os.system('clear')
        print('+================================+')
        print('|          MENU PASIEN           |')
        print('+================================+')
        print('|         1. Cari Data           |')
        print('|         0. Keluar              |')
        print('+================================+')
        PilihanPasien = int(input('Pilihan ? '))

    return PilihanPasien

def MenuDokter(PilihanDokter):
    print('+=====================================+')
    print('|            MENU DOKTER              |')
    print('+=====================================+')
    print('|          1. Isi Data                |')
    print('|          2. Tampilkan Data          |')
    print('|          3. Edit Data               |')
    print('|          4. Pengurutan Data         |')
    print('|          5. Pencarian Data          |')
    print('|          6. Penghapusan Data        |')
    print('|          7. Penghancuran Data       |')
    print('|          8. Rekap Rekam Medis       |')
    print('|          0. Keluar                  |')
    print('+=====================================+')
    PilihanDokter = int(input('Pilihan ? '))

    while(PilihanDokter  < 0) or (PilihanDokter  > 8):
        print('Pilih yang ada di menu!')
        input()

        os.system('clear')
        print('+=====================================+')
        print('|            MENU DOKTER              |')
        print('+=====================================+')
        print('|          1. Isi Data                |')
        print('|          2. Tampilkan Data          |')
        print('|          3. Edit Data               |')
        print('|          4. Pengurutan Data         |')
        print('|          5. Pencarian Data          |')
        print('|          6. Penghapusan Data        |')
        print('|          7. Penghancuran Data       |')
        print('|          8. Rekap Rekam Medis       |')
        print('|          0. Keluar                  |')
        print('+=====================================+')
        PilihanDokter = int(input('Pilihan ? '))

    return PilihanDokter

def IsiData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    Status = True
    i = BanyakData
    print('----------------------DATA KE-', i+1, '--------------')
    NoRM[i]           = input('No.Rekam Medis             : ')

    while(NoRM[i].upper() != 'STOP' and i < MAKSDATA and Status):
        Nama[i]           = str(input('Nama                       : '))
        JenisKelamin[i]   = str(input('Jenis Kelamin              : '))
        TanggalPeriksa[i] = str(input('Tanggal Periksa            : '))
        BeratBadan[i]     = int(input('Berat Badan                : '))
        TinggiBadan[i]    = int(input('Tinggi Badan               : '))
        Diagnosa[i]       = str(input('Diagnosa                   : '))
        i = i + 1

        if i < MAKSDATA:
            print('----------------------DATA KE-', i+1, '--------------')
            NoRM[i] = str(input('No.Rekam Medis             : '))
        else:
            print('Array Penuh!')
            Status = False

    BanyakData = i

    return BanyakData

def EditData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    if(BanyakData == 0):
        print('Belum ada data!')
    else:
        print('+--------------------------------------------------+')
        print('| No |No. Rekam Medis |           Nama             |')

        for i in range(BanyakData):
            print('+--------------------------------------------------+')
            print(f'| {i+1:2} | {NoRM[i]:15} | {Nama[i]:25} |')
        print('+--------------------------------------------------+')

        NoEdit = int(input('Data yang mau di edit(No.RM)? '))

        while(NoEdit < 0) or (NoEdit > BanyakData):
            print('Pilih no yang ada')
            input()
            os.system('clear')
            print('+--------------------------------------------------+')
            print('| No |No. Rekam Medis |           Nama             |')

            for i in range(BanyakData):
                print('+--------------------------------------------------+')
                print(f'| {i+1:2} | {NoRM[i]:15} | {Nama[i]:25} |')
            print('+--------------------------------------------------+')

            NoEdit = int(input('Data yang mau di edit(No.RM)? '))
        
       
        os.system('clear')
        print('+=====================================+')
        print('|        PILIH YANG MAU DI EDIT       |')
        print('+=====================================+')
        print('|           1. Nama                   |')
        print('|           2. Jenis Kelamin          |')
        print('|           3. Tanggaal Periksa       |')
        print('|           4. Berat Badan            |')
        print('|           5. Tinggi Badan           |')
        print('|           6. Diagnosa               |')
        print('|           0. Keluar                 |')
        print('+=====================================+')
        PilihanEdit = int(input('Pilihan?'))

        match(PilihanEdit):
            case 1:
                os.system('clear')
                Nama[NoEdit-1] = input('Nama Baru : ')
            case 2:
                os.system('clear')
                JenisKelamin[NoEdit-1] = input('Jenis Kelamin Baru : ')
            case 3:
                os.system('clear')
                TanggalPeriksa[NoEdit-1] = input('Tanggal Periksa Baru : ')
            case 4:
                os.system('clear')
                BeratBadan[NoEdit-1] = int(input('Berat Badan Baru : '))
            case 5:
                os.system('clear')
                TinggiBadan[NoEdit-1] = int(input('Tinggi Badan Baru : '))
            case 6:
                os.system('clear')
                Diagnosa[NoEdit-1] = input('Diagnosa Baru : ')
        print()
        print('Data berhasil diubah!')
    input()

def TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):

    for i in range(BanyakData):
        print('+-------------------------------------------------------+')
        print(f'|                 DATA PASIEN-{i+1:<2}                        |')
        print('+-------------------------------------------------------+')
        print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
        print(f'| Nama                       : {Nama[i]:15}          |')
        print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
        print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
        print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
        print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
        print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
        print('+-------------------------------------------------------+')

def MenuPengurutan(PilihanPengurutan):
    print ('+=====================================+')
    print ('|           MENU PENGURUTAN           |')
    print ('+=====================================+')
    print ('|            1. Ascending             |')
    print ('|            2. Descending            |')
    print ('|            0. Keluar                |')
    print ('+=====================================+')
    PilihanPengurutan = int(input('Pilihan?'))
    return PilihanPengurutan

def MenuSortingAsc(PilihanAsc):
    print('+===========================================+')
    print('|       MENGURUTKAN DATA SECARA MENAIK      |')
    print('+===========================================+')
    print('|            1. No. Rekam Medis             |')
    print('|            2. Nama                        |')
    print('|            3. Tanggal Periksa             |')
    print('|            4. Berat Badan                 |')
    print('|            5. Tinggi Badan                |')
    print('|            0. Keluar                      |')
    print('+===========================================+')
    PilihanAsc = int(input('Pilihan?'))
    return PilihanAsc

#PENGURUTAN ASCENDING
def UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData-1,i+1,-1):
            if NoRM[j] < NoRM[j-1]:
                Temp = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = Temp
                
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp

                Temp = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = Temp

                Temp = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = Temp

                Temp = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = Temp

                Temp = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = Temp

                Temp = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = Temp

def UrutNamaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData-1,i+1,-1):
            if Nama[j] < Nama[j-1]:
                Temp = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = Temp
                
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp

                Temp = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = Temp

                Temp = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = Temp

                Temp = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = Temp

                Temp = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = Temp

                Temp = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = Temp

def UrutTanggalPeriksaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData-1,i+1,-1):
            if TanggalPeriksa[j] < TanggalPeriksa[j-1]:
                Temp = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = Temp
                
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp

                Temp = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = Temp

                Temp = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = Temp

                Temp = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = Temp

                Temp = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = Temp

                Temp = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = Temp

#Minimum Sort Asc
def UrutBeratBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        min = i
        for j in range(i+1,BanyakData):
            if (BeratBadan[j] < BeratBadan[min]):
                min = j
        Temp = Nama[i]
        Nama[i] = Nama[min]
        Nama[min] = Temp

        Temp = NoRM[i]
        NoRM[i] = NoRM[min]
        NoRM[min] = Temp
        
        Temp = JenisKelamin[i]
        JenisKelamin[i] = JenisKelamin[min]
        JenisKelamin[min] = Temp

        Temp = TanggalPeriksa[i]
        TanggalPeriksa[i] = TanggalPeriksa[min]
        TanggalPeriksa[min] = Temp

        Temp = BeratBadan[i]
        BeratBadan[i] = BeratBadan[min]
        BeratBadan[min] = Temp

        Temp = TinggiBadan[i]
        TinggiBadan[i] = TinggiBadan[min]
        TinggiBadan[min] = Temp

        Temp = Diagnosa[i]
        Diagnosa[i] = Diagnosa[min]
        Diagnosa[min] = Temp

#Maximum Sort Asc
def UrutTinggiBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        max = 0
        for j in range(1,BanyakData+1-(i+1)):
            if (TinggiBadan[j] > TinggiBadan[max]):
                max = j

        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp

        Temp = NoRM[j]
        NoRM[j] = NoRM[max]
        NoRM[max] = Temp
        
        Temp = JenisKelamin[j]
        JenisKelamin[j] = JenisKelamin[max]
        JenisKelamin[max] = Temp

        Temp = TanggalPeriksa[j]
        TanggalPeriksa[j] = TanggalPeriksa[max]
        TanggalPeriksa[max] = Temp

        Temp = BeratBadan[j]
        BeratBadan[j] = BeratBadan[max]
        BeratBadan[max] = Temp

        Temp = TinggiBadan[j]
        TinggiBadan[j] = TinggiBadan[max]
        TinggiBadan[max] = Temp

        Temp = Diagnosa[j]
        Diagnosa[j] = Diagnosa[max]
        Diagnosa[max] = Temp

#PENGURUTAN DESCENDING
def UrutNoRMDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range((BanyakData-1)-i):
            if(NoRM[j] < NoRM[j+1]):
                Temp = NoRM[j]
                NoRM[j] = NoRM[j+1]
                NoRM[j+1] = Temp
                
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp

                Temp = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j+1]
                JenisKelamin[j+1] = Temp

                Temp = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j+1]
                TanggalPeriksa[j+1] = Temp

                Temp = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j+1]
                BeratBadan[j+1] = Temp

                Temp = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j+1]
                TinggiBadan[j+1] = Temp

                Temp = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j+1]
                Diagnosa[j+1] = Temp

def UrutNamaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range((BanyakData-1)-i):
            if(Nama[j] < Nama[j+1]):
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp

                Temp = NoRM[j]
                NoRM[j] = NoRM[j+1]
                NoRM[j+1] = Temp
                
                Temp = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j+1]
                JenisKelamin[j+1] = Temp

                Temp = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j+1]
                TanggalPeriksa[j+1] = Temp

                Temp = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j+1]
                BeratBadan[j+1] = Temp

                Temp = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j+1]
                TinggiBadan[j+1] = Temp

                Temp = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j+1]
                Diagnosa[j+1] = Temp

def UrutTanggalPeriksaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range((BanyakData-1)-i):
            if(TanggalPeriksa[j] < TanggalPeriksa[j+1]):
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j+1] = Temp

                Temp = NoRM[j]
                NoRM[j] = NoRM[j+1]
                NoRM[j+1] = Temp
                
                Temp = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j+1]
                JenisKelamin[j+1] = Temp

                Temp = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j+1]
                TanggalPeriksa[j+1] = Temp

                Temp = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j+1]
                BeratBadan[j+1] = Temp

                Temp = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j+1]
                TinggiBadan[j+1] = Temp

                Temp = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j+1]
                Diagnosa[j+1] = Temp


#Maximum Sort Desc
def UrutBeratBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        max = 0
        for j in range(1,BanyakData+1-(i+1)):
            if (BeratBadan[j] < BeratBadan[max]):
                max = j
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp

        Temp = NoRM[j]
        NoRM[j] = NoRM[max]
        NoRM[max] = Temp
            
        Temp = JenisKelamin[j]
        JenisKelamin[j] = JenisKelamin[max]
        JenisKelamin[max] = Temp

        Temp = TanggalPeriksa[j]
        TanggalPeriksa[j] = TanggalPeriksa[max]
        TanggalPeriksa[max] = Temp

        Temp = BeratBadan[j]
        BeratBadan[j] = BeratBadan[max]
        BeratBadan[max] = Temp

        Temp = TinggiBadan[j]
        TinggiBadan[j] = TinggiBadan[max]
        TinggiBadan[max] = Temp

        Temp = Diagnosa[j]
        Diagnosa[j] = Diagnosa[max]
        Diagnosa[max] = Temp


#Minimum Sort Desc
def  UrutTinggiBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        min = i
        for j in range(i+1,BanyakData):
            if (TinggiBadan[j] > TinggiBadan[min]):
                min = j

        Temp = TinggiBadan[min]
        TinggiBadan[min] = TinggiBadan[i]
        TinggiBadan[i] = Temp

        Temp = NoRM[min]
        NoRM[min] = NoRM[i]
        NoRM[i] = Temp

        Temp = Nama[min]
        Nama[min] = Nama[i]
        Nama[i] = Temp

        Temp = JenisKelamin[min]
        JenisKelamin[min] = JenisKelamin[i]
        JenisKelamin[i] = Temp

        Temp = TanggalPeriksa[min]
        TanggalPeriksa[min] = TanggalPeriksa[i]
        TanggalPeriksa[i] = Temp

        Temp = BeratBadan[min]
        BeratBadan[min] = BeratBadan[i]
        BeratBadan[i] = Temp

        Temp = Diagnosa[min]
        Diagnosa[min] = Diagnosa[i]
        Diagnosa[i] = Temp

def MenuPengurutan(PilihanPengurutan):
    if(BanyakData == 0):
        print('Belum ada data!')
    else:
        print('+=====================================+')
        print('|           MENU PENGURUTAN           |')
        print('+=====================================+')
        print('|            1. Ascending             |')
        print('|            2. Descending            |')
        print('|            0. Keluar                |')
        print('+=====================================+')
        PilihanPengurutan = int(input('Pilihan? '))
    return PilihanPengurutan



def MenuSortingDsc(PilihanDsc):
    if(BanyakData == 0):
        print('Belum ada data!')
    else:
        print('+===========================================+')
        print('|       MENGURUTKAN DATA SECARA MENURUN      |')
        print('+===========================================+')
        print('|            1. No. Rekam Medis             |')
        print('|            2. Nama                        |')
        print('|            3. Tanggal Periksa             |')
        print('|            4. Berat Badan                 |')
        print('|            5. Tinggi Badan                |')
        print('|            0. Keluar                      |')
        print('+===========================================+')
        PilihanDsc = int(input('Pilihan?'))
    return PilihanDsc

def MenuPencarian(PilihanPencarian):
    if(BanyakData == 0):
        print('Belum ada data!')
    else:
        print('+===========================================+')
        print('|               MENU PENCARIAN              |')
        print('+===========================================+')
        print('|            1. Cari No. Rekam Medis        |')
        print('|            2. Cari Nama                   |')
        print('|            3. Cari Jenis Kelamin          |')
        print('|            4. Cari Tanggal Periksa        |')
        print('|            5. Cari Berat Badan            |')
        print('|            6. Cari Tinggi Badan           |')
        print('|            7. Cari Diagnosis              |')
        print('|            0. Keluar                      |')
        print('+===========================================+')
        PilihanPencarian = int(input('Pilihan?'))
    return PilihanPencarian

def PenghancuranArray(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa):
    for i in range(MAKSDATA):
        NoRM[i]           = 0
        Nama[i]           = 0
        JenisKelamin[i]   = 0
        TanggalPeriksa[i] = 0
        BeratBadan[i]     = 0
        TinggiBadan[i]    = 0
        Diagnosa[i]       = 0

    BanyakData = 0
    print('Data berhasil dihancurkan!')
    input()
    return BanyakData 

def CariNoRM(NoRM, BanyakData):

    DataCari = str(input('No. Rekam Medis yang dicari? '))
    Ia = 0
    Ib = BanyakData
    Ketemu = False

    while(not Ketemu) and(Ia <= Ib):
        K = (Ia + Ib) // 2

        if(NoRM[K] == DataCari):
            Ketemu = True
        else:
            if(NoRM[K] < DataCari):
                Ia = K + 1
            else:
                Ib = K - 1
    
    if(Ketemu):
        print('+-------------------------------------------------------+')
        print(f'|                 DATA PASIEN-{K+1:<2}                        |')
        print('+-------------------------------------------------------+')
        print(f'| No. Rekam Medis            : {NoRM[K]:8}                 |')
        print(f'| Nama                       : {Nama[K]:15}          |')
        print(f'| Jenis Kelamin              : {JenisKelamin[K]:2}                       |')
        print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[K]:10}               |')
        print(f'| Berat Badan                : {BeratBadan[K]:<5} kg                 |')
        print(f'| Tinggi Badan               : {TinggiBadan[K]:<5} cm                 |')
        print(f'| Diagnosa                   : {Diagnosa[K]:15}          |')
        print('+-------------------------------------------------------+')
    else:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def CariNama(Nama):
    DataCari = str(input('Nama yang dicari? ')).upper()
    i = 0

    while(Nama[i].upper() != DataCari) and (i < MAKSDATA):
        i = i + 1

    if(Nama[i].upper() == DataCari):
        print('+-------------------------------------------------------+')
        print(f'|                 DATA PASIEN-{i+1:<2}                        |')
        print('+-------------------------------------------------------+')
        print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
        print(f'| Nama                       : {Nama[i]:15}          |')
        print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
        print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
        print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
        print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
        print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
        print('+-------------------------------------------------------+')
    else:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def CariJenisKelamin(JenisKelamin):
    DataCari = str(input('Jenis Kelamin yang dicari? ')).upper()
    Ketemu = False

    for i in range(BanyakData):
        if(JenisKelamin[i].upper() == DataCari):
            print('+-------------------------------------------------------+')
            print(f'|                 DATA PASIEN-{i+1:<2}                        |')
            print('+-------------------------------------------------------+')
            print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
            print(f'| Nama                       : {Nama[i]:15}          |')
            print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
            print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
            print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
            print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
            print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
            print('+-------------------------------------------------------+')
    
    if not Ketemu:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def CariTanggalPeriksa(TanggalPeriksa):
    DataCari = str(input('Tanggal Periksa yang dicari? ')).upper()
    Ketemu = False

    for i in range(BanyakData):
        if(TanggalPeriksa[i].upper() == DataCari):
            print('+-------------------------------------------------------+')
            print(f'|                 DATA PASIEN-{i+1:<2}                        |')
            print('+-------------------------------------------------------+')
            print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
            print(f'| Nama                       : {Nama[i]:15}          |')
            print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
            print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
            print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
            print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
            print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
            print('+-------------------------------------------------------+')
    
    if not Ketemu:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def CariTinggiBadan(TinggiBadan):
    DataCari = str(input('Tinggi Badan yang dicari? ')).upper()
    Ketemu = False

    for i in range(BanyakData):
        if(TinggiBadan[i].upper() == DataCari):
            print('+-------------------------------------------------------+')
            print(f'|                 DATA PASIEN-{i+1:<2}                        |')
            print('+-------------------------------------------------------+')
            print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
            print(f'| Nama                       : {Nama[i]:15}          |')
            print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
            print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
            print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
            print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
            print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
            print('+-------------------------------------------------------+')
    
    if not Ketemu:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def CariBeratBadan(BeratBadan):
    DataCari = str(input('Berat Badan yang dicari? ')).upper()
    Ketemu = False

    for i in range(BanyakData):
        if(BeratBadan[i].upper() == DataCari):
            print('+-------------------------------------------------------+')
            print(f'|                 DATA PASIEN-{i+1:<2}                        |')
            print('+-------------------------------------------------------+')
            print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
            print(f'| Nama                       : {Nama[i]:15}          |')
            print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
            print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
            print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
            print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
            print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
            print('+-------------------------------------------------------+')
    
    if not Ketemu:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def CariDiagnosa(Diagnosa):
    DataCari = str(input('Diagnosa yang dicari? ')).upper()
    Ketemu = False

    for i in range(BanyakData):
        if(Diagnosa[i].upper() == DataCari):
            print('+-------------------------------------------------------+')
            print(f'|                 DATA PASIEN-{i+1:<2}                        |')
            print('+-------------------------------------------------------+')
            print(f'| No. Rekam Medis            : {NoRM[i]:8}                 |')
            print(f'| Nama                       : {Nama[i]:15}          |')
            print(f'| Jenis Kelamin              : {JenisKelamin[i]:2}                       |')
            print(f'| Tanggal Periksa [DD/MM/YY] : {TanggalPeriksa[i]:10}               |')
            print(f'| Berat Badan                : {BeratBadan[i]:<5} kg                 |')
            print(f'| Tinggi Badan               : {TinggiBadan[i]:<5} cm                 |')
            print(f'| Diagnosa                   : {Diagnosa[i]:15}          |')
            print('+-------------------------------------------------------+')
    
    if not Ketemu:
        print(f'{DataCari} tidak ditemukan')

    print()
    input()

def PenghapusanData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    print(f'+==============================+')
    print(f'|         REKAP MEDIS          |')

    for i in range(BanyakData):
        print(f'+------------------------------+')
        print(f'| {i+1:<2} | {NoRM[i]:<5} | {Nama[i]:<15} |')
    print(f'+==============================+')
    
    PosisiHapus = int(input('Posisi Hapus?'))
    PosisiHapus -= 1

    if BanyakData > 0:
        if (PosisiHapus >= 0) and (PosisiHapus < BanyakData):
            # Geser elemen setelah posisi hapus ke kiri
            for i in range(PosisiHapus + 1, BanyakData):
                NoRM[i-1] = NoRM[i]
                Nama[i-1] = Nama[i]
                JenisKelamin[i-1] = JenisKelamin[i]
                TanggalPeriksa[i-1] = TanggalPeriksa[i]
                BeratBadan[i-1] = BeratBadan[i]
                TinggiBadan[i-1] = TinggiBadan[i]
                Diagnosa[i-1] = Diagnosa[i]
            
            # Kurangi jumlah data
            BanyakData -= 1
            print('Data berhasil dihapus.')
        else:
            print('Posisi hapus tidak valid.')
    else:
        print('Data Kosong')

    input()
    return BanyakData
    
def RekapRekamMedis(JenisKelamin, BeratBadan, TinggiBadan, BanyakData):
    TotalBerat = TotalTinggi = JumlahLaki = JumlahPerempuan= 0
    if(BanyakData == 0):
        print('Belum ada data')
    else:
        if (BanyakData > 0):
            MaxBerat = BeratBadan[1]
            MinBerat = BeratBadan[1]
            MaxTinggi = BeratBadan[1]
            MinTinggi = BeratBadan[1]

        for i in range(BanyakData):
            if(JenisKelamin[i] == 'L'):
                JumlahLaki += 1
            if(JenisKelamin[i] == 'P'):
                JumlahPerempuan += 1
        
            TotalBerat += BeratBadan[i]
            TotalTinggi += TinggiBadan[i]

            if(BeratBadan[i] > MaxBerat):
                MaxBerat = BeratBadan[i]
            if(BeratBadan[i] < MinBerat):
                MinBerat = BeratBadan[i]
            
            if(TinggiBadan[i] > MaxTinggi):
                MaxTinggi = TinggiBadan[i]
            if(TinggiBadan[i] < MinTinggi):
                MinTinggi = TinggiBadan[i]


            RataBerat = TotalBerat / BanyakData
            RataTinggi = TotalTinggi / BanyakData

        os.system('clear')
        print(f'+--------------------------------------------+')
        print(f'|                  REKAP DATA                |')
        print(f'+-------------------------+------------------+')
        print(f'| Total Pasein            | {BanyakData:8}         |')
        print(f'+-------------------------+------------------+')
        print(f'| Jumlah Pasien Laki      | {JumlahLaki:8}         |')
        print(f'| Jumlah Pasien Perempuan | {JumlahPerempuan:8}         |')
        print(f'+-------------------------+------------------+')
        print(f'| Rata-rata Berat Badan   | {RataBerat:8.2f} kg      |')
        print(f'| Rata-rata Tinggi Badan  | {RataTinggi:8.2f} cm      |')
        print(f'+-------------------------+------------------+')
        print(f'| Berat Maksimum          | {MaxBerat:8} kg      |')
        print(f'| Berat Minimum           | {MinBerat:8} kg      |')
        print(f'| Tinggi Maksimum         | {MaxTinggi:8} cm      |')
        print(f'| Tinggi Minimum          | {MinTinggi:8} cm      |')
        print(f'+-------------------------+------------------+')
        print()
        input()








# Algoritma Utama    
os.system('clear')
Pilihan = PilihanPasien = PilihanDokter = BanyakData= PilihanPengurutan=PilihanAsc=PilihanDsc=PilihanPencarian = 0
BanyakData = Test(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)

Pilihan = MenuPilihan(Pilihan)
while(Pilihan != 0):
    match(Pilihan):
        case 1: 
            os.system('clear')
            PilihanPasien = MenuPasien(PilihanPasien)  
            while(PilihanPasien != 0):
                match(PilihanPasien):
                    case 1:
                        os.system('clear')
                        UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                        CariNoRM(NoRM, BanyakData)
                os.system('clear')
                PilihanPasien = MenuPasien(PilihanPasien)
               
        case 2: 
            os.system('clear')
            PilihanDokter = MenuDokter(PilihanDokter)  
            while(PilihanDokter != 0):
                match(PilihanDokter):
                    case 1: 
                        os.system('clear')
                        BanyakData = IsiData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
            
                    case 2: 
                        os.system('clear')
                        TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                        input()
            
                    case 3: 
                        os.system('clear')
                        EditData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
            
                    case 4:  
                        os.system('clear')
                        print('<< Pengurutan DATA >>')
                        PilihanPengurutan = MenuPengurutan(PilihanPengurutan)
                        while(PilihanPengurutan != 0):
                            match (PilihanPengurutan):
                                case 1:
                                    os.system('clear')
                                    PilihanAsc = MenuSortingAsc(PilihanAsc)
                                    while(PilihanAsc != 0):
                                        match(PilihanAsc):
                                            case 1:
                                                UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 2:
                                                UrutNamaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 3:
                                                UrutTanggalPeriksaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 4:
                                                UrutBeratBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 5:
                                                UrutTinggiBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 6:
                                                print('<< MENGURUTKAN Diagnosa SECARA ASC >>')
                                        input()
                                        os.system('clear')
                                        PilihanAsc = MenuSortingAsc(PilihanAsc)
                                case 2:
                                    os.system('clear')
                                    PilihanDsc = MenuSortingDsc(PilihanDsc)
                                    while(PilihanDsc != 0):
                                        match(PilihanDsc):
                                            case 1:
                                                UrutNoRMDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 2:
                                                UrutNamaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 3:
                                                UrutTanggalPeriksaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 4:
                                                UrutBeratBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 5:
                                                UrutTinggiBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                                TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)        
                                            case 6:
                                                print('<< MENGURUTKAN Diagnosa SECARA ASC >>')
                                        input()
                                        os.system('clear')
                                        PilihanDsc = MenuSortingDsc(PilihanDsc)
                            os.system('clear')
                            PilihanPengurutan = MenuPengurutan(PilihanPengurutan)
                    case 5: 
                        os.system('clear')
                        PilihanPencarian = MenuPencarian(PilihanPencarian)
                        while(PilihanPencarian != 0):
                            match(PilihanPencarian):
                                case 1:
                                    UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
                                    CariNoRM(NoRM, BanyakData)
                                case 2:
                                    CariNama(Nama)            
                                case 3:
                                    CariJenisKelamin(JenisKelamin)            
                                case 4:
                                    CariTanggalPeriksa(TanggalPeriksa);            
                                case 5:
                                    CariBeratBadan(BeratBadan);            
                                case 6:
                                    CariTinggiBadan(TinggiBadan);            
                                case 7:
                                    CariDiagnosa(Diagnosa);    
                            os.system('clear')
                            PilihanPencarian = MenuPencarian(PilihanPencarian)
                                    
                    case 6: 
                        os.system('clear')
                        BanyakData = PenghapusanData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData)
            
                    case 7: 
                        os.system('clear')
                        BanyakData = PenghancuranArray(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa)
            
                    case 8: 
                        os.system('clear')
                        RekapRekamMedis(JenisKelamin, BeratBadan, TinggiBadan, BanyakData)
            
                os.system('clear')
                PilihanDokter = MenuDokter(PilihanDokter)
    os.system('clear')
    Pilihan = MenuPilihan(Pilihan)

os.system('clear')
print('Terima Kasih')
