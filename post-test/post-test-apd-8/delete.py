import os
from read import listPreset, terpilih

def hapusPreset(preset_siapa, cost_siapa) :
    stop_modify = 0
    while True :

      if len(preset_siapa) < 1:
         os.system('cls' if os.name == 'nt' else 'clear')
         print("tidak punya preset")
         return

      if stop_modify == 2:
         print("opsi hapus berhenti")
         stop_modify = 0
         break
      
      listPreset(preset_siapa)

      print("masukkan nama echo yang ingin di edit")
      print("tekan bebas selain preset sebanyak 2 kali untuk keluar")
      edit1 = input(f"masukkan pilihan : ") 
      
      if edit1 not in preset_siapa :
        os.system('cls' if os.name == 'nt' else 'clear')
        print("preset tidak ada")
        stop_modify += 1
      else : 
         terpilih(edit1, preset_siapa[edit1])
         edit2 = int(input("yakin ingin hapus preset?(0 untuk ya) :"))
         if edit2 == 0 :
            del preset_siapa[edit1]
            del cost_siapa[edit1]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("hapus preset berhasil")
         else :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("cancel penghapusan :")