from random import randint
import time
import os

print("="*5, "GAME TEBAK ANGKA", "="*5)
input("Tekan Enter Untuk Mulai ")
os.system("cls")
def load():
    for x in range(2):
        print("="*5, "GAME TEBAK ANGKA", "="*5)
        print("Sedang Mengacak Angka.")
        time.sleep(1)
        os.system("cls")

        print("="*5, "GAME TEBAK ANGKA", "="*5)
        print("Sedang Mengacak Angka..")
        time.sleep(1)
        os.system("cls")

        print("="*5, "GAME TEBAK ANGKA", "="*5)
        print("Sedang Mengacak Angka...")
        time.sleep(1)
        os.system("cls")
    global angka
    angka = randint(1, 10)

def tebak():
    print("="*5, "GAME TEBAK ANGKA", "="*5)
    global pilih
    pilih = int(input("Masukan Tebakan Anda : "))

def hasil():
    if(pilih == angka):
        print("Tebakan Anda Benar!")
        print("Angka acak adalah : ", angka)
        print("Tebakan anda adalah : ", pilih)
    else:
        print("Anda salah!")
        print("Angka acak adalah : ", angka)
        print("Tebakan anda adalah : ", pilih)

while True:
    load()
    tebak()
    hasil()
    ulang = input("Masih Ingin Main(y/n)? ")
    if(ulang == "y" or ulang == "Y"):
        os.system("cls")
    else:
        print("="*5, "Terimakasih", "="*5)
        break