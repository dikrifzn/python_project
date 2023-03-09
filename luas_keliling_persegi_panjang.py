import os

## Program Menghitung Luas dan Keliling di persegi panjang

#header
def header():
    os.system("cls")

    print(f"{'Program Menghitung':^40}")
    print(f"{'Luas dan Keliling Persegi Panjang':^40}")
    print("-"*40)

#input user
def input_user():
    panjang = int(input("Masukan Panjang : "))
    lebar = int(input("Masukan lebar : "))

    return panjang, lebar

def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2*(panjang + lebar)

while True:
    header()
    panjang, lebar = input_user()
    luas = hitung_luas(panjang, lebar)
    keliling = hitung_keliling(panjang, lebar)

    print(f"Luas Persegi Panjang Tersebut adalah {luas}")
    print(f"Keliling Persegi Panjang Tersebut adalah {keliling}")
    
    islanjut = input("Apakah ingin Melanjutkan (y/n?) ")
    if islanjut == "n":
        print("-"*40)
        print(f"{'Program Selesai':^40}")
        break