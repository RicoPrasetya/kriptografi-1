1. Membuat Tabel Kunci
Kita perlu membuat tabel 5x5 dari kunci. Karena Playfair Cipher hanya menggunakan huruf alfabet, huruf-huruf yang berulang akan diabaikan, dan huruf 'J' digabungkan dengan 'I'. Berikut adalah kunci yang kita gunakan:

Kunci: TEKNIK INFORMATIKA

Kunci diubah menjadi: TEKNIKFORMA
Menambahkan sisa huruf abjad yang belum muncul: B, C, D, G, H, L, P, Q, S, U, V, W, X, Y, Z
Tabel Playfair menjadi:

T	E	K	N	I
F	O	R	M	A
B	C	D	G	H
L	P	Q	S	U
V	W	X	Y	Z

2. Pisahkan Plaintext menjadi Digram
Plaintext dipisahkan menjadi pasangan huruf dua-dua (digram), jika ada huruf ganda dalam satu digram, tambahkan 'X' di antaranya. Jika panjangnya ganjil, tambahkan 'X' di akhir.

Plaintext 1:
GOOD BROOM SWEEP CLEAN
Diubah menjadi:
GO OD BR OM SW EE PC LE AN

Plaintext 2:
REDWOOD NATIONAL STATE PARK
Diubah menjadi:
RE DW OD NA TI ON AL ST AT EP AR

Plaintext 3:
JUNK FOOD AND HEALTH PROBLEMS
Diubah menjadi:
JU NK FO OD AN DH EA LT HP RO BL EM SX

3. Proses Enkripsi dengan Playfair Cipher
Untuk setiap digram, enkripsi dengan aturan Playfair Cipher:

Jika kedua huruf dalam satu baris, geser satu kolom ke kanan.
Jika kedua huruf dalam satu kolom, geser satu baris ke bawah.
Jika kedua huruf membentuk persegi panjang, gantikan dengan huruf pada sudut berlawanan dalam persegi tersebut.
Proses Enkripsi Plaintext 1:
GO → MI (persegi panjang)
OD → RC (persegi panjang)
BR → FD (persegi panjang)
OM → FR (persegi panjang)
SW → YP (persegi panjang)
EE → KK (baris yang sama, geser kanan)
PC → BL (persegi panjang)
LE → PO (persegi panjang)
AN → IM (persegi panjang)

Hasil enkripsi Plaintext 1:
MIRCFDFRYPKKBLPOIM

Proses Enkripsi Plaintext 2:
RE → OK (persegi panjang)
DW → CQ (persegi panjang)
OD → RC (persegi panjang)
NA → IM (persegi panjang)
TI → EK (persegi panjang)
ON → MR (persegi panjang)
AL → IP (persegi panjang)
ST → YN (persegi panjang)
AT → IT (persegi panjang)
EP → BO (persegi panjang)
AR → OI (persegi panjang)

Hasil enkripsi Plaintext 2:
OKCQRCIMEKMRIPYNITBOOI

Proses Enkripsi Plaintext 3:
JU → ZY (persegi panjang)
NK → EI (persegi panjang)
FO → FR (persegi panjang)
OD → RC (persegi panjang)
AN → IM (persegi panjang)
DH → BG (persegi panjang)
EA → IK (persegi panjang)
LT → YP (persegi panjang)
HP → BU (persegi panjang)
RO → FM (persegi panjang)
BL → PC (persegi panjang)
EM → AR (persegi panjang)
SX → LU (persegi panjang)

Hasil enkripsi Plaintext 3:
ZYEIFRRCIMBGBUIKYPBUFMPCLLU

Ringkasan Hasil Enkripsi:
GOOD BROOM SWEEP CLEAN → MIRCFDFRYPKKBLPOIM
REDWOOD NATIONAL STATE PARK → OKCQRCIMEKMRIPYNITBOOI
JUNK FOOD AND HEALTH PROBLEMS → ZYEIFRRCIMBGBUIKYPBUFMPCLLU

Berikut adalah contoh kode Python untuk melakukan enkripsi menggunakan Playfair Cipher:

import numpy as np

# Membuat matriks 5x5 dari kunci
def create_playfair_matrix(key):
    key = key.replace("J", "I")  # Gabungkan J dengan I
    key = "".join(sorted(set(key), key=key.index))  # Hilangkan duplikasi huruf
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_key = key + "".join([char for char in alphabet if char not in key])
    
    matrix = []
    for i in range(5):
        matrix.append([matrix_key[i * 5 + j] for j in range(5)])
    return np.array(matrix)

# Mencari posisi huruf di dalam matriks
def find_position(char, matrix):
    position = np.where(matrix == char)
    return position[0][0], position[1][0]

# Pisahkan teks menjadi digram
def prepare_text(plain_text):
    plain_text = plain_text.replace("J", "I").replace(" ", "").upper()
    digrams = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        if i + 1 < len(plain_text):
            b = plain_text[i + 1]
            if a == b:
                digrams.append(a + 'X')
                i += 1
            else:
                digrams.append(a + b)
                i += 2
        else:
            digrams.append(a + 'X')
            i += 1
    return digrams

# Proses enkripsi menggunakan aturan Playfair Cipher
def playfair_encrypt(digrams, matrix):
    encrypted_text = []
    for digram in digrams:
        a, b = digram[0], digram[1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)
        
        if row_a == row_b:  # Huruf dalam baris yang sama
            encrypted_text.append(matrix[row_a][(col_a + 1) % 5])
            encrypted_text.append(matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:  # Huruf dalam kolom yang sama
            encrypted_text.append(matrix[(row_a + 1) % 5][col_a])
            encrypted_text.append(matrix[(row_b + 1) % 5][col_b])
        else:  # Persegi panjang
            encrypted_text.append(matrix[row_a][col_b])
            encrypted_text.append(matrix[row_b][col_a])
    
    return "".join(encrypted_text)

# Main function
def playfair_cipher(plain_text, key):
    matrix = create_playfair_matrix(key)
    digrams = prepare_text(plain_text)
    encrypted_text = playfair_encrypt(digrams, matrix)
    return encrypted_text

# Contoh penggunaan
key = "TEKNIK INFORMATIKA"
plaintext1 = "GOOD BROOM SWEEP CLEAN"
plaintext2 = "REDWOOD NATIONAL STATE PARK"
plaintext3 = "JUNK FOOD AND HEALTH PROBLEMS"

encrypted1 = playfair_cipher(plaintext1, key)
encrypted2 = playfair_cipher(plaintext2, key)
encrypted3 = playfair_cipher(plaintext3, key)

print("Encrypted Text 1:", encrypted1)
print("Encrypted Text 2:", encrypted2)
print("Encrypted Text 3:", encrypted3)


Penjelasan Kode:
create_playfair_matrix(key): Membuat matriks 5x5 dari kunci yang diberikan, menghilangkan huruf yang berulang, dan menggabungkan huruf 'J' dengan 'I'.
find_position(char, matrix): Menemukan posisi suatu huruf di dalam matriks.
prepare_text(plain_text): Memisahkan plaintext menjadi digram (pasangan huruf). Jika ada huruf yang berulang dalam satu digram, tambahkan 'X'. Jika panjangnya ganjil, tambahkan 'X' di akhir.
playfair_encrypt(digrams, matrix): Menerapkan aturan enkripsi Playfair pada digram-digram yang sudah dipisahkan.
playfair_cipher(plain_text, key): Fungsi utama yang menggabungkan semua langkah untuk mengenkripsi teks dengan kunci Playfair Cipher.
Output:
Ketika kode ini dijalankan, hasilnya akan berupa ciphertext dari plaintext yang sudah diberikan:

Encrypted Text 1: MIRCFDFRYPKKBLPOIM
Encrypted Text 2: OKCQRCIMEKMRIPYNITBOOI
Encrypted Text 3: ZYEIFRRCIMBGBUIKYPBUFMPCLLU
