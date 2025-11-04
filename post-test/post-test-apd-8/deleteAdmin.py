import os
from read import listEcho
from variable import echo
import option

def hapusListEcho() :
   os.system('cls' if os.name == 'nt' else 'clear')
   if len(echo["cost4"]) < 2 or len(echo["cost3"]) < 2 or len(echo["cost1"]) < 2 :
      print("opsi hapus berhenti")
      print("masing masing echo dgn cost berbeda setidaknya punya 1 echo")
      return
   
   listEcho()

   try :
     admin_input= int(input("masukkan nomor yang ingin dihapus (20 untuk selesai) : "))
   except ValueError :
      print("echo tidak ada")
   
   if admin_input <= len(echo["cost4"]) - 1 :
      echo["cost4"].pop(admin_input)  

   elif admin_input <= len(echo["cost4"] + echo["cost3"]) -1 :
      echo["cost3"].pop(admin_input - len(echo["cost4"]))  

   elif admin_input <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) -1 :
      echo["cost1"].pop(admin_input - len(echo["cost3"] + echo["cost4"]))  

   elif admin_input == 20 :
      print("selesai hapus echo")
      return
   
   else :
      print("input salah")  

   lanjut = option.lanjutOrTak()

   if lanjut :
      hapusListEcho()

   else :
      print("keluar dari opsi...")
      return