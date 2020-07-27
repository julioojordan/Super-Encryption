#======================================================
# ENKRIPSI DEKRIPSI MENGGUNAKAN SUPER ENKRIPSI CIPHER||
# JULIO ADNYAN JORDAN ARYANTO (24060117130078)       ||
#                                                    ||
#CATATAN:                                            ||
# substitusi yang digunakan adalah Caesar Cipher     ||
#======================================================
#MULAI

#from array import *
# Inisialisasi
# Fungsi Enkripsi Substitusi Caesar Cipher
def SEnkripsi(Kar):
    if Kar == 'A' :
        return 'D'
    elif Kar =='B':
        return 'E'
    elif Kar =='C':
        return 'F'
    elif Kar =='D':
        return 'G'
    elif Kar =='E':
        return 'H'
    elif Kar =='F':
        return 'I'
    elif Kar =='G':
        return 'J'
    elif Kar =='H':
        return 'K'
    elif Kar =='I':
        return 'L'
    elif Kar =='J':
        return 'M'
    elif Kar =='K':
        return 'N'
    elif Kar =='L':
        return 'O'
    elif Kar =='M':
        return 'P'
    elif Kar =='N':
        return 'Q'
    elif Kar =='O':
        return 'R'
    elif Kar =='P':
        return 'S'
    elif Kar =='Q':
        return 'T'
    elif Kar =='R':
        return 'U'
    elif Kar =='S':
        return 'V'
    elif Kar =='T':
        return 'W'
    elif Kar =='U':
        return 'X'
    elif Kar =='V':
        return 'Y'
    elif Kar =='W':
        return 'Z'
    elif Kar =='X':
        return 'A'
    elif Kar =='Y':
        return 'B'
    elif Kar =='Z':
        return 'C'
    else :
        return ''
    
# Fungsi dekripsi Subtitusi Caesar Cipher   
def SDekripsi(Kar):
    if Kar == 'D' :
        return 'A'
    elif Kar =='E':
        return 'B'
    elif Kar =='F':
        return 'C'
    elif Kar =='G':
        return 'D'
    elif Kar =='H':
        return 'E'
    elif Kar =='I':
        return 'F'
    elif Kar =='J':
        return 'G'
    elif Kar =='K':
        return 'H'
    elif Kar =='L':
        return 'I'
    elif Kar =='M':
        return 'J'
    elif Kar =='N':
        return 'K'
    elif Kar =='O':
        return 'L'
    elif Kar =='P':
        return 'M'
    elif Kar =='Q':
        return 'N'
    elif Kar =='R':
        return 'O'
    elif Kar =='S':
        return 'P'
    elif Kar =='T':
        return 'Q'
    elif Kar =='U':
        return 'R'
    elif Kar =='V':
        return 'S'
    elif Kar =='W':
        return 'T'
    elif Kar =='X':
        return 'U'
    elif Kar =='Y':
        return 'V'
    elif Kar =='Z':
        return 'W'
    elif Kar =='A':
        return 'X'
    elif Kar =='B':
        return 'Y'
    elif Kar =='C':
        return 'Z'
    else :
        return ''

#nilai Dummy D
D = "X"

#Realisasi

def begin():
    print ("=================================")

    print ("Apa yang ingin Dilakukan ?")
    print ("1. Enkripsi dengan Super Enkripsi")
    print ("2. Dekripsi dengan Super Enkripsi")
    print ("=================================")

    pil = input("Masukan Pilihan Anda:")

    if pil == '1':
        Enkripsi()
    elif pil == '2':
        Dekripsi()
    else :
        begin()
#==============================

#==============================
def Enkripsi():
    #list untuk hasil enkripsi
    Eteks1 = [] #hasil untuk enkripsi substitusi
    Eteks2 = [] #hasil untuk enkripsi transposisi

    teks = input("Masukan Plainteks : ")
    k = input("Masukan Nilai K : ")
    k = int(k)
    #mengubah semua inputan teks menjadi kapital
    Uteks = teks.upper()
    #menghilangkan spasi di Cteks
    Ateks = []
    for j in range(len(Uteks)):
        if Uteks[j] != ' ' :
            Ateks.append(Uteks[j])
    #print(Ateks)

    #----- Tahap 1 -----
    #Melakukan enkripsi substitusi
    for i in range(len(Ateks)):
        Eteks1.append(SEnkripsi(Ateks[i]))
    #----- END Tahap 1 -----

    #----- Tahap 2 -----
    # Melakukan Enkripsi Transposisi
    # (1) Menambahkan nilai dummy ke teks apabila Eteks1 mod k != 0
    if (len(Eteks1)%k != 0):
        batas = k - len(Eteks1)%k
        for i in range(batas):
            Eteks1.append("X")
            
    # (2) Memasukan nilai Eteks1 kedalam matrix transposisi
    count_baris = int(len(Eteks1)/k)
    count_kolom = int(len(Eteks1)/count_baris)
    matrix_transposisi = [[] for k in range(count_baris)]
    counter = 0
    for baris in range(len(matrix_transposisi)):
        for kolom in range(count_kolom):
            matrix_transposisi[baris].append(Eteks1[counter])
            counter = counter + 1
    #print(matrix_transposisi)
    
    # (3) Melakukan transpose matrix untuk mendapatkan Cipherteks
    temp_row = []
    tranpose_matrix = []

    for kolom in range(len(matrix_transposisi[0])):
        for baris in range(len(matrix_transposisi)):
            temp_row.append(matrix_transposisi[baris][kolom])
        tranpose_matrix.append(temp_row)
        temp_row = []
    #print(tranpose_matrix)

    # (4) Memasukan hasil tranpose kedalam Eteks2 secara horizontal
    for baris in range(len(tranpose_matrix)):
        for kolom in range(len(tranpose_matrix[0])):
            Eteks2.append(tranpose_matrix[baris][kolom])
    #print(Eteks2)

    # (5) Menampilkan Hasil
    print ("Cipherteks yang didapatkan dari enkripsi Super Enkripsi adalah ="+" ".join(Eteks2))
    begin()
    #----- END Tahap 2 -----
#==============================

#==============================
def Dekripsi():
    teks = input("Masukan Cipherteks : ")
    k = input("Masukan Nilai K : ")
    k = int(k)
    #mengubah semua inputan teks menjadi kapital
    Uteks = teks.upper()
    #menghilangkan spasi di Cteks
    Ateks = []
    for j in range(len(Uteks)):
        if Uteks[j] != ' ' :
            Ateks.append(Uteks[j])
    print(Ateks)

    #----- Tahap 1 -----
    #Melakukan Dekripsi transposisi
    n = 1 
    while(n <= k):
        #List untuk hasil Dekripsi 
        Dteks1 = [] #hasil untuk dekripsi transposisi
        Dteks2 = [] #hasil untuk dekripsi Substitusi
        # (1) Menambahkan nilai dummy ke teks apabila Ateks mod k != 0
        if (len(Ateks)%k != 0):
            batas = k - len(Ateks)%k
            for i in range(batas):
                Ateks.append("X")
        # (2) Memasukan nilai Ateks kedalam matrix transposisi 
        matrix_transposisi = [[] for b in range(n)]
        count_baris = len(matrix_transposisi)
        count_kolom = int(len(Ateks)/k)
        counter = 0
        for baris in range(count_baris):
            for kolom in range(count_kolom):
                matrix_transposisi[baris].append(Ateks[counter])
                counter = counter + 1
                
        # (3) Tranpose matrix_transposisi
        temp_row = []
        tranpose_matrix = []

        for kolom in range(len(matrix_transposisi[0])):
            for baris in range(len(matrix_transposisi)):
                temp_row.append(matrix_transposisi[baris][kolom])
            tranpose_matrix.append(temp_row)
            temp_row = []

        # (4) Memasukan Hasil Tranpose Ke dalam Dteks1
        for baris in range(len(tranpose_matrix)):
            for kolom in range(len(tranpose_matrix[0])):
                Dteks1.append(tranpose_matrix[baris][kolom])
        #----- END Tahap 1 -----


        #----- Tahap 2 -----
        #melakukan dekripsi substitusi dari Dteks1
        for i in range(len(Dteks1)):
            Dteks2.append(SDekripsi(Dteks1[i]))
        #----- END Tahap 2 -----
        print ("Plainteks yang didapatkan dari dekripsi Super Enkripsi dengan k =",n,"adalah ="+" ".join(Dteks2))
        n = n + 1
    begin()
#==============================

#==============================
    
begin()
        
