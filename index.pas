program RekamMedis;
uses crt,SysUtils;


const
    MAKSDATA = 10;

type
    ArrayNoRM     = array[1..MAKSDATA] of string;
    ArrayNama     = array[1..MAKSDATA] of string;
    ArrayKelamin  = array[1..MAKSDATA] of string;
    ArrayTanggal  = array[1..MAKSDATA] of string;
    ArrayBerat    = array[1..MAKSDATA] of integer;
    ArrayTinggi   = array[1..MAKSDATA] of integer;
    ArrayDiagnosa = array[1..MAKSDATA] of string;


var
    NoRM : ArrayNoRM;
    Nama : ArrayNama;
    JenisKelamin : ArrayKelamin;
    TanggalPeriksa : ArrayTanggal;
    BeratBadan : ArrayBerat;
    TinggiBadan : ArrayTinggi;
    Diagnosa : ArrayDiagnosa;

    Pilihan,PilihanDokter,PilihanPasien, PilihanAsc,
    PilihanDsc,PilihanPengurutan,PilihanPencarian ,MetodeCariPasein,BanyakData : integer;

//Testing Array
procedure ArrayTest(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
                            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
                            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa );
begin
    //array 1
    (* NoRM[1]             := '1';
    Nama[1]             := 'Budi';
    JenisKelamin[1]     := 'L';
    TanggalPeriksa[1]   := '120225';
    BeratBadan[1]       := 76;
    TinggiBadan[1]      := 170;
    Diagnosa[1]         := 'Demam';

    //array 2
    NoRM[2]             := '2';
    Nama[2]             := 'Yanto';
    JenisKelamin[2]     := 'L';
    TanggalPeriksa[2]   := '120225';
    BeratBadan[2]       := 60;
    TinggiBadan[2]      := 150;
    Diagnosa[2]         := 'Demam';

    //array 3
    NoRM[3]             := '3';
    Nama[3]             := 'Gusti';
    JenisKelamin[3]     := 'L';
    TanggalPeriksa[3]   := '120225';
    BeratBadan[3]       := 80;
    TinggiBadan[3]      := 160;
    Diagnosa[3]         := 'Diare';

    BanyakData := 3; *)
end;

procedure PenghancuranArray(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
                            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
                            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa );
var
    i : integer;
begin
    for i := 1 to MAKSDATA do
    begin
        NoRm[i]           := '/';
        Nama[i]           := '/';
        JenisKelamin[i]   := '/';
        TanggalPeriksa[i] := '/';
        BeratBadan[i]     := 0;
        TinggiBadan[i]    := 0;
        Diagnosa[i]       := '/';
    end;
end;

procedure TampilData(NoRM : ArrayNoRM; Nama : ArrayNama; JenisKelamin : ArrayKelamin; 
                        TanggalPeriksa : ArrayTanggal; BeratBadan : ArrayBerat; 
                        TinggiBadan : ArrayTinggi; Diagnosa : ArrayDiagnosa; BanyakData : integer );
var
    i : integer;
begin
    if BanyakData = 0 then
    begin
        write('Belum ada data!');
    end
    else
    begin
        for i := 1 to BanyakData do
        begin
            writeln('+-------------------------------------------------------+');
            writeln('|                 DATA PASEIN-',i,'                         |');
            writeln('+-------------------------------------------------------+');
            writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
            writeln('| Nama                       : ', Nama[i]:15, '          |');
            writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
            writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
            writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
            writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
            writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
            writeln('+-------------------------------------------------------+');
        end;
    end;
end;

procedure MenuPilihan(var Pilihan : integer);
begin
   writeln ('+=====================+');
   writeln ('|     REKAM MEDIS     |');
   writeln ('+=====================+');
   writeln ('|      1. Pasien      |');
   writeln ('|      2. Dokter      |');
   writeln ('|      0. Keluar      |');
   writeln ('+=====================+');


    write('Pilihan ? ');readln(Pilihan);
    while(Pilihan  < 0) or (Pilihan  > 2) do
    begin
        writeln('Pilih yang ada di menu!');
        readln;
        clrscr;
        writeln ('+=====================+');
        writeln ('|     REKAM MEDIS     |');
        writeln ('+=====================+');
        writeln ('|      1. Pasien      |');
        writeln ('|      2. Dokter      |');
        writeln ('|      0. Keluar      |');
        writeln ('+=====================+');
        write('Pilihan ? ');readln(Pilihan);
    end;
end;

procedure MenuPasien(var PilihanPasien : integer);
begin
    writeln ('+================================+');
    writeln ('|          MENU PASIEN           |');
    writeln ('+================================+');
    writeln ('|         1. Cari Data           |');
    writeln ('|         0. Keluar              |');
    writeln ('+================================+');


    write('Pilihan ? ');readln(PilihanPasien);
    while(PilihanPasien  < 0) or (PilihanPasien  > 1) do
    begin
        writeln('Pilih yang ada di menu!');
        readln;
        clrscr;
        writeln ('+================================+');
        writeln ('|          MENU PASIEN           |');
        writeln ('+================================+');
        writeln ('|         1. Cari Data           |');
        writeln ('|         0. Keluar              |');
        writeln ('+================================+');
        write('Pilihan ? ');readln(PilihanPasien);
    end;
end;


procedure MenuDokter(var PilihanDokter : integer);
begin
    writeln ('+=====================================+');
    writeln ('|            MENU DOKTER              |');
    writeln ('+=====================================+');
    writeln ('|          1. Isi Data                |');
    writeln ('|          2. Tampilkan Data          |');
    writeln ('|          3. Edit Data               |');
    writeln ('|          4. Pengurutan Data         |');
    writeln ('|          5. Pencarian Data          |');
    writeln ('|          6. Penghapusan Data        |');
    writeln ('|          7. Penghancuran Data       |');
    writeln ('|          8. Rekap Rekam Medis       |');
    writeln ('|          0. Keluar                  |');
    writeln ('+=====================================+');


    write('Pilihan ? ');readln(PilihanDokter);
    while(PilihanDokter  < 0) or (PilihanDokter  > 8) do
    begin
        writeln('Pilih yang ada di menu!');
        readln;
        clrscr;
        writeln ('+=====================================+');
        writeln ('|            MENU DOKTER              |');
        writeln ('+=====================================+');
        writeln ('|          1. Isi Data                |');
        writeln ('|          2. Tampilkan Data          |');
        writeln ('|          3. Edit Data               |');
        writeln ('|          4. Pengurutan Data         |');
        writeln ('|          5. Pencarian Data          |');
        writeln ('|          6. Penghapusan Data        |');
        writeln ('|          7. Penghancuran Data       |');
        writeln ('|          8. Rekap Rekam Medis       |');
        writeln ('|          0. Keluar                  |');
        writeln ('+=====================================+');
        write('Pilihan ? ');readln(PilihanDokter);
    end;
end;


procedure IsiData(var NoRM: ArrayNoRM; var Nama: ArrayNama; var JenisKelamin: ArrayKelamin; 
                  var TanggalPeriksa: ArrayTanggal; var BeratBadan: ArrayBerat; 
                  var TinggiBadan: ArrayTinggi; var Diagnosa: ArrayDiagnosa; var BanyakData: integer);
var
    i: integer;
begin
    i := BanyakData + 1;

    while (i <= 10) and (NoRM[i] <> 'STOP') do
    begin
        writeln('----------------------DATA KE-', i, '--------------');
        write('No.Rekam Medis             : '); readln(NoRM[i]);
        NoRM[i] := UpperCase(NoRM[i]);

        if NoRM[i] = 'STOP' then
            break;

        write('Nama                       : '); readln(Nama[i]);
        Nama[i] := UpperCase(Nama[i]);
        write('Jenis Kelamin [L/P]        : '); readln(JenisKelamin[i]);
        JenisKelamin[i] := UpperCase(JenisKelamin[i]);
        write('Tanggal Periksa [DD/MM/YY] : '); readln(TanggalPeriksa[i]);
        write('Berat Badan (kg)           : '); readln(BeratBadan[i]);
        write('Tinggi Badan (cm)          : '); readln(TinggiBadan[i]);
        write('Diagnosa                   : '); readln(Diagnosa[i]);

        i := i + 1;
    end;

    if i > 10 then
    begin
        writeln('Data sudah mencapai batas maksimum (10 entri).');
    end;

    BanyakData := i - 1; // Update jumlah data yang berhasil dimasukkan
end;

procedure EditData(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
                    var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
                    var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; BanyakData : integer);
var 
 i, NoEdit, PilihanEdit: integer;
begin
    if(BanyakData = 0) then
    begin
        writeln('Belum Ada Data!');
    end
    else
    begin
        writeln('+---------------------------------------------+');
        writeln('| No. Rekam Medis |           Nama            |');

        for i := 1 to BanyakData do
        begin
            writeln('+---------------------------------------------+');
            writeln('| ',NoRM[i]:15 ,' | ', Nama[i]:25 ,' |');
        end;

        write('Data yang mau di edit(No.RM)?');readln(NoEdit);

        while(NoEdit < 0 ) or (NoEdit > BanyakData ) do
        begin
            writeln('Data tidak ada!');
            readln;
            clrscr;

            writeln('+---------------------------------------------+');
            writeln('| No. Rekam Medis |           Nama            |');

            for i := 1 to BanyakData do
            begin
                writeln('+---------------------------------------------+');
                writeln('| ',NoRM[i]:15 ,' | ', Nama[i]:25 ,' |');
            end;

            write('Data yang mau di edit(No.RM)?');readln(NoEdit);
        end;

        clrscr;
        writeln ('+=====================================+');
        writeln ('|        PILIH YANG MAU DI EDIT       |');
        writeln ('+=====================================+');
        writeln ('|           1. Nama                   |');
        writeln ('|           2. Jenis Kelamin          |');
        writeln ('|           3. Tanggaal Periksa       |');
        writeln ('|           4. Berat Badan            |');
        writeln ('|           5. Tinggi Badan           |');
        writeln ('|           6. Diagnosa               |');
        writeln ('|           0. Keluar                 |');
        writeln ('+=====================================+');
        write('Pilihan?');readln(PilihanEdit);

        case(PilihanEdit) of
            1 : begin
                clrscr;
                writeln('Edit Nama');
                write('Nama : ');readln(Nama[NoEdit]);
                writeln('Data berhasil diperbarui!');
            end;
            2 : begin
                clrscr;
                writeln('Edit Jenis Kelamin');
                write('Jenis Kelamin : ');readln(JenisKelamin[NoEdit]);
                writeln('Data berhasil diperbarui!');
                
            end;
            3 : begin
                clrscr;
                writeln('Edit Tanggal Periksa');
                write('Tanggal Periksa : ');readln(TanggalPeriksa[NoEdit]);
                writeln('Data berhasil diperbarui!');
                
            end;
            4 : begin
                clrscr;
                writeln('Edit Berat Badan');
                write('Berat Badan : ');readln(BeratBadan[NoEdit]);
                writeln('Data berhasil diperbarui!');
                
            end;
            5 : begin
                clrscr;
                writeln('Edit Tinggi Badan');
                write('Tinggi Badan : ');readln(TinggiBadan[NoEdit]);
                writeln('Data berhasil diperbarui!');

            end;
            6 : begin
                clrscr;
                writeln('Edit Diagnosa');
                write('Diagnosa : ');readln(Diagnosa[NoEdit]);
                writeln('Data berhasil diperbarui!');
            end;
        end;
    end;
end;

//Sorting Ascending Menggunakan Bubble Sort
procedure UrutNoRMAsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt : integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        for j := N downto i+1 do
        begin
            if(NoRM[j] < NoRM[j-1]) then
            begin
                TempStr := NoRM[j];
                NoRM[j] := NoRM[j-1];
                NoRM[j-1] := TempStr;
                
                TempStr := Nama[j];
                Nama[j] := Nama[j-1];
                Nama[j-1] := TempStr;

                TempStr := JenisKelamin[j];
                JenisKelamin[j] := JenisKelamin[j-1];
                JenisKelamin[j-1] := TempStr;

                TempStr := TanggalPeriksa[j];
                TanggalPeriksa[j] := TanggalPeriksa[j-1];
                TanggalPeriksa[j-1] := TempStr;

                TempInt := BeratBadan[j];
                BeratBadan[j] := BeratBadan[j-1];
                BeratBadan[j-1] := TempInt;

                TempInt := TinggiBadan[j];
                TinggiBadan[j] := TinggiBadan[j-1];
                TinggiBadan[j-1] := TempInt;

                TempStr := Diagnosa[j];
                Diagnosa[j] := Diagnosa[j-1];
                Diagnosa[j-1] := TempStr;

            end;
        end;
    end;
end;

procedure UrutNamaAsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt : integer;
    TempStr : string;

begin
    for i := 1 to N-1 do
    begin
        for j := N downto i+1 do
        begin
            if(Nama[j] < Nama[j-1]) then
            begin
                TempStr := Nama[j];
                Nama[j] := Nama[j-1];
                Nama[j-1] := TempStr;

                TempStr := NoRM[j];
                NoRM[j] := NoRM[j-1];
                NoRM[j-1] := TempStr;
                
                TempStr := JenisKelamin[j];
                JenisKelamin[j] := JenisKelamin[j-1];
                JenisKelamin[j-1] := TempStr;

                TempStr := TanggalPeriksa[j];
                TanggalPeriksa[j] := TanggalPeriksa[j-1];
                TanggalPeriksa[j-1] := TempStr;

                TempInt := BeratBadan[j];
                BeratBadan[j] := BeratBadan[j-1];
                BeratBadan[j-1] := TempInt;

                TempInt := TinggiBadan[j];
                TinggiBadan[j] := TinggiBadan[j-1];
                TinggiBadan[j-1] := TempInt;

                TempStr := Diagnosa[j];
                Diagnosa[j] := Diagnosa[j-1];
                Diagnosa[j-1] := TempStr;

            end;
        end;
    end;
end;

procedure UrutTanggalPeriksaAsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt : integer;
    TempStr : string;

begin
    for i := 1 to N-1 do
    begin
        for j := N downto i+1 do
        begin
            if(TanggalPeriksa[j] < TanggalPeriksa[j-1]) then
            begin
                TempStr := Nama[j];
                Nama[j] := Nama[j-1];
                Nama[j-1] := TempStr;

                TempStr := NoRM[j];
                NoRM[j] := NoRM[j-1];
                NoRM[j-1] := TempStr;
                
                TempStr := JenisKelamin[j];
                JenisKelamin[j] := JenisKelamin[j-1];
                JenisKelamin[j-1] := TempStr;

                TempStr := TanggalPeriksa[j];
                TanggalPeriksa[j] := TanggalPeriksa[j-1];
                TanggalPeriksa[j-1] := TempStr;

                TempInt := BeratBadan[j];
                BeratBadan[j] := BeratBadan[j-1];
                BeratBadan[j-1] := TempInt;

                TempInt := TinggiBadan[j];
                TinggiBadan[j] := TinggiBadan[j-1];
                TinggiBadan[j-1] := TempInt;

                TempStr := Diagnosa[j];
                Diagnosa[j] := Diagnosa[j-1];
                Diagnosa[j-1] := TempStr;

            end;
        end;
    end;
end;

//Minimum Sort Asc
procedure UrutBeratBadanAsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt, min: integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        min := i;
        for j := i + 1 to N do
        begin
            if(BeratBadan[j] < BeratBadan[min]) then
            begin
                min := j;
            end;
        end;
    TempStr := Nama[min];
    Nama[min] := Nama[i];
    Nama[i] := TempStr;

    TempStr := NoRM[min];
    NoRM[min] := NoRM[i];
    NoRM[i] := TempStr;
    
    TempStr := JenisKelamin[min];
    JenisKelamin[min] := JenisKelamin[i];
    JenisKelamin[i] := TempStr;

    TempStr := TanggalPeriksa[min];
    TanggalPeriksa[min] := TanggalPeriksa[i];
    TanggalPeriksa[i] := TempStr;

    TempInt := BeratBadan[min];
    BeratBadan[min] := BeratBadan[i];
    BeratBadan[i] := TempInt;

    TempInt := TinggiBadan[min];
    TinggiBadan[min] := TinggiBadan[i];
    TinggiBadan[i] := TempInt;

    TempStr := Diagnosa[min];
    Diagnosa[min] := Diagnosa[i];
    Diagnosa[i] := TempStr;
    end;
end;

//Maximum Sort Asc
procedure UrutTinggiBadanAsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt, max : integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        max := 1;
        for j := 2 to (N+1) - i do
        begin
            if(TinggiBadan[j] > TinggiBadan[max]) then
            begin
                max := j;
            end;
        end;
    TempStr := Nama[max];
    Nama[max] := Nama[j];
    Nama[j] := TempStr;

    TempStr := NoRM[max];
    NoRM[max] := NoRM[j];
    NoRM[j] := TempStr;
    
    TempStr := JenisKelamin[max];
    JenisKelamin[max] := JenisKelamin[j];
    JenisKelamin[j] := TempStr;

    TempStr := TanggalPeriksa[max];
    TanggalPeriksa[max] := TanggalPeriksa[j];
    TanggalPeriksa[j] := TempStr;

    TempInt := BeratBadan[max];
    BeratBadan[max] := BeratBadan[j];
    BeratBadan[j] := TempInt;

    TempInt := TinggiBadan[max];
    TinggiBadan[max] := TinggiBadan[j];
    TinggiBadan[j] := TempInt;

    TempStr := Diagnosa[max];
    Diagnosa[max] := Diagnosa[j];
    Diagnosa[j] := TempStr;
    end;
end;


//Sorting Descending Menggunakan Bubble Sort
procedure UrutNoRMDsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt : integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        for j := N downto i+1 do
        begin
            if(NoRM[j] > NoRM[j-1]) then
            begin
                TempStr := NoRM[j];
                NoRM[j] := NoRM[j-1];
                NoRM[j-1] := TempStr;
                
                TempStr := Nama[j];
                Nama[j] := Nama[j-1];
                Nama[j-1] := TempStr;

                TempStr := JenisKelamin[j];
                JenisKelamin[j] := JenisKelamin[j-1];
                JenisKelamin[j-1] := TempStr;

                TempStr := TanggalPeriksa[j];
                TanggalPeriksa[j] := TanggalPeriksa[j-1];
                TanggalPeriksa[j-1] := TempStr;

                TempInt := BeratBadan[j];
                BeratBadan[j] := BeratBadan[j-1];
                BeratBadan[j-1] := TempInt;

                TempInt := TinggiBadan[j];
                TinggiBadan[j] := TinggiBadan[j-1];
                TinggiBadan[j-1] := TempInt;

                TempStr := Diagnosa[j];
                Diagnosa[j] := Diagnosa[j-1];
                Diagnosa[j-1] := TempStr;

            end;
        end;
    end;
end;

procedure UrutNamaDsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt : integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        for j := N downto i+1 do
        begin
            if(Nama[j] > Nama[j-1]) then
            begin
                TempStr := Nama[j];
                Nama[j] := Nama[j-1];
                Nama[j-1] := TempStr;

                TempStr := NoRM[j];
                NoRM[j] := NoRM[j-1];
                NoRM[j-1] := TempStr;
                
                TempStr := JenisKelamin[j];
                JenisKelamin[j] := JenisKelamin[j-1];
                JenisKelamin[j-1] := TempStr;

                TempStr := TanggalPeriksa[j];
                TanggalPeriksa[j] := TanggalPeriksa[j-1];
                TanggalPeriksa[j-1] := TempStr;

                TempInt := BeratBadan[j];
                BeratBadan[j] := BeratBadan[j-1];
                BeratBadan[j-1] := TempInt;

                TempInt := TinggiBadan[j];
                TinggiBadan[j] := TinggiBadan[j-1];
                TinggiBadan[j-1] := TempInt;

                TempStr := Diagnosa[j];
                Diagnosa[j] := Diagnosa[j-1];
                Diagnosa[j-1] := TempStr;

            end;
        end;
    end;
end;

procedure UrutTanggalPeriksaDsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt : integer;
    TempStr : string;

begin
    for i := 1 to N-1 do
    begin
        for j := N downto i+1 do
        begin
            if(TanggalPeriksa[j] > TanggalPeriksa[j-1]) then
            begin
                TempStr := Nama[j];
                Nama[j] := Nama[j-1];
                Nama[j-1] := TempStr;

                TempStr := NoRM[j];
                NoRM[j] := NoRM[j-1];
                NoRM[j-1] := TempStr;
                
                TempStr := JenisKelamin[j];
                JenisKelamin[j] := JenisKelamin[j-1];
                JenisKelamin[j-1] := TempStr;

                TempStr := TanggalPeriksa[j];
                TanggalPeriksa[j] := TanggalPeriksa[j-1];
                TanggalPeriksa[j-1] := TempStr;

                TempInt := BeratBadan[j];
                BeratBadan[j] := BeratBadan[j-1];
                BeratBadan[j-1] := TempInt;

                TempInt := TinggiBadan[j];
                TinggiBadan[j] := TinggiBadan[j-1];
                TinggiBadan[j-1] := TempInt;

                TempStr := Diagnosa[j];
                Diagnosa[j] := Diagnosa[j-1];
                Diagnosa[j-1] := TempStr;

            end;
        end;
    end;
end;

//Maximum Sort Desc
procedure UrutBeratBadanDsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i, j, max, TempInt : integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        max := i;
        for j := i+1 to N do
        begin
            if (BeratBadan[j] > BeratBadan[max]) then
            begin
                max := j;
            end;
        end;

        // Swap data jika max berbeda dari i
        if (max <> i) then
        begin
            TempStr := Nama[i];
            Nama[i] := Nama[max];
            Nama[max] := TempStr;

            TempStr := NoRM[i];
            NoRM[i] := NoRM[max];
            NoRM[max] := TempStr;
                
            TempStr := JenisKelamin[i];
            JenisKelamin[i] := JenisKelamin[max];
            JenisKelamin[max] := TempStr;

            TempStr := TanggalPeriksa[i];
            TanggalPeriksa[i] := TanggalPeriksa[max];
            TanggalPeriksa[max] := TempStr;

            TempInt := BeratBadan[i];
            BeratBadan[i] := BeratBadan[max];
            BeratBadan[max] := TempInt;

            TempInt := TinggiBadan[i];
            TinggiBadan[i] := TinggiBadan[max];
            TinggiBadan[max] := TempInt;

            TempStr := Diagnosa[i];
            Diagnosa[i] := Diagnosa[max];
            Diagnosa[max] := TempStr;
        end;
    end;
end;

//Minimum Sort Desc
procedure UrutTinggiBadanDsc(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; N : integer);
var
    i,j,TempInt, max : integer;
    TempStr : string;
begin
    for i := 1 to N-1 do
    begin
        max := 1;
        for j := 2 to (N+1) - i do
        begin
            if(TinggiBadan[j] < TinggiBadan[max]) then
            begin
                max := j;
            end;
        end;
    TempStr := Nama[max];
    Nama[max] := Nama[j];
    Nama[j] := TempStr;

    TempStr := NoRM[max];
    NoRM[max] := NoRM[j];
    NoRM[j] := TempStr;
    
    TempStr := JenisKelamin[max];
    JenisKelamin[max] := JenisKelamin[j];
    JenisKelamin[j] := TempStr;

    TempStr := TanggalPeriksa[max];
    TanggalPeriksa[max] := TanggalPeriksa[j];
    TanggalPeriksa[j] := TempStr;

    TempInt := BeratBadan[max];
    BeratBadan[max] := BeratBadan[j];
    BeratBadan[j] := TempInt;

    TempInt := TinggiBadan[max];
    TinggiBadan[max] := TinggiBadan[j];
    TinggiBadan[j] := TempInt;

    TempStr := Diagnosa[max];
    Diagnosa[max] := Diagnosa[j];
    Diagnosa[j] := TempStr;
    end;
end;

procedure MenuPengurutan(var PilihanPengurutan : integer);
begin
    if(BanyakData = 0) then
    begin
        writeln('Belum ada data!')
    end
    else
    begin
        writeln ('+=====================================+');
        writeln ('|           MENU PENGURUTAN           |');
        writeln ('+=====================================+');
        writeln ('|            1. Ascending             |');
        writeln ('|            2. Descending            |');
        writeln ('|            0. Keluar                |');
        writeln ('+=====================================+');
        write('Pilihan? ');readln(PilihanPengurutan);
    end;
    
    
end;

procedure MenuSortingAsc(var PilihanAsc : integer);
begin
    writeln ('+===========================================+');
    writeln ('|       MENGURUTKAN DATA SECARA MENAIK      |');
    writeln ('+===========================================+');
    writeln ('|            1. No. Rekam Medis             |');
    writeln ('|            2. Nama                        |');
    writeln ('|            3. Tanggal Periksa             |');
    writeln ('|            4. Berat Badan                 |');
    writeln ('|            5. Tinggi Badan                |');
    writeln ('|            0. Keluar                      |');
    writeln ('+===========================================+');
    write('Pilihan? ');readln(PilihanAsc);
end;

procedure MenuSortingDsc(var PilihanDsc : integer);
begin
    writeln ('+============================================+');
    writeln ('|       MENGURUTKAN DATA SECARA MENURUN      |');
    writeln ('+============================================+');
    writeln ('|            1. No. Rekam Medis              |');
    writeln ('|            2. Nama                         |');
    writeln ('|            3. Tanggal Periksa              |');
    writeln ('|            4. Berat Badan                  |');
    writeln ('|            5. Tinggi Badan                 |');
    writeln ('|            0. Keluar                       |');
    writeln ('+============================================+');
    write('Pilihan? ');readln(PilihanDsc);
end;

procedure PenghapusanData(var NoRM : ArrayNoRM; var Nama : ArrayNama; var JenisKelamin : ArrayKelamin; 
            var TanggalPeriksa : ArrayTanggal; var BeratBadan : ArrayBerat; 
            var TinggiBadan : ArrayTinggi; var Diagnosa : ArrayDiagnosa; var BanyakData : integer);

var
    i, indeks, NoHapus  : integer;
    (* found: boolean;
    PosHapus : integer; *)
begin
    if (BanyakData = 0) then
    begin
        writeln('Data belum ada!');

    end
    else
    begin
        writeln('+---------------------------------------------+');
        writeln('| No. Rekam Medis |           Nama            |');

        for i := 1 to BanyakData do
        begin
            writeln('+---------------------------------------------+');
            writeln('| ', NoRM[i]:15, ' | ', Nama[i]:25, ' |');
        end;

        write('Data yang mau di hapus(No.RM)?'); readln(NoHapus);

        if (BanyakData > 0) then
        begin
            if (NoHapus >= 1) and (NoHapus <= BanyakData) then
            begin
                // Geser elemen array ke kiri mulai dari posisi hapus
                for indeks := (NoHapus + 1) to BanyakData do
                begin
                    NoRM[indeks - 1]           := NoRM[indeks];
                    Nama[indeks - 1]           := Nama[indeks];
                    JenisKelamin[indeks - 1]   := JenisKelamin[indeks];
                    TanggalPeriksa[indeks - 1] := TanggalPeriksa[indeks];
                    BeratBadan[indeks - 1]     := BeratBadan[indeks];
                    TinggiBadan[indeks - 1]    := TinggiBadan[indeks];
                    Diagnosa[indeks - 1]       := Diagnosa[indeks];
                end;
                // Set elemen terakhir ke 0 (opsional, tergantung kebutuhan)
                NoRM[BanyakData] := '/';
                Nama[BanyakData] := '/';
                JenisKelamin[BanyakData] := '/';
                TanggalPeriksa[BanyakData] := '/';
                BeratBadan[BanyakData] := 0;
                TinggiBadan[BanyakData] := 0;
                Diagnosa[BanyakData] := '/';
                
                // Kurangi jumlah data
                BanyakData := BanyakData - 1;
            end
            else
            begin
                writeln('Posisi hapus tidak valid');
            end;
        end
        else
        begin
            writeln('Data Kosong');
        end;
    end;
end;

procedure MenuPecarian(var PilihanPencarian : integer);
begin
    if(BanyakData = 0) then
    begin
        writeln('Belum ada data!');
    end
    else
    begin
        writeln ('+===========================================+');
        writeln ('|               MENU PENCARIAN              |');
        writeln ('+===========================================+');
        writeln ('|            1. Cari No. Rekam Medis        |');
        writeln ('|            2. Cari Nama                   |');
        writeln ('|            3. Cari Jenis Kelamin          |');
        writeln ('|            4. Cari Tanggal Periksa        |');
        writeln ('|            5. Cari Berat Badan            |');
        writeln ('|            6. Cari Tinggi Badan           |');
        writeln ('|            7. Cari Diagnosis              |');
        writeln ('|            0. Keluar                      |');
        writeln ('+===========================================+');
        write('Pilihan? ');readln(PilihanPencarian);
    end;
end;

procedure CariNoRM(NoRM: ArrayNoRM; BanyakData: Integer);
var
    Ia, Ib, K : Integer;
    DataCari : string;
    Ketemu: Boolean;
begin
    // Pastikan array NoRM sudah terurut
    UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);

    write('No. Rekam Medis yang dicari: '); readln(DataCari);

    Ia := 1; // Indeks awal
    Ib := BanyakData; // Indeks akhir
    Ketemu := False;

    while (not Ketemu) and (Ia <= Ib) do
    begin
        K := (Ia + Ib) div 2; // Hitung indeks tengah

        if (NoRM[K] = DataCari) then
        begin
            Ketemu := True; // Data ditemukan
        end
        else
        begin
            if (NoRM[K] < DataCari) then
            begin
                Ia := K + 1; // Cari di sebelah kanan
            end
            else
            begin
                Ib := K - 1; // Cari di sebelah kiri
            end;
        end;
    end;

    if (Ketemu) then
    begin
        writeln('+-------------------------------------------------------+');
        writeln('|                 DATA PASEIN-',K,'                         |');
        writeln('+-------------------------------------------------------+');
        writeln('| No. Rekam Medis            :      ', NoRM[K]:8, '            |');
        writeln('| Nama                       : ', Nama[K]:15, '          |');
        writeln('| Jenis Kelamin              :            ', JenisKelamin[K]:2,'            |');
        writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[K]:10, '           |');
        writeln('| Berat Badan                :         ', BeratBadan[K]:5, '            |');
        writeln('| Tinggi Badan               :         ', TinggiBadan[K]:5, '            |');
        writeln('| Diagnosa                   : ', Diagnosa[K]:15, '          |');
        writeln('+-------------------------------------------------------+');
    end
    else
    begin
        writeln(DataCari, ' tidak ditemukan');
    end;
end;

procedure CariNama(var Nama : ArrayNama);
var
    i : integer;
    DataCari : string;
begin
    write('Nama yang dicari : ');readln(DataCari);
    i := 1;

    while(UpperCase(Nama[i]) <> UpperCase(DataCari)) and (i < MAKSDATA) do
    begin
        i := i + 1;
    end;
    if(UpperCase(Nama[i]) = UpperCase(DataCari)) then
    begin
        writeln('+-------------------------------------------------------+');
        writeln('|                 DATA PASEIN-',i,'                         |');
        writeln('+-------------------------------------------------------+');
        writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
        writeln('| Nama                       : ', Nama[i]:15, '          |');
        writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
        writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
        writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
        writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
        writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
        writeln('+-------------------------------------------------------+');
    end
    else
    begin
        writeln(DataCari,'Tidak ditemukan');
        
    end;
end;

procedure CariJenisKelamin(var JenisKelamin : ArrayKelamin);
var
    i : integer;
    DataCari : string;
    Ditemukan : boolean; // Variabel untuk menandai apakah data ditemukan
begin
    write('Jenis Kelamin yang dicari : '); readln(DataCari);
    Ditemukan := false; // Awalnya asumsikan data tidak ditemukan

    for i := 1 to MAKSDATA do // Periksa semua data dalam array
    begin
        if JenisKelamin[i] = DataCari then
        begin
            Ditemukan := true; // Data ditemukan
            writeln('+-------------------------------------------------------+');
            writeln('|                 DATA PASEIN-',i,'                         |');
            writeln('+-------------------------------------------------------+');
            writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
            writeln('| Nama                       : ', Nama[i]:15, '          |');
            writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
            writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
            writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
            writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
            writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
            writeln('+-------------------------------------------------------+');
            writeln; // Beri jarak antar data
        end;
    end;

    if not Ditemukan then
    begin
        writeln(DataCari, ' Tidak ditemukan');
    end;
end;

procedure CariTanggalPeriksa(var TanggalPeriksa : ArrayTanggal);
var
    i : integer;
    DataCari : string;
    Ditemukan : boolean; // Variabel untuk menandai apakah data ditemukan
begin
    write('Tanggal Periksa yang dicari : ');readln(DataCari);
    Ditemukan := false; // Awalnya asumsikan data tidak ditemukan

    for i := 1 to MAKSDATA do // Periksa semua data dalam array
    begin
        if(TanggalPeriksa[i] = DataCari) then
        begin
            Ditemukan := true; // Data ditemukan
            writeln('+-------------------------------------------------------+');
            writeln('|                 DATA PASEIN-',i,'                         |');
            writeln('+-------------------------------------------------------+');
            writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
            writeln('| Nama                       : ', Nama[i]:15, '          |');
            writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
            writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
            writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
            writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
            writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
            writeln('+-------------------------------------------------------+');
            writeln; // Beri jarak antar data
        end;
    end;

    if not Ditemukan then
    begin
        writeln(DataCari, ' Tidak ditemukan');
    end;
end;


procedure CariBeratBadan(var BeratBadan : ArrayBerat);
var
    i,DataCari : integer;
    Ditemukan : boolean; // Variabel untuk menandai apakah data ditemukan
begin
    write('Berat Badan yang dicari : ');readln(DataCari);
    Ditemukan := false; // Awalnya asumsikan data tidak ditemukan

    for i := 1 to MAKSDATA do // Periksa semua data dalam array
    begin
        if(BeratBadan[i] = DataCari) then
        begin
            Ditemukan := true; // Data ditemukan
            writeln('+-------------------------------------------------------+');
            writeln('|                 DATA PASEIN-',i,'                         |');
            writeln('+-------------------------------------------------------+');
            writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
            writeln('| Nama                       : ', Nama[i]:15, '          |');
            writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
            writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
            writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
            writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
            writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
            writeln('+-------------------------------------------------------+');
            writeln; // Beri jarak antar data
        end;
    end;

    if not Ditemukan then
    begin
        writeln(DataCari, ' Tidak ditemukan');
    end;
end;


procedure CariTinggiBadan(var TinggiBadan : ArrayTinggi);
var
    i,DataCari : integer;
    Ditemukan : boolean; // Variabel untuk menandai apakah data ditemukan
begin
    write('Tinggi Badan yang dicari : ');readln(DataCari);
    Ditemukan := false; // Awalnya asumsikan data tidak ditemukan

    for i := 1 to MAKSDATA do // Periksa semua data dalam array
    begin
        if(TinggiBadan[i] = DataCari) then
        begin
            Ditemukan := true; // Data ditemukan
            writeln('+-------------------------------------------------------+');
            writeln('|                 DATA PASEIN-',i,'                         |');
            writeln('+-------------------------------------------------------+');
            writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
            writeln('| Nama                       : ', Nama[i]:15, '          |');
            writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
            writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
            writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
            writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
            writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
            writeln('+-------------------------------------------------------+');
            writeln; // Beri jarak antar data
        end;
    end;

    if not Ditemukan then
    begin
        writeln(DataCari, ' Tidak ditemukan');
    end;
end;

procedure CariDiagnosa(var Diagnosa : ArrayDiagnosa);
var
    i : integer;
    DataCari : string;
    Ditemukan : boolean; // Variabel untuk menandai apakah data ditemukan
begin
    write('Diagnosa yang dicari : ');readln(DataCari);
    Ditemukan := false; // Awalnya asumsikan data tidak ditemukan

    for i := 1 to MAKSDATA do // Periksa semua data dalam array
    begin
        if(Diagnosa[i] = DataCari) then
        begin
            Ditemukan := true; // Data ditemukan
            writeln('+-------------------------------------------------------+');
            writeln('|                 DATA PASEIN-',i,'                         |');
            writeln('+-------------------------------------------------------+');
            writeln('| No. Rekam Medis            :      ', NoRM[i]:8, '            |');
            writeln('| Nama                       : ', Nama[i]:15, '          |');
            writeln('| Jenis Kelamin              :            ', JenisKelamin[i]:2,'            |');
            writeln('| Tanggal Periksa [DD/MM/YY] :     ', TanggalPeriksa[i]:10, '           |');
            writeln('| Berat Badan                :         ', BeratBadan[i]:5, '            |');
            writeln('| Tinggi Badan               :         ', TinggiBadan[i]:5, '            |');
            writeln('| Diagnosa                   : ', Diagnosa[i]:15, '          |');
            writeln('+-------------------------------------------------------+');

            writeln; // Beri jarak antar data
        end;
    end;

    if not Ditemukan then
    begin
        writeln(DataCari, ' Tidak ditemukan');
    end;
end;


procedure RekapRekamMedis(JenisKelamin : ArrayKelamin; BeratBadan: ArrayBerat; TinggiBadan: ArrayTinggi; BanyakData: integer);
var
    i, JumlahLaki, JumlahPerempuan: integer;
    TotalBerat, TotalTinggi, MaxBerat, MinBerat, MaxTinggi, MinTinggi: integer;
    RataBerat, RataTinggi: real;
begin
    if (BanyakData = 0) then
    begin
        writeln('Belum ada data!');
    end
    else
    begin
        JumlahLaki := 0;
    JumlahPerempuan := 0;
    TotalBerat := 0;
    TotalTinggi := 0;
    
    // Inisialisasi nilai max dan min dengan data pertama jika ada
    if BanyakData > 0 then
    begin
        MaxBerat := BeratBadan[1];
        MinBerat := BeratBadan[1];
        MaxTinggi := TinggiBadan[1];
        MinTinggi := TinggiBadan[1];
    end;

    for i := 1 to BanyakData do
    begin
        // Hitung jumlah gender
        if (UpperCase(JenisKelamin[i]) = 'L') then
        begin
            JumlahLaki := JumlahLaki + 1
        end;

        if (UpperCase(JenisKelamin[i]) = 'P') then
        begin
            JumlahPerempuan := JumlahPerempuan + 1;
        end;

        // Hitung total berat dan tinggi
        TotalBerat := TotalBerat + BeratBadan[i];
        TotalTinggi := TotalTinggi + TinggiBadan[i];

        // Cari berat maksimum dan minimum
        if (BeratBadan[i] > MaxBerat) then
        begin
            MaxBerat := BeratBadan[i];
        end;
        if (BeratBadan[i] < MinBerat) then
        begin
            MinBerat := BeratBadan[i];
        end;

        // Cari tinggi maksimum dan minimum
        if (TinggiBadan[i] > MaxTinggi) then
        begin
            MaxTinggi := TinggiBadan[i];
        end;
        if (TinggiBadan[i] < MinTinggi) then
        begin
            MinTinggi := TinggiBadan[i];
        end;

        // Hitung rata-rata
        if (BanyakData > 0) then
        begin
            RataBerat := TotalBerat / BanyakData;
            RataTinggi := TotalTinggi / BanyakData;
        end
        else
        begin
            RataBerat := 0;
            RataTinggi := 0;
        end;
        clrscr;
        // Tampilkan hasil rekap
        writeln('+--------------------------------------------+');
        writeln('|                  REKAP DATA                |');
        writeln('+-------------------------+------------------+');
        writeln('| Total Pasein            | ', BanyakData:8, '         |');
        writeln('+-------------------------+------------------+');
        writeln('| Jumlah Pasien Laki      | ', JumlahLaki:8, '         |');
        writeln('| Jumlah Pasien Perempuan | ', JumlahPerempuan:8, '         |');
        writeln('+-------------------------+------------------+');
        writeln('| Rata-rata Berat Badan   | ', RataBerat:8:2, ' kg      |');
        writeln('| Rata-rata Tinggi Badan  | ', RataTinggi:8:2, ' cm      |');
        writeln('+-------------------------+------------------+');
        writeln('| Berat Maksimum          | ', MaxBerat:8, ' kg      |');
        writeln('| Berat Minimum           | ', MinBerat:8, ' kg      |');
        writeln('| Tinggi Maksimum         | ', MaxTinggi:8, ' cm      |');
        writeln('| Tinggi Minimum          | ', MinTinggi:8, ' cm      |');
        writeln('+-------------------------+------------------+');
        end;
    end;
end;

procedure PilihanCariPasien(var MetodeCariPasein : integer);
begin
    if(BanyakData = 0) then
    begin
        writeln('Belum ada data!');
    end
    else
    begin
        writeln ('+================================+');
        writeln ('|          MENU PASIEN           |');
        writeln ('+================================+');
        writeln ('|       1. Cari Rekam Medis      |');
        writeln ('|       2. Cari Nama             |');
        writeln ('|       0. Keluar                |');
        writeln ('+================================+');
        write('Pilihan? ');readln(MetodeCariPasein);
    end;
end;


//Algoritma Utama
begin
    clrscr;
    BanyakData := 0;
    ArrayTest(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa);
    MenuPilihan(Pilihan);
    while(Pilihan <> 0) do
    begin
        case (Pilihan) of
            1 : begin
                clrscr;
                MenuPasien(PilihanPasien);
                while(PilihanPasien <> 0) do
                begin
                    case (PilihanPasien) of
                        1 : begin
                            clrscr;
                            PilihanCariPasien(MetodeCariPasein);
                            while(MetodeCariPasein <> 0) do
                            begin
                                case(MetodeCariPasein) of
                                    1 : begin
                                        clrscr;
                                        UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                        CariNoRM(NoRM, BanyakData);
                                    end;
                                    2 : begin
                                        clrscr;
                                        CariNama(Nama);
                                    end;
                                end;
                            clrscr;
                            PilihanCariPasien(MetodeCariPasein);
                            end;
                        end;
                    end;
                clrscr;
                MenuPasien(PilihanPasien);
                end;
            end;
            2: begin
                clrscr;
                MenuDokter( PilihanDokter);
                while(PilihanDokter <> 0) do
                begin
                    case(PilihanDokter) of
                        1 : begin
                            clrscr;
                            IsiData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                            
                        end;
                        2 : begin
                            clrscr;
                            TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                            readln;
                        end;
                        3: begin
                            clrscr;
                            EditData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                        end;
                        4: begin
                            clrscr;
                            MenuPengurutan(PilihanPengurutan);
                            while(PilihanPengurutan <> 0) do
                            begin
                                case(PilihanPengurutan) of
                                    1 : begin
                                        clrscr;
                                        MenuSortingAsc(PilihanAsc);
                                        while(PilihanAsc <> 0) do
                                        begin
                                            case(PilihanAsc) of
                                                1 : begin
                                                    clrscr;
                                                    UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                2 : begin
                                                    clrscr;
                                                    UrutNamaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                3 : begin
                                                    clrscr;
                                                    UrutTanggalPeriksaAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                4 : begin
                                                    clrscr;
                                                    UrutBeratBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                5 : begin
                                                    clrscr;
                                                    UrutTinggiBadanAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                            end;
                                        clrscr;
                                        MenuSortingAsc(PilihanAsc);
                                        end;
                                    end;
                                    2 : begin
                                        clrscr;
                                        MenuSortingDsc(PilihanDsc);
                                        while(PilihanDsc <> 0) do
                                        begin
                                            case(PilihanDsc) of
                                                1 : begin
                                                    clrscr;
                                                    UrutNoRMDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;


                                                end;
                                                2 : begin
                                                    clrscr;
                                                    UrutNamaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                3 : begin
                                                    clrscr;
                                                    UrutTanggalPeriksaDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                4 : begin
                                                    clrscr;
                                                    UrutBeratBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                                5 : begin
                                                    clrscr;
                                                    UrutTinggiBadanDsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                                    TampilData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData );
                                                    readln;

                                                end;
                                            end;
                                        clrscr;
                                        MenuSortingDsc(PilihanDsc);
                                        end;   
                                    end;
                                end;
                            clrscr;
                            MenuPengurutan(PilihanPengurutan);
                            end;
                        end;
                        5: begin
                            clrscr;
                            MenuPecarian(PilihanPencarian);
                            while(PilihanPencarian <> 0) do
                            begin
                                case (PilihanPencarian) of
                                    1 : begin
                                        clrscr;
                                        UrutNoRMAsc(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                                        CariNoRM(NoRM, BanyakData);
                                        readln;

                                    end;
                                    2 : begin
                                        clrscr;
                                        CariNama(Nama);
                                        readln;

                                    end;
                                    3 : begin
                                        clrscr;
                                        CariJenisKelamin(JenisKelamin);
                                        readln;

                                    end;
                                    4 : begin
                                        clrscr;
                                        CariTanggalPeriksa(TanggalPeriksa);
                                        readln;

                                    end;
                                    5 : begin
                                        clrscr;
                                        CariBeratBadan(BeratBadan);
                                        readln;

                                    end;
                                    6 : begin
                                        clrscr;
                                        CariTinggiBadan(TinggiBadan);
                                        readln;

                                    end;
                                    7 : begin
                                        clrscr;
                                        CariDiagnosa(Diagnosa);
                                        readln;

                                    end;
                                end;
                            readln;
                            clrscr;
                            MenuPecarian(PilihanPencarian);
                            end;
                        end;
                        6: begin
                            clrscr;
                            PenghapusanData(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa, BanyakData);
                            readln;
                        end;
                        7: begin
                            clrscr;
                            PenghancuranArray(NoRM, Nama, JenisKelamin, TanggalPeriksa, BeratBadan, TinggiBadan, Diagnosa);
                            BanyakData := 0;
                            writeln('Semua data telah dihancurkan');
                            readln;
                        end;
                        8: begin
                            clrscr;
                            RekapRekamMedis(JenisKelamin, BeratBadan, TinggiBadan, BanyakData);
                            readln;
                        end;
                    end;
                clrscr;
                MenuDokter( PilihanDokter);
                end;
            end;
        end;
    clrscr;
    MenuPilihan(Pilihan);
    end;
    clrscr;
    write('Selamat Tinggal!');
end.
