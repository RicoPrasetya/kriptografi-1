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
