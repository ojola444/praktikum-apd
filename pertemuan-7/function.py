# def perkenalan():
#     print("halo aku bilek")

# perkenalan()

# def kali():
#     x = 5*5
#     print(x)

# kali()

# def luasPersgiPanjang(p, l):
#     if l == p :
#         return "bukan persegi panjang"
#     else :
#         luas = p*l
#         return luas

# print(luasPersgiPanjang(5,5))

# echo = {
#    "cost4" : ["Bell-Borne Geochelone", "crownless", "Fellian Beringal", "inferno rider"],
#    "cost3" : ["chop chop", "chaserazor", "kerasaur", "hoochief"],
#    "cost1" : ["fusion prism", "gulpuff", "excarat", "aero predator"]
# }
# def rowEcho () :
#     print("echo cost 4 : ")
#     for index,cost4 in enumerate(echo["cost4"]) :
#         print(f"{index} : {cost4}")
    
#     print("echo cost 3 : ")
#     for index,cost3 in enumerate(echo["cost3"]) :
#         print(f"{index + len(echo['cost4'])} : {cost3}")
    
#     print("echo cost 1 : ")
#     for index,cost1 in enumerate(echo["cost1"]) :
#         print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")


# rowEcho()

# def faktorial(n):
# # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
#     # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")
# # Output:
# # Hasil dari 5! adalah: 120

film = []


def show_data():
    if len(film) <= 0:
        print("Belum Ada data")
    else:
        print("ID | Judul Film")
        for indeks in range(len(film)):
            print(indeks, "|", film[indeks])

# Fungsi untuk menambah data
def insert_data():
    film_baru = input("Judul Film: ")
    film.append(film_baru)
    print("Film berhasil ditambahkan!")


# Fungsi untuk mengedit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID film: "))
    if indeks >= len(film) or indeks < 0:
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        film[indeks] = judul_baru
        print("Film berhasil diupdate!")


# Fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID film: "))
    if indeks >= len(film) or indeks < 0:
        print("ID salah")
    else:
        film.remove(film[indeks])
        print("Film berhasil dihapus!")


# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU---------- ")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    menu = input("PILIH MENU> ")
    print ("\n")

    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print ("Salah pilih!")

if __name__ == "__main__":
        while (True):
            show_menu()


