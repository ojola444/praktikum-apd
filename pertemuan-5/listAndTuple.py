# matakuliah = ["APD", "kalkulus", "orsikom","basdat","ai"]

# print(matakuliah[0:5:3])

# matakuliah1 = []

# matakuliah1.append("pkn")
 
# print(matakuliah1)

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(end="sebelum ditambah : ")
# print(studyclub)

# studyclub.insert(2,"Web")
# print(end="setelah ditambah : ")
# print(studyclub)

# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# print(end="memanggil list : ")
# print(praktikum[1])

# print(end="memanggil list dalam list : ")
# print(praktikum[4][0:])

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# studyclub[2] = "AI"
# print(studyclub)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# menghapus elemen pada indeks ke-2, yakni "Kalkulus"

# del matakuliah[2]
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# matakuliah.remove("Kalkulus")
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2

# ambil_matkul = matakuliah.pop(2)
# print(matakuliah)

# print(ambil_matkul)

# nomor = [1,2,3]

# kali = len(nomor) * 2

# print(kali)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# for peli, i in enumerate(matakuliah) :
#     print(f"{peli + 1} : {i}")

# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"]
# ]

# print(kelas[0][0:2])
# kelas[1].insert(1,"juned")
# print(kelas[1][1])

# for i in kelas :
#     for j in i :
#         print(end= j + ", ")

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))

# print(anggota[4][0])
# print(anggota[5][1])

studyclub = ("Data Science", "Robotics", "Multimedia", "Network")

print(studyclub)
listStudy = list(studyclub)

listStudy[1] = "web"

tuplestudy = tuple(listStudy)

print(tuplestudy)

