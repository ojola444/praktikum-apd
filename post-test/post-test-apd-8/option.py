def lanjutOrTak() :
   print("1, untuk lanjut")
   print("angka atau huruf selain 1 untuk keluar")
   try : 
      opsi = int(input("masukkan pilihan"))
   except ValueError:
      return False
   
   if opsi == 1 :
      return True
   else :
      return False