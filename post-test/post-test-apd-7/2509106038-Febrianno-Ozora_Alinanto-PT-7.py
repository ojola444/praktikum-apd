import os
import time

user = {
   "admin" : ["admin34"],
   "user"  : ["user1234"]
}

echo = {
   "cost4" : ["Bell-Borne Geochelone", "crownless", "Fellian Beringal", "inferno rider"],
   "cost3" : ["chop chop", "chaserazor", "kerasaur", "hoochief"],
   "cost1" : ["fusion prism", "gulpuff", "excarat", "aero predator"]
}

preset_user = {}
cost_preset = {}

echo_cost = []
new_preset = []
total_cost = 0

username_input = ""
input_user = ""
admin_input = ""

role = 2
stop_modify = 0


def listEcho() :
    print("---------------------echo cost 4-----------------------")
    for index,cost4 in enumerate(echo["cost4"]) :
        print(f"{index} : {cost4}")

    print("-------------------------------------------------------")
    print("\n")
    
    print("---------------------echo cost 3-----------------------")
    for index,cost3 in enumerate(echo["cost3"]) :
        print(f"{index + len(echo['cost4'])} : {cost3}")
    print("-------------------------------------------------------")
    print("\n")
    
    print("---------------------echo cost 1-----------------------")
    for index,cost1 in enumerate(echo["cost1"]) :
        print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
    print("-------------------------------------------------------")
    print("\n")

def listPreset(punya_user) :
   for key, value in punya_user.items():
            print(f"{key} : {value}")

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

def loginn() :
    count_try = 0
    global role
    global username_input

    print("ketik 1 untuk login")
    print("ketik 2 untuk regist")
    print("ketik 3 untuk keluar")
    username_input = input("masukkan pilihan :")
    if username_input == "2":
      try :
       username_input = input("masukkan nama baru anda : ")
       if username_input == "" or  username_input == " " * len(username_input):
          raise ValueError("nama tidak boleh kosong atau spasi saja")
      except ValueError as kosong :
         print(kosong)
       
      if username_input in user :
         print("user sudah ada")
      else :
         try :
          password_input = input("masukkan password baru anda : ")
          if password_input == "" or  password_input == " " * len(password_input):
             raise ValueError("password tidak boleh kosong atau spasi saja")
          else :
             user[username_input] = [password_input]
             print(f"selamat datang {username_input}")
         except ValueError as kosong :
            print(kosong) 
            

    elif username_input == "3" :
      print("keluar dari program...")
      time.sleep(2)
      exit()
    elif username_input == "1" :
      while True :

        if count_try == 3 :
            print("terlalu banyak mencoba, silakan coba nanti")
            time.sleep(2)
            exit()  

        username_input = input("masukkan nama anda : ")
        password_input = input("masukkan password anda : ")  

        if username_input in user and (password_input in user[username_input]):
            count_try = 0
            if username_input == "admin" :
                role = 0
                if username_input not in preset_user :
                    preset_user[username_input] = {}
                    cost_preset[username_input] = {}
              
            else :
                print(f"selamat datang {username_input}")
                role = 1
                if username_input not in preset_user :
                    preset_user[username_input] = {}
                    cost_preset[username_input] = {}
            return username_input, role
            
        
        else :
            count_try += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"password/username salah, coba {3 - count_try} kali lagi ")

    else : 
        print("invalid")

## fitur user

#buat preset
def buatPreset(preset_siapa, cost_siapa) :
    
    global echo_cost
    global new_preset
    global total_cost
    global role
    total_cost = 0
    listEcho()
    while True :
        print("21 untuk selesai buat preset")
        print("50 untuk selesai")
        print("nomor echo untuk menambahkan echo ke preset baru")
        try:
            input_user = int(input("masukkan pilihan : "))
            print("\n")
        except ValueError :
           print("input tak valid")

        if input_user <= len(echo["cost4"]) - 1 :
           new_preset.append(echo["cost4"][input_user])
           echo_cost.append(4)
           total_cost += 4

        elif input_user <= len(echo["cost4"] + echo["cost3"]) - 1 :
           new_preset.append(echo["cost3"][input_user - len(echo["cost3"])])
           echo_cost.append(3)
           total_cost += 3
  
        elif input_user <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) - 1 :
           new_preset.append(echo["cost1"][input_user - len(echo["cost4"] + echo["cost3"])])
           echo_cost.append(1)
           total_cost += 1
        
        elif input_user == 21:   
         
           if len(new_preset) < 1 and len(echo_cost) < 1:
              os.system('cls' if os.name == 'nt' else 'clear')
              listEcho ()
              print("tidak ada echo yang dimasukkan")    

           else :
              os.system('cls' if os.name == 'nt' else 'clear')
              cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
              preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset
              listEcho()
              print("preset dibuat")
              new_preset = []
              echo_cost = []
              total_cost = 0    

        elif input_user == 50 and len(new_preset) > 0 :
           input_user = int(input("kamu punya preset belum disimplan, tekan 1 untuk menyimpan "))    
           if input_user == 1 :
             cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
             preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset
    
             new_preset = []
             echo_cost = []
             total_cost = 0
           else :
             new_preset = []
             echo_cost = []
             total_cost = 0 
           os.system('cls' if os.name == 'nt' else 'clear')
           print("buat preset selesai ")
           print("keluar dari opsi...")
           break

        elif input_user == 50 and len(new_preset) == 0 :
           os.system('cls' if os.name == 'nt' else 'clear')
           print("keluar dari opsi...")
           break
        
        else :
         print("input salah")  

        if total_cost > 12:
           os.system('cls' if os.name == 'nt' else 'clear')
           listEcho()
           print("cost echo yang kamu masukkan sudah lebih dari 12")
           new_preset.pop()  
           echo_cost.pop()    
           cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
           preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset    
           new_preset = []
           echo_cost = []
           total_cost = 0    

        elif total_cost == 12 :
           os.system('cls' if os.name == 'nt' else 'clear')
           listEcho()
           print("donee wak udah 12")
           cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
           preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset   
           new_preset = []
           echo_cost = []
           total_cost = 0    

        elif len(new_preset) == 5:
           os.system('cls' if os.name == 'nt' else 'clear')
           listEcho()
           print("echo kamu sudah 5")
           cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
           preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset
           
           new_preset = []
           echo_cost = []
           total_cost = 0
        

#lihat preset          
def lihatPreset(preset_siapa) :
   if len(preset_siapa) < 1 :
      print("belum ada preset yang ditampilkan")
   else :
      print(f"kamu punya {len(preset_user[username_input])} preset")
      print("\n")
      listPreset(preset_siapa)

# tambah echo di preset
def tambahEchoPreset(preset_siapa, cost_siapa) :
    
    stop_modify = 0
    temporary_cost = 0
    count = 0

    while True :

        for key in preset_siapa:
           
           if len(preset_siapa[key]) == 5 or sum(cost_siapa[key]) == 12:
              print(f"{key} : tidak bisa ditambah")
              count += 1

           else :
              print(f"{key} : bisa ditambah")

        if len(preset_siapa) == count :
         os.system('cls' if os.name == 'nt' else 'clear')
         print("tidak ada preset yang bisa ditambah")
         count = 0
         break

        if stop_modify == 2:
         print("opsi edit berhenti")
         stop_modify = 0
         os.system('cls' if os.name == 'nt' else 'clear')
         break

        print("masukkan nama echo yang ingin di edit")
        print("tekan bebas selain preset sebanyak 2 kali untuk keluar")
        edit1 = input(f"masukkan pilihan : ") 

        if edit1 not in preset_siapa:
         print("preset tidak ada")
         stop_modify += 1

        else : 
           print(f"echo yang dipilih : {preset_siapa[edit1]}")

           if len(preset_siapa[edit1]) == 5 :
              print("penambahan echo tidak valid : slot penuh")

           elif sum(cost_siapa[edit1]) == 12 :
              print("penambahan echo tidak valid : cost penuh")

           else :
                  listEcho()

           try :          
              edit2 = int(input("pilih echo yang dimasukkan : "))
           except ValueError :
              print("input salah")

           else :
              total_cost = sum(cost_siapa[edit1])
   
              if edit2 <= len(echo["cost4"]) -  1:
                 preset_siapa[edit1].append(echo["cost4"][edit2])
                 cost_siapa[edit1].append(4)
                 total_cost += 4
                 temporary_cost = 4
   
              elif edit2 <= len(echo["cost4"] + echo["cost3"]) -  1:
                 preset_siapa[edit1].append(echo["cost3"][edit2 - len(echo["cost3"])])
                 cost_siapa[edit1].append(3)
                 total_cost += 3
                 temporary_cost = 3
   
              elif edit2 <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) -  1:
                 preset_siapa[edit1].append(echo["cost1"][edit2 - len(echo["cost4"] + echo["cost3"])])
                 cost_siapa[edit1].append(1)
                 total_cost += 1
                 temporary_cost = 1
   
              else :
                 print("input salah")  
   
              if total_cost > 12 :
                 print("echo yang dimasukkan butuh cost lebih")
                 print("gagal menambahkan")
                 preset_siapa[edit1].pop()
                 cost_siapa[edit1].pop()
                 total_cost -= temporary_cost
   
              else :
                 os.system('cls' if os.name == 'nt' else 'clear')
                 print("berhasil menambahkan")

#edit echo di preset
def editEchoPreset (preset_siapa, cost_siapa) :
    os.system('cls' if os.name == 'nt' else 'clear')

    stop_modify = 0
    while True :

        if stop_modify == 2:
           print("opsi edit berhenti")
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
           print(f"echo yang dipilih : {preset_siapa[edit1]}")
        
           temp_preset_list = preset_siapa[edit1][:]
           temp_cost_list = cost_siapa[edit1][:]
           total_cost = sum(cost_siapa[edit1])        
           try :
            edit2 = int(input("edit value yang ke? : "))
           except ValueError :
              print("input salah")

           else :

              if edit2 > len(preset_siapa[edit1]) -1 :
                 os.system('cls' if os.name == 'nt' else 'clear')
                 print("echo tidak ada")
                 continue
              print("echo cost 4 : ")

              listEcho()

              try :          
               final_edit = int(input(f"ubah {preset_siapa[edit1][edit2]} jadi? : "))
              except ValueError :
                 print("input salah")
                 
              else : 
          
                if final_edit > len(echo["cost4"] + echo["cost3"] + echo["cost1"]) - 1 :
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print("input tidak tersedia")    
                  continue
                
                elif final_edit <= len(echo["cost4"]) - 1 :
                   
                   preset_siapa[edit1][edit2] = echo["cost4"][final_edit]
                   total_cost -= cost_siapa[edit1][edit2]
                   cost_siapa[edit1][edit2] = 4
                   temporary_cost = 4     
                elif final_edit <= len(echo["cost4"] + echo["cost3"]) - 1 :
                   
                   preset_siapa[edit1][edit2] = echo["cost3"][final_edit - len(echo["cost4"])]
                   total_cost -= cost_siapa[edit1][edit2]
                   cost_siapa[edit1][edit2] = 3
                   temporary_cost = 3    
                elif final_edit <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) - 1 :
                   
                   preset_siapa[edit1][edit2] = echo["cost1"][final_edit - len(echo["cost3"] + echo["cost4"])]
                   total_cost -= cost_siapa[edit1][edit2]
                   cost_siapa[edit1][edit2] = 1
                   temporary_cost = 1
                 
                
                total_cost += temporary_cost    
                if total_cost > 12 :
                   print("error : cost sudah melebihi 12")
                   preset_siapa[edit1] = temp_preset_list
                   cost_siapa[edit1] = temp_cost_list
                   
                else :
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print("edit echo berhasil")

#ubah nama preset
def ubahNamaPreset(preset_siapa, cost_siapa) :
   os.system('cls' if os.name == 'nt' else 'clear')
   stop_modify = 0
   while True :
                 
      listPreset(preset_siapa)

      if stop_modify == 2:
         print("opsi edit berhenti")
         stop_modify = 0
         break

      print("masukkan nama echo yang ingin di edit")
      print("tekan bebas selain preset sebanyak 2 kali untuk keluar")
      edit1 = input(f"masukkan pilihan : ") 
      
      if edit1 not in preset_siapa :      
         os.system('cls' if os.name == 'nt' else 'clear')
         print("preset tidak ada")
         stop_modify += 1

      else :
         print(f"preset yang dipilih : {preset_siapa[edit1]}")
         edit2 = input("ubah jadi? : ")
         if edit2 in preset_siapa :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("preset dengan nama yang sama sudah ada")
         else : 
            os.system('cls' if os.name == 'nt' else 'clear')
            preset_siapa[edit2] = preset_siapa.pop(edit1)
            cost_siapa[edit2] = cost_siapa.pop(edit1)
            print("ubah nama berhasil")

#hapus preset
def hapusPreset(preset_siapa, cost_siapa) :
    stop_modify = 0
    while True :
           
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
         print(f"preset yang dipilih : {preset_siapa[edit1]}")
         edit2 = int(input("yakin ingin hapus preset?(0 untuk ya) :"))
         if edit2 == 0 :
            del preset_siapa[edit1]
            del cost_siapa[edit1]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("hapus preset berhasil")
         else :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("cancel penghapusan :")

## opsi admin

# tambah echo baru ke list
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

   lanjut = lanjutOrTak()

   if lanjut :
      echoBaru()

   else :
      print("keluar dari opsi...")
      return 

      

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
      echo["cost3"].pop(admin_input - len(echo["cost3"]))  

   elif admin_input <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) -1 :
      echo["cost1"].pop(admin_input - len(echo["cost3"] + echo["cost1"]))  

   elif admin_input == 20 :
      print("selesai hapus echo")
      return
   
   else :
      print("input salah")  

   lanjut = lanjutOrTak()

   if lanjut :
      hapusListEcho()

   else :
      print("keluar dari opsi...")
      return

def menu(presetTerpilih, costTerpilih) :
   global role
   print("\n")
   print("-----Menu-----")
   print("[1] tampilkan preset")
   print("[2] buat preset baru")
   print("[3] tambah echo di preset")
   print("[4] edit echo di preset")
   print("[5] ubah nama preset")
   print("[6] hapus perset")
   if role == 0 :
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
      buatPreset(presetTerpilih, costTerpilih)

   elif pilihan == "3" :
      tambahEchoPreset(presetTerpilih, costTerpilih)

   elif pilihan == "4" :
      editEchoPreset(presetTerpilih, costTerpilih)
    
   elif pilihan == "5" :
      ubahNamaPreset(presetTerpilih, costTerpilih)

   elif pilihan == "6" :
      hapusPreset(presetTerpilih, costTerpilih)

   elif pilihan == "7" and role == 0 :
      echoBaru()

   elif pilihan == "8" and role == 0 :
      hapusListEcho()

   elif pilihan == "9" :
      role = 2 
      return role 
   
   else :
      print("pilihan tidak ada")
       
if __name__ == "__main__":
        while (True):
            if role == 0 or role == 1 :
               menu(preset_user[username_input], cost_preset[username_input])
            else : 
               loginn()

  