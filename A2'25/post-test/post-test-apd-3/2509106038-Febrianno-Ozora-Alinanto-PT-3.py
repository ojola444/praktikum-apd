sisi1 = int(input("masukkan sisi pertama : "))
sisi2 = int(input("masukkan sisi kedua : "))
sisi3 = int(input("masukkan sisi ketiga : "))

setengah_keliling = (sisi1 + sisi2 + sisi3) / 2
luas = (setengah_keliling * (setengah_keliling - sisi1) * (setengah_keliling - sisi2) * (setengah_keliling - sisi3)) ** 0.5

if sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1 :
    print("bukan segitiga")
    
elif sisi1 == sisi2 and sisi2 == sisi3 :
     print("segitiga sama sisi")
     print(f"luas : {luas}")

elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3 :
     print("segitiga siku-suku")
     print(f"luas : {luas}")

else :
     print("segitiga sembarang")
     print(f"luas : {luas}")



