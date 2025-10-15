import os
import time

user = "ozora"
pass_user = "038"

username_input = ""
password_input = ""
count_try = 0
role = 2

sisi1 = 0
sisi2 = 0
sisi3 = 0

print("login user")
print("ketik out jika ingin keluar")

while True :
   username_input = input("masukkan nama  :")

   if  username_input == "out" or username_input == "Out" :
      print("keluar dari program...")
      time.sleep(2)
      break
    
   password_input = input("masukkan password anda : ")  
   if count_try >= 5 :
       print("terlalu banyak mencoba, silakan coba nanti")
       time.sleep(2)
       username_input = "out"
       count_try = 0
       break  
   
   elif username_input == user and password_input == pass_user :
       print(f"selamat datang {user}")
       count_try = 0
       role = 1
   
   else :
       count_try += 1
       print(f"password salah, coba {6 - count_try} kali lagi ")
       time.sleep(0.5)
   
   if role == 1:
     while True:

      sisi1 = int(input("masukkan sisi pertama (tekan nomor 0 untuk log out) : "))
      if sisi1 ==  0 :
         os.system('cls' if os.name == 'nt' else 'clear')
         break
   
      sisi2 = int(input("masukkan sisi kedua : "))
      if sisi2 == 0 :
         os.system('cls' if os.name == 'nt' else 'clear') 
         print("log out...")
         break
       
      sisi3 = int(input("masukkan sisi ketiga : "))  
  
      setengah_keliling = (sisi1 + sisi2 + sisi3) / 2
      luas = (setengah_keliling * (setengah_keliling - sisi1) * (setengah_keliling - sisi2) * (setengah_keliling - sisi3)) ** 0.5
   
      if sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1 :
       print("bukan segitiga")
       print("Note : masukkan angka 0 untuk log out")
      
      elif sisi1 == sisi2 and sisi2 == sisi3 :
       print("segitiga sama sisi")
   
      elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3 :
       print("segitiga sama kaki")
       
      else :
       print("segitiga sembarang")
   
      print(f"luas : {luas}")
   role = 2
   
   
   
   
