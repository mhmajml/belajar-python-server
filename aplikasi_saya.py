# Program untuk menghitung luas segitiga

# Minta input alas dan tinggi dari pengguna
alas = float(input("Masukkan panjang alas segitiga (dalam satuan cm): "))
tinggi = float(input("Masukkan tinggi segitiga (dalam satuan cm): "))

# Hitung luas segitiga
luas = 0.5 * alas * tinggi

# Tampilkan hasil
print(f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm²")