# Caesar cipher encryption
key = 3
huruf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def encrypt(pesan):
    for i in range(len(pesan)):
        for j in range(len(huruf)):
            if pesan[i] == huruf[j]:
                try:
                    if j == 23:
                        pesan[i] = 'A'
                    elif j == 24:
                        pesan[i] = 'B'
                    elif j == 25:
                        pesan[i] = 'C'
                    pesan[i] = huruf[j+key]
                    break
                except:
                    pass
            else:
                pass
    print("Encrypted message : ", end="")
    for i in pesan:
        print(i, end="")
    print('\n')

def decrypt(pesan):
    for i in range(len(pesan)):
        for j in range(len(huruf)):
            if pesan[i] == huruf[j]:
                try:
                    if j == 2:
                        pesan[i] = 'Z'
                    elif j == 1:
                        pesan[i] = 'Y'
                    elif j == 0:
                        pesan[i] = 'X'
                    pesan[i] = huruf[j-key]
                    break
                except:
                    pass
            else:
                pass
    print("Decrypted message : ", end="")
    for i in pesan:
        print(i, end="")
    print('\n')

while True:
    print("===CAESAR CIPHER ENCRYPTION===")
    print("1. Encryption    2. Decryption")
    pilih = int(input("Silahkan Pilih : "))
    if pilih == 1:
        pesan = list(input("Masukan Pesan : ").upper())
        encrypt(pesan)
    else:
        pesan = list(input("Masukan encryted code : ").upper())
        decrypt(pesan)