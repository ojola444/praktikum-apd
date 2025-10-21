# #membuat set 
 
# buah = {"mangga", "jeruk", "alpukat", "muani"}

# print(buah)

# for i in buah :
#     print(i, end=" ")

# angka = [1, 1, 2, 3, 4, 4]

# unik = set(angka)
# print(angka)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"
# } 
# }

# print(Biodata)

# for i, j in Biodata.items() :
#     print(f"{i} : {j}")

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama"))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)

# del Film["The Conjuring"]
 
# hapus = Film.pop("The Conjuring")
# print(hapus)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][3])

# dictKosong = {}
# setKosong = set(dictKosong)
# print(setKosong)

a = {10, 11, 12}
b = {11, 13, 14}

c = a | b
print(c)