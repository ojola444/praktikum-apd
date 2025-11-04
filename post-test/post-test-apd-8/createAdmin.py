import os
import option
from read import listEcho
from variable import echo

def echoBaru ():
   os.system('cls' if os.name == 'nt' else 'clear')
               
   listEcho()
   try :
     admin_input = int(input("tambah echo cost berapa? (tekan 5 untuk jika selesai) : "))
   except ValueError :
      print("input salah, coba lagi la")
   if admin_input == 5 :
      ("selesai menambahkan ")
      return

   admin_mod = input("masukkan nama echo : ")  
   if admin_input == 4 :
      echo["cost4"].append(admin_mod)
      print(f"berhasil menambahkan {admin_mod} ke echo cost 4")
      
   elif admin_input == 3 :
      echo["cost3"].append(admin_mod)
      print(f"berhasil menambahkan {admin_mod} ke echo cost 3")  
   elif admin_input == 1 :
      echo["cost1"].append(admin_mod)
      print(f"berhasil menambahkan {admin_mod} ke echo cost 1")
   
   else :
      print(f"echo cost {admin_input} tidak ada ") 

   lanjut = option.lanjutOrTak()

   if lanjut :
      echoBaru()

   else :
      print("keluar dari opsi...")
      return 
