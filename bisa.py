import random

def main():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    print("🎲 Selamat datang di game Tebak Angka!")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    print("Bisakah kamu menebaknya?")

    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"🎉 Benar! Angkanya adalah {angka_rahasia}")
                print(f"Kamu berhasil menebak dalam {percobaan} kali percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid ya!")

if __name__ == "__main__":
    main()
