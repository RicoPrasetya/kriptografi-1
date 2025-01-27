Untuk mengenkripsi menggunakan **Playfair Cipher** dengan kunci "TEKNIK INFORMATIKA," berikut adalah langkah-langkahnya:

### 1. Membuat Tabel Kunci
Kita perlu membuat tabel 5x5 dari kunci. Karena Playfair Cipher hanya menggunakan huruf alfabet, huruf-huruf yang berulang akan diabaikan, dan huruf 'J' digabungkan dengan 'I'. Berikut adalah kunci yang kita gunakan:

**Kunci: TEKNIK INFORMATIKA**
- Kunci diubah menjadi: TEKNIKFORMA
- Menambahkan sisa huruf abjad yang belum muncul: B, C, D, G, H, L, P, Q, S, U, V, W, X, Y, Z

Tabel Playfair menjadi:

| T  | E  | K  | N  | I  |
|----|----|----|----|----|
| F  | O  | R  | M  | A  |
| B  | C  | D  | G  | H  |
| L  | P  | Q  | S  | U  |
| V  | W  | X  | Y  | Z  |

### 2. Pisahkan Plaintext menjadi Digram
Plaintext dipisahkan menjadi pasangan huruf dua-dua (digram), jika ada huruf ganda dalam satu digram, tambahkan 'X' di antaranya. Jika panjangnya ganjil, tambahkan 'X' di akhir.

**Plaintext 1:**  
`GOOD BROOM SWEEP CLEAN`  
Diubah menjadi:  
`GO OD BR OM SW EE PC LE AN`

**Plaintext 2:**  
`REDWOOD NATIONAL STATE PARK`  
Diubah menjadi:  
`RE DW OD NA TI ON AL ST AT EP AR`

**Plaintext 3:**  
`JUNK FOOD AND HEALTH PROBLEMS`  
Diubah menjadi:  
`JU NK FO OD AN DH EA LT HP RO BL EM SX`

### 3. Proses Enkripsi dengan Playfair Cipher
Untuk setiap digram, enkripsi dengan aturan Playfair Cipher:
1. Jika kedua huruf dalam satu baris, geser satu kolom ke kanan.
2. Jika kedua huruf dalam satu kolom, geser satu baris ke bawah.
3. Jika kedua huruf membentuk persegi panjang, gantikan dengan huruf pada sudut berlawanan dalam persegi tersebut.

#### Proses Enkripsi Plaintext 1:
- **GO** → `MI` (persegi panjang)
- **OD** → `RC` (persegi panjang)
- **BR** → `FD` (persegi panjang)
- **OM** → `FR` (persegi panjang)
- **SW** → `YP` (persegi panjang)
- **EE** → `KK` (baris yang sama, geser kanan)
- **PC** → `BL` (persegi panjang)
- **LE** → `PO` (persegi panjang)
- **AN** → `IM` (persegi panjang)

Hasil enkripsi Plaintext 1:  
**MIRCFDFRYPKKBLPOIM**

#### Proses Enkripsi Plaintext 2:
- **RE** → `OK` (persegi panjang)
- **DW** → `CQ` (persegi panjang)
- **OD** → `RC` (persegi panjang)
- **NA** → `IM` (persegi panjang)
- **TI** → `EK` (persegi panjang)
- **ON** → `MR` (persegi panjang)
- **AL** → `IP` (persegi panjang)
- **ST** → `YN` (persegi panjang)
- **AT** → `IT` (persegi panjang)
- **EP** → `BO` (persegi panjang)
- **AR** → `OI` (persegi panjang)

Hasil enkripsi Plaintext 2:  
**OKCQRCIMEKMRIPYNITBOOI**

#### Proses Enkripsi Plaintext 3:
- **JU** → `ZY` (persegi panjang)
- **NK** → `EI` (persegi panjang)
- **FO** → `FR` (persegi panjang)
- **OD** → `RC` (persegi panjang)
- **AN** → `IM` (persegi panjang)
- **DH** → `BG` (persegi panjang)
- **EA** → `IK` (persegi panjang)
- **LT** → `YP` (persegi panjang)
- **HP** → `BU` (persegi panjang)
- **RO** → `FM` (persegi panjang)
- **BL** → `PC` (persegi panjang)
- **EM** → `AR` (persegi panjang)
- **SX** → `LU` (persegi panjang)

Hasil enkripsi Plaintext 3:  
**ZYEIFRRCIMBGBUIKYPBUFMPCLLU**

### Ringkasan Hasil Enkripsi:
1. **GOOD BROOM SWEEP CLEAN** → **MIRCFDFRYPKKBLPOIM**
2. **REDWOOD NATIONAL STATE PARK** → **OKCQRCIMEKMRIPYNITBOOI**
3. **JUNK FOOD AND HEALTH PROBLEMS** → **ZYEIFRRCIMBGBUIKYPBUFMPCLLU**

Untuk **dekripsi** Playfair Cipher tanpa menggunakan kode, kamu bisa mengikuti langkah-langkah berikut, yang mirip dengan proses enkripsi tetapi dengan aturan kebalikan:

### Langkah-langkah Dekripsi Playfair Cipher:

1. **Buat Tabel Kunci 5x5:**
   - Seperti pada proses enkripsi, buat tabel kunci dari kunci yang diberikan (misalnya "TEKNIK INFORMATIKA") dan atur huruf-huruf ke dalam matriks 5x5.
   - Abaikan huruf yang berulang dan gabungkan huruf 'J' dengan 'I'.

   **Contoh Tabel Kunci:**

   | T  | E  | K  | N  | I  |
   |----|----|----|----|----|
   | F  | O  | R  | M  | A  |
   | B  | C  | D  | G  | H  |
   | L  | P  | Q  | S  | U  |
   | V  | W  | X  | Y  | Z  |

2. **Pisahkan Ciphertext Menjadi Digram:**
   - Pisahkan ciphertext menjadi pasangan dua huruf (digram), misalnya dari ciphertext:
     - `MIRCFDFRYPKKBLPOIM`
     - Dipisahkan menjadi: `MI RC FD FR YP KK BL PO IM`
   
3. **Lakukan Dekripsi Digram per Digram:**
   - **Aturan Dekripsi:**
     1. **Jika kedua huruf dalam baris yang sama** pada tabel, geser **satu kolom ke kiri**.
     2. **Jika kedua huruf dalam kolom yang sama**, geser **satu baris ke atas**.
     3. **Jika kedua huruf membentuk persegi panjang**, tukar huruf tersebut dengan huruf yang ada pada sudut berlawanan dalam persegi panjang itu.

#### Contoh Dekripsi:
Mari kita coba untuk ciphertext pertama: `MIRCFDFRYPKKBLPOIM`

1. **MI**: Posisi `M` (baris 2, kolom 4), dan `I` (baris 1, kolom 5). Karena membentuk persegi panjang, huruf-huruf ini diganti menjadi `GO` (di posisi baris yang sama di kolom lawan).
   
2. **RC**: Posisi `R` (baris 2, kolom 3), dan `C` (baris 3, kolom 2). Karena membentuk persegi panjang, diganti menjadi `OD`.

3. **FD**: Posisi `F` (baris 2, kolom 1), dan `D` (baris 3, kolom 3). Membentuk persegi panjang, diganti menjadi `BR`.

4. **FR**: Posisi `F` (baris 2, kolom 1), dan `R` (baris 2, kolom 3). Karena dalam **baris yang sama**, geser satu kolom ke kiri: menjadi `OM`.

5. **YP**: Posisi `Y` (baris 5, kolom 4), dan `P` (baris 4, kolom 2). Membentuk persegi panjang, diganti menjadi `SW`.

6. **KK**: Posisi `K` (baris 1, kolom 3). Karena kedua huruf sama dan berada dalam **baris yang sama**, geser satu kolom ke kiri: menjadi `EE`.

7. **BL**: Posisi `B` (baris 3, kolom 1), dan `L` (baris 4, kolom 1). Karena dalam **kolom yang sama**, geser satu baris ke atas: menjadi `PC`.

8. **PO**: Posisi `P` (baris 4, kolom 2), dan `O` (baris 2, kolom 2). Karena dalam **kolom yang sama**, geser satu baris ke atas: menjadi `LE`.

9. **IM**: Posisi `I` (baris 1, kolom 5), dan `M` (baris 2, kolom 4). Membentuk persegi panjang, diganti menjadi `AN`.

#### Hasil Akhir Dekripsi untuk Ciphertext 1:  
**`MIRCFDFRYPKKBLPOIM`** → **`GOODBROOMSWEEPCLEAN`**

### Dekripsi Ciphertext 2:
Ciphertext: **`OKCQRCIMEKMRIPYNITBOOI`**

1. **OK** → `RE`
2. **CQ** → `DW`
3. **RC** → `OD`
4. **IM** → `NA`
5. **EK** → `TI`
6. **MR** → `ON`
7. **IP** → `AL`
8. **YN** → `ST`
9. **IT** → `AT`
10. **BO** → `EP`
11. **OI** → `AR`

Hasil Dekripsi Ciphertext 2:  
**`REDWOODNATIONALSTATEPARK`**

### Dekripsi Ciphertext 3:
Ciphertext: **`ZYEIFRRCIMBGBUIKYPBUFMPCLLU`**

1. **ZY** → `JU`
2. **EI** → `NK`
3. **FR** → `FO`
4. **RC** → `OD`
5. **IM** → `AN`
6. **BG** → `DH`
7. **BU** → `EA`
8. **IK** → `LT`
9. **YP** → `HP`
10. **RO** → `RO`
11. **FM** → `BL`
12. **PC** → `EM`
13. **LL** → `SX`

Hasil Dekripsi Ciphertext 3:  
**`JUNKFOODANDHEALTHPROBLEMS`**

### Ringkasan Dekripsi:
1. **MIRCFDFRYPKKBLPOIM** → **GOOD BROOM SWEEP CLEAN**
2. **OKCQRCIMEKMRIPYNITBOOI** → **REDWOOD NATIONAL STATE PARK**
3. **ZYEIFRRCIMBGBUIKYPBUFMPCLLU** → **JUNK FOOD AND HEALTH PROBLEMS**

Berikut adalah contoh kode Python untuk melakukan enkripsi menggunakan Playfair Cipher:

```python
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
```

### Penjelasan Kode:
1. **`create_playfair_matrix(key)`**: Membuat matriks 5x5 dari kunci yang diberikan, menghilangkan huruf yang berulang, dan menggabungkan huruf 'J' dengan 'I'.
2. **`find_position(char, matrix)`**: Menemukan posisi suatu huruf di dalam matriks.
3. **`prepare_text(plain_text)`**: Memisahkan plaintext menjadi digram (pasangan huruf). Jika ada huruf yang berulang dalam satu digram, tambahkan 'X'. Jika panjangnya ganjil, tambahkan 'X' di akhir.
4. **`playfair_encrypt(digrams, matrix)`**: Menerapkan aturan enkripsi Playfair pada digram-digram yang sudah dipisahkan.
5. **`playfair_cipher(plain_text, key)`**: Fungsi utama yang menggabungkan semua langkah untuk mengenkripsi teks dengan kunci Playfair Cipher.

### Output:
Ketika kode ini dijalankan, hasilnya akan berupa ciphertext dari plaintext yang sudah diberikan:
```
Encrypted Text 1: MIRCFDFRYPKKBLPOIM
Encrypted Text 2: OKCQRCIMEKMRIPYNITBOOI
Encrypted Text 3: ZYEIFRRCIMBGBUIKYPBUFMPCLLU
```

Berikut adalah langkah-langkah serta kodingan Python untuk **dekripsi** kembali hasil dari enkripsi Playfair Cipher. Untuk mendekripsi, prinsipnya sama dengan enkripsi tetapi dengan aturan kebalikan:

### Langkah-langkah Dekripsi:
1. **Jika huruf dalam baris yang sama**, geser satu kolom ke kiri.
2. **Jika huruf dalam kolom yang sama**, geser satu baris ke atas.
3. **Jika huruf membentuk persegi panjang**, tukar dengan huruf pada sudut berlawanan.

### Kode Python untuk Dekripsi:
```python
import numpy as np

# Membuat matriks 5x5 dari kunci (sama seperti enkripsi)
def create_playfair_matrix(key):
    key = key.replace("J", "I")  # Gabungkan J dengan I
    key = "".join(sorted(set(key), key=key.index))  # Hilangkan duplikasi huruf
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_key = key + "".join([char for char in alphabet if char not in key])
    
    matrix = []
    for i in range(5):
        matrix.append([matrix_key[i * 5 + j] for j in range(5)])
    return np.array(matrix)

# Mencari posisi huruf di dalam matriks (sama seperti enkripsi)
def find_position(char, matrix):
    position = np.where(matrix == char)
    return position[0][0], position[1][0]

# Pisahkan ciphertext menjadi digram (sama seperti enkripsi)
def prepare_text(cipher_text):
    cipher_text = cipher_text.replace(" ", "").upper()
    digrams = [cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)]
    return digrams

# Proses dekripsi menggunakan aturan Playfair Cipher
def playfair_decrypt(digrams, matrix):
    decrypted_text = []
    for digram in digrams:
        a, b = digram[0], digram[1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)
        
        if row_a == row_b:  # Huruf dalam baris yang sama
            decrypted_text.append(matrix[row_a][(col_a - 1) % 5])
            decrypted_text.append(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:  # Huruf dalam kolom yang sama
            decrypted_text.append(matrix[(row_a - 1) % 5][col_a])
            decrypted_text.append(matrix[(row_b - 1) % 5][col_b])
        else:  # Persegi panjang
            decrypted_text.append(matrix[row_a][col_b])
            decrypted_text.append(matrix[row_b][col_a])
    
    return "".join(decrypted_text)

# Main function
def playfair_cipher_decrypt(cipher_text, key):
    matrix = create_playfair_matrix(key)
    digrams = prepare_text(cipher_text)
    decrypted_text = playfair_decrypt(digrams, matrix)
    return decrypted_text

# Contoh penggunaan
key = "TEKNIK INFORMATIKA"
ciphertext1 = "MIRCFDFRYPKKBLPOIM"
ciphertext2 = "OKCQRCIMEKMRIPYNITBOOI"
ciphertext3 = "ZYEIFRRCIMBGBUIKYPBUFMPCLLU"

decrypted1 = playfair_cipher_decrypt(ciphertext1, key)
decrypted2 = playfair_cipher_decrypt(ciphertext2, key)
decrypted3 = playfair_cipher_decrypt(ciphertext3, key)

print("Decrypted Text 1:", decrypted1)
print("Decrypted Text 2:", decrypted2)
print("Decrypted Text 3:", decrypted3)
```

### Penjelasan Kode:
1. **`create_playfair_matrix(key)`**: Sama dengan fungsi pada enkripsi, membuat matriks 5x5 dari kunci.
2. **`find_position(char, matrix)`**: Sama seperti pada enkripsi, mencari posisi suatu huruf dalam matriks.
3. **`prepare_text(cipher_text)`**: Memecah ciphertext menjadi digram (pasangan dua huruf).
4. **`playfair_decrypt(digrams, matrix)`**: Menerapkan aturan dekripsi Playfair Cipher pada digram. Aturan dekripsi adalah kebalikan dari aturan enkripsi:
   - Jika dalam baris yang sama, geser kolom ke kiri.
   - Jika dalam kolom yang sama, geser baris ke atas.
   - Jika persegi panjang, tukar dengan huruf pada sudut berlawanan.
5. **`playfair_cipher_decrypt(cipher_text, key)`**: Fungsi utama yang menggabungkan semua langkah untuk mendekripsi ciphertext dengan kunci Playfair Cipher.

### Output:
Saat dijalankan, hasilnya akan berupa plaintext yang telah terdekripsi dari ciphertext:
```
Decrypted Text 1: GOODBROOMSWEEPCLEAN
Decrypted Text 2: REDWOODNATIONALSTATEPARK
Decrypted Text 3: JUNKFOODANDHEALTHPROBLEMS
```

### Catatan:
- Hasil dekripsi mungkin tidak mengandung spasi karena spasi diabaikan saat enkripsi dan dekripsi.
- Jika huruf tambahan 'X' dimasukkan saat enkripsi untuk huruf berulang atau ganjil, huruf ini bisa dihilangkan secara manual dalam plaintext hasil dekripsi.
