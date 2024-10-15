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
