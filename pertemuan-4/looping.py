# for looping
# for i in range(10) :
#     print(i)


# nama  = ['v2', 'sans']

# for j in nama :
#     print(j)


# while looping
# jawab = "ya"
# hitung = 0

# while (jawab == "ya") :
#     hitung += 1
#     jawab = input("ulangi lagi : ")


# print(f"total jawwab {hitung}")

# cuaca = "hujan"

# while (cuaca == "hujan" or cuaca == "Hujan") :
#     print("jangan keluar rumah dulu")
#     cuaca = input("sekarang gimana wak : ")

# print("pergi keluar rumah")

# angka = 10

# while (angka > 1) :
#     print(angka)
#     angka -= 2

# for i in range(1,5) :
#     for j in range(1,3):
#         print(f"{i} x {j} = {i * j}")
#     print ()

# angka = [2, 5, 8, 12, 7, 20]

# print("cari angka lebih dari 10")

# for i in angka :
#     print(f"memeriksa angka {i}")
#     if i > 10 :
#         print(f"{i} lebih besar dari 10")
#         break

# print("selesai")

# nomor = int(input("masukkan nomor : "))

# for i in range (1, nomor) :
#     if i % 2 != 0:
#         continue
#     print(f'angka genap ditemukan yaitu : {i}')

# print("program selese")

# nomor = int(input("masukkan nomor : "))
# genap = 0

# for i in range (1, nomor + 1) :
#     if nomor % i != 0:
#         continue
#     print(f'angka bisa dibagi dengan {nomor} ditemukan yaitu : {i}')
#     genap += 1

# print("program selese")

# if genap == 2 :
#     print("nomor prima")

# else :
#     print("bukan nomor prima")

# list comprehension (for loop dalam satu baris)

# kuadrat = [i**2 for i in range(1,6)]
# print(kuadrat)

# angka_genap = [x for x in range(1,11) if x % 2 == 0]

# for x in range(1,11) :
#     if x % 2 == 0 :
#         print(x)

for i in range(1, 6):
    print(" " * i * "*")
