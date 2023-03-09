data_base = ["baso", "bak mie", "nasi goreng"]
keyword = ""

def loops():
    if keyword == "":
        keyword = input("Apa Yang Ingin kamu Cari? : ")
    else:
        keyword.lower()
        search()

def search():
    for i in data_base:
        if i[0] == keyword[0]:
            print(i)
            loops()
        else:
            pass

while keyword == "" :
    keyword = input("Apa Yang Ingin kamu Cari? : ")
else:
    keyword.lower()
    search()