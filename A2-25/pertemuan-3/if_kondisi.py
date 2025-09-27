##  KONDISI IF

## CONTOH 
# angka = 3

# if angka > 5 :
#     print("angka lebih besar 5")

# output kosong karena kondisi salah

# cuaca = "cerah"

## kondisi IF ELSE
## CONTOH
# if cuaca == "hujan" :
#    print("dirumah aja")

# else :
#    print("nongkrong kalo mau")

# output = "nongkrong kalau mau"

# nilai = 70

# if nilai >= 70 :
#     print("lulus")

# else :
#     print("tak luluus")

#  output = "lulus"   

# ##KONDISI ELSE IF / ELIF
# ##CONTOH

# cuaca = "hujan"

# if cuaca == "hujan" :
#    print("dirumah aja")

# elif cuaca == "mendung" :
#    print("makan mie")

# else :
#    print("nongkrong")
# output = dirumah aja

# usia = int(input("masukkan umur kmu :"))

# if usia <=13 :
#     print("anak anak")
# elif usia <= 18 :
#     print("remaja")
# elif usia <= 40 :
#     print("dewasa")
# else :
#     print("tua")

# nilai = int(input("masukkan nilai kamu : "))

# if nilai >= 90 :
#     print("a")
# elif nilai >= 70 :
#     print("b")
# elif nilai >= 60 :
#     print("c")
# else :
#     print("d")


# ## TERNARY OPERATOR

# nilai = 80
# status = "lulus" if nilai >= 70 else "tidak lulus"
# print(status)

# ## NESTED IF

# a = 2
# b = 1
# c = 3

# if a < b :
#     if a < c :
#         print("a paling kecil")

# elif a < c :
#     print("c paling besar")

# else :
#     print("a lebih besar")


# ##STUDI kASUS 1

# tinggi = int(input("masukkan tinggi"))

# check = "boleh masuk" if tinggi > 145 else "tidak boleh masuk"

# print(check)

# ##STUDI KASUS 2

# pembelian = int(input("belanja kmu : "))

# if pembelian >= 100000 :
#     diskon = pembelian * 0.20
#     print("dapat diskon 20 persen")
#     print(pembelian - diskon)

# elif pembelian >= 50000 :
#     diskon = pembelian * 0.15
#     print("dapat diskon 15 persen")
#     print(pembelian - diskon)

# else :
#     print("gadapat diskon")

nilai = int(input("masukkan nilai kmu : "))
kelas = str(input("masukkan kelas kamu : "))

if nilai >= 80 and kelas == "A" or kelas == "a" :
    print("IPK 4")

elif nilai >= 80 and kelas == "B" or kelas == "b" :
    print("IPK 3")

else :
    print("IPK 2")