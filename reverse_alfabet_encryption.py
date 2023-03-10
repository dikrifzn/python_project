alfabet =list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
rev_alfabet = list("ZYXWVUTSRQPONMLKJIHGFEDCBA")

def encrypt(pesan):
    for i in range(len(pesan)):
        for j in range(len(rev_alfabet)):
            if pesan[i] == rev_alfabet[j]:
                pesan[i] = alfabet[j]
                break
    print("Encrypted message : ", end="")
    for i in pesan:
        print(i, end="")
    print('\n')

def decrypt(pesan):
    for i in range(len(pesan)):
        for j in range(len(rev_alfabet)):
            if pesan[i] == alfabet[j]:
                pesan[i] = rev_alfabet[j]
                break
    print("Encrypted message : ", end="")
    for i in pesan:
        print(i, end="")
    print('\n')

while True:
    print("===REVERSE ALFABET ENCRYPTION===")
    print("1. Encryption    2. Decryption")
    pilih = int(input("Silahkan Pilih : "))
    if pilih == 1:
        pesan = list(input("Masukan Pesan : ").upper())
        encrypt(pesan)
    else:
        pesan = list(input("Masukan encryted code : ").upper())
        decrypt(pesan)
