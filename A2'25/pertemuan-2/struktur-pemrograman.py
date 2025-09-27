print("=== INTEGER ===")

nomor = 12
nomor1 = 13
print(nomor + nomor1)

print("===  FLOAT ===")

desimal = 0.12
desimal1 = 12.12

print(desimal + desimal1)

print("=== STRING ===")

kata = "halo"
kata1 = """apa benar ikan berkepala lele itu ada
tulung penejelasannya"""
print("patang""puluh""patang")
print("patang" + "puluh" + "patang")
indexx = "iki dadaku kelip kelip jon"

#menampilkan index ke-3
print(indexx[3])
#menampilkan index ke-0 hingga ke-3
print(indexx[0:3])
#menampilkan seluruhnya, tetapi dimulai dari index ke-5
print(indexx[5:])
#menampilkan hanya sampai index ke-8
print(indexx[:8])

print("=== BOOlEAN ===")

trumin = True
falsemin = False

print("=== LIST ===")

buah = ["jambu", "mangga", "apel", "pir"]
print(buah)
print(buah[0])

print("=== TUPLE ===")

tuple = ('Lian', 19, True, 'APD')
print(tuple[0])
print(tuple[2])

print("=== DICTIONARY ===")

warna = {
'warna1' : 'merah',
'warna2' : 'kuning',
'warna3' : 'hijau'
}
print(warna['warna1'])
print(warna['warna3'])

print("=== INPUT MANUAL ===")

masukan = input("masukkan terserah mau apa, tapi tipe datanya bakal default string : ")
print(masukan)