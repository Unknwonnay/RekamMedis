import os
from time import process_time_ns
from traceback import print_tb

MAKSDATA = 10

NoRM            = [0] * MAKSDATA
Nama            = [0] * MAKSDATA
JenisKelamin    = [0] * MAKSDATA
TanggalPeriksa  = [0] * MAKSDATA
BeratBadan      = [0] * MAKSDATA
TinggiBadan     = [0] * MAKSDATA
Diagnosa        = [0] * MAKSDATA

def Test(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    NoRM[0]         = 'A-01'
    Nama[0]         = 'Aido'
    JenisKelamin[0] = 'P'
    TanggalPeriksa[0] = '01-01-2024'
    BeratBadan[0]   = 50
    TinggiBadan[0]  = 160
    Diagnosa[0]     = 'Demam'
    BanyakData = 1
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
        Nama[i]           = input('Nama                       : ')
        JenisKelamin[i]   = input('Jenis Kelamin              : ')
        TanggalPeriksa[i] = input('Tanggal Periksa            : ')
        BeratBadan[i]     = int(input('Berat Badan                : '))
        TinggiBadan[i]    = int(input('Tinggi Badan               : '))
        Diagnosa[i]       = input('Diagnosa                   : ')
        i = i + 1

        if i < MAKSDATA:
            print('----------------------DATA KE-', i+1, '--------------')
            NoRM[i] = input('No.Rekam Medis             : ')
        else:
            print('Array Penuh!')
            Status = False

    BanyakData = i

    return BanyakData

def EditData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    if(BanyakData == 0):
        print('Belum ada data!')
    else:
        print('+---------------------------------------------+')
        print('| No. Rekam Medis |           Nama            |')

        for i in range(BanyakData):
            print('+---------------------------------------------+')
            print(f'| {NoRM[i]:15} | {Nama[i]:25} |')
        print('+---------------------------------------------+')

        NoEdit = str(input('Data yang mau di edit(No.RM)? '))

        for i in range(BanyakData):
            if NoEdit == NoRM[i]:
                Status = True
                index = i
            else:
                Status = False
        
        if(Status):
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
                    Nama[index] = input('Nama Baru : ')
                case 2:
                    os.system('clear')
                    JenisKelamin[index] = input('Jenis Kelamin Baru : ')
                case 3:
                    os.system('clear')
                    TanggalPeriksa[index] = input('Tanggal Periksa Baru : ')
                case 4:
                    os.system('clear')
                    BeratBadan[index] = int(input('Berat Badan Baru : '))
                case 5:
                    os.system('clear')
                    TinggiBadan[index] = int(input('Tinggi Badan Baru : '))
                case 6:
                    os.system('clear')
                    Diagnosa[index] = input('Diagnosa Baru : ')


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
        for j in range(BanyakData, i, -1):
            if NoRM[j] < NoRM[j-1]:
                TempStr = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = TempStr
                
                TempStr = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = TempStr

                TempStr = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = TempStr

                TempStr = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = TempStr

                TempInt = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = TempInt

                TempInt = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = TempInt

                TempStr = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = TempStr

def UrutNamaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData, i, -1):
            if Nama[j] < Nama[j-1]:
                TempStr = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = TempStr
                
                TempStr = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = TempStr

                TempStr = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = TempStr

                TempStr = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = TempStr

                TempInt = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = TempInt

                TempInt = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = TempInt

                TempStr = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = TempStr

def UrutTanggalPeriksaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData, i, -1):
            if TanggalPeriksa[j] < TanggalPeriksa[j-1]:
                TempStr = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = TempStr
                
                TempStr = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = TempStr

                TempStr = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = TempStr

                TempStr = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = TempStr

                TempInt = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = TempInt

                TempInt = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = TempInt

                TempStr = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = TempStr

#Minimum Sort Asc
def UrutBeratBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        min = i
        for j in range(i+1, BanyakData):
            if BeratBadan[j] < BeratBadan[min]:
                min = j

        TempStr = Nama[min]
        Nama[min] = Nama[i]
        Nama[i] = TempStr

        TempStr = NoRM[min]
        NoRM[min] = NoRM[i]
        NoRM[i] = TempStr
        
        TempStr = JenisKelamin[min]
        JenisKelamin[min] = JenisKelamin[i]
        JenisKelamin[i] = TempStr

        TempStr = TanggalPeriksa[min]
        TanggalPeriksa[min] = TanggalPeriksa[i]
        TanggalPeriksa[i] = TempStr

        TempInt = BeratBadan[min]
        BeratBadan[min] = BeratBadan[i]
        BeratBadan[i] = TempInt

        TempInt = TinggiBadan[min]
        TinggiBadan[min] = TinggiBadan[i]
        TinggiBadan[i] = TempInt

        TempStr = Diagnosa[min]
        Diagnosa[min] = Diagnosa[i]
        Diagnosa[i] = TempStr

#Maximum Sort Asc
def UrutTinggiBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        max = i
        for j in range(1, (BanyakData+1)-i):
            if TinggiBadan[j] > TinggiBadan[max]:
                max = j

        TempStr = Nama[max]
        Nama[max] = Nama[i]
        Nama[i] = TempStr

        TempStr = NoRM[max]
        NoRM[max] = NoRM[i]
        NoRM[i] = TempStr
        
        TempStr = JenisKelamin[max]
        JenisKelamin[max] = JenisKelamin[i]
        JenisKelamin[i] = TempStr

        TempStr = TanggalPeriksa[max]
        TanggalPeriksa[max] = TanggalPeriksa[i]
        TanggalPeriksa[i] = TempStr

        TempInt = BeratBadan[max]
        BeratBadan[max] = BeratBadan[i]
        BeratBadan[i] = TempInt

        TempInt = TinggiBadan[max]
        TinggiBadan[max] = TinggiBadan[i]
        TinggiBadan[i] = TempInt

        TempStr = Diagnosa[max]
        Diagnosa[max] = Diagnosa[i]
        Diagnosa[i] = TempStr

#PENGURUTAN DESCENDING
def UrutNoRMDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData-1, i, -1):
            if(NoRM[j] > NoRM[j-1]):
                TempStr = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = TempStr
                
                TempStr = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = TempStr

                TempStr = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = TempStr

                TempStr = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = TempStr

                TempInt = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = TempInt

                TempInt = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = TempInt

                TempStr = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = TempStr

def UrutNamaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData-1, i, -1):
            if(Nama[j] > Nama[j-1]):
                TempStr = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = TempStr

                TempStr = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = TempStr
                
                TempStr = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = TempStr

                TempStr = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = TempStr

                TempInt = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = TempInt

                TempInt = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = TempInt

                TempStr = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = TempStr

def  UrutTanggalPeriksaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        for j in range(BanyakData-1, i, -1):
            if(TanggalPeriksa[j] > TanggalPeriksa[j-1]):
                TempStr = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = TempStr

                TempStr = NoRM[j]
                NoRM[j] = NoRM[j-1]
                NoRM[j-1] = TempStr
                
                TempStr = JenisKelamin[j]
                JenisKelamin[j] = JenisKelamin[j-1]
                JenisKelamin[j-1] = TempStr

                TempStr = TanggalPeriksa[j]
                TanggalPeriksa[j] = TanggalPeriksa[j-1]
                TanggalPeriksa[j-1] = TempStr

                TempInt = BeratBadan[j]
                BeratBadan[j] = BeratBadan[j-1]
                BeratBadan[j-1] = TempInt

                TempInt = TinggiBadan[j]
                TinggiBadan[j] = TinggiBadan[j-1]
                TinggiBadan[j-1] = TempInt

                TempStr = Diagnosa[j]
                Diagnosa[j] = Diagnosa[j-1]
                Diagnosa[j-1] = TempStr


#Maximum Sort Desc
def UrutBeratBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        max = i
        for j in range(BanyakData-1, i, -1):
            if(BeratBadan[j] > BeratBadan[max]):
                max = j
        if (max != i) :
            TempStr = Nama[i]
            Nama[i] = Nama[max]
            Nama[max] = TempStr

            TempStr = NoRM[i]
            NoRM[i] = NoRM[max]
            NoRM[max] = TempStr
                
            TempStr = JenisKelamin[i]
            JenisKelamin[i] = JenisKelamin[max]
            JenisKelamin[max] = TempStr

            TempStr = TanggalPeriksa[i]
            TanggalPeriksa[i] = TanggalPeriksa[max]
            TanggalPeriksa[max] = TempStr

            TempInt = BeratBadan[i]
            BeratBadan[i] = BeratBadan[max]
            BeratBadan[max] = TempInt

            TempInt = TinggiBadan[i]
            TinggiBadan[i] = TinggiBadan[max]
            TinggiBadan[max] = TempInt

            TempStr = Diagnosa[i]
            Diagnosa[i] = Diagnosa[max]
            Diagnosa[max] = TempStr


#Minimum Sort Desc
def  UrutTinggiBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData):
    for i in range(BanyakData-1):
        max = 1
        for j in range(2, (BanyakData+1) - i):
            if(TinggiBadan[j] < TinggiBadan[max]):
                max = j

        TempStr = Nama[max]
        Nama[max] = Nama[j]
        Nama[j] = TempStr

        TempStr = NoRM[max]
        NoRM[max] = NoRM[j]
        NoRM[j] = TempStr

        TempStr = JenisKelamin[max]
        JenisKelamin[max] = JenisKelamin[j]
        JenisKelamin[j] = TempStr

        TempStr = TanggalPeriksa[max]
        TanggalPeriksa[max] = TanggalPeriksa[j]
        TanggalPeriksa[j] = TempStr

        TempInt = BeratBadan[max]
        BeratBadan[max] = BeratBadan[j]
        BeratBadan[j] = TempInt

        TempInt = TinggiBadan[max]
        TinggiBadan[max] = TinggiBadan[j]
        TinggiBadan[j] = TempInt

        TempStr = Diagnosa[max]
        Diagnosa[max] = Diagnosa[j]
        Diagnosa[j] = TempStr

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
                        print('<< MENCARI DATA >>')
                input()
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
                                                print('<< MENGURUTKAN No. Rekam Medis SECARA ASC >>')
        
                                            case 2:
                                                print('<< MENGURUTKAN NAMA SECARA ASC >>')
        
                                            case 3:
                                                print('<< MENGURUTKAN Tanggal Periksa SECARA ASC >>')
        
                                            case 4:
                                                print('<< MENGURUTKAN Berat Badan SECARA ASC >>')
        
                                            case 5:
                                                print('<< MENGURUTKAN Tinggi Badan SECARA ASC >>')
        
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
                                                print('<< MENGURUTKAN No. Rekam Medis SECARA DESC >>')
                                            case 2:
                                                print('<< MENGURUTKAN NAMA SECARA DESC >>')
                                            case 3:
                                                print('<< MENGURUTKAN Tanggal Periksa SECARA DESC >>')
                                            case 4:
                                                print('<< MENGURUTKAN Berat Badan SECARA DESC >>')
                                            case 5:
                                                print('<< MENGURUTKAN Tinggi Badan SECARA DESC >>')
                                            case 6:
                                                print('<< MENGURUTKAN Diagnosa SECARA DESC >>')
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
                                    print('Cari NO. Rekam Medis')            
                                case 2:
                                    print('Cari Nama')            
                                case 3:
                                    print('Cari Jenis Kelamin')            
                                case 4:
                                    print('Cari Tanggal Periksa')            
                                case 5:
                                    print('Cari Berat Badan')            
                                case 6:
                                    print('Cari Tinggi Badan')            
                                case 7:
                                    print('Cari Diagnosa')    
                            os.system('clear')
                            PilihanPencarian = MenuPencarian(PilihanPencarian)
                                    
                    case 6: 
                        os.system('clear')
                        print('<< Penghapusan DATA >>')
            
                    case 7: 
                        os.system('clear')
                        print('<< Penghancuran DATA >>')
            
                    case 8: 
                        os.system('clear')
                        print('<< Rekap Rekam Medis >>')
            
                input()
                os.system('clear')
                PilihanDokter = MenuDokter(PilihanDokter)
    os.system('clear')
    Pilihan = MenuPilihan(Pilihan)

os.system('clear')
print('Terima Kasih')
