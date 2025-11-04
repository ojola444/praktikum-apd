import loginAndRegist
from read import lihatPreset
import create
import createAdmin
import update
import delete
import deleteAdmin
import variable
from variable import preset_user, cost_preset, user


def menu(presetTerpilih, costTerpilih) :
   
   print("\n")
   print("-----Menu-----")
   print("[1] tampilkan preset")
   print("[2] buat preset baru")
   print("[3] tambah echo di preset")
   print("[4] edit echo di preset")
   print("[5] ubah nama preset")
   print("[6] hapus perset")
   if variable.role == 0 :
    print("[7] (opsi admin) tambah echo baru di list echo")
    print("[8] (opsi admin) hapus echo di list echo ")

   print("[9] log out")
   print("[0] keluar dan log out ")
   pilihan = input("masukkan nomor : ")
   print("\n")

   if pilihan == "0" :
      exit()

   elif pilihan == "1" :
      lihatPreset(presetTerpilih)

   elif pilihan == "2" :
      create.buatPreset(presetTerpilih, costTerpilih)

   elif pilihan == "3" :
      update.tambahEchoPreset(presetTerpilih, costTerpilih)

   elif pilihan == "4" :
      update.editEchoPreset(presetTerpilih, costTerpilih)
    
   elif pilihan == "5" :
      update.ubahNamaPreset(presetTerpilih, costTerpilih)

   elif pilihan == "6" :
      delete.hapusPreset(presetTerpilih, costTerpilih)

   elif pilihan == "7" and variable.role == 0 :
      createAdmin.echoBaru()

   elif pilihan == "8" and variable.role == 0 :
      deleteAdmin.hapusListEcho()

   elif pilihan == "9" :
      variable.role = 2 
      return variable.role 
   
   else :
      print("pilihan tidak ada")
       
if __name__ == "__main__":
        while (True):
            if variable.role == 0 or variable.role == 1 :
               menu(preset_user[variable.username_input], cost_preset[variable.username_input])
            else : 
               loginAndRegist.loginn()