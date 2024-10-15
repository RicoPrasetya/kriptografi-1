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
