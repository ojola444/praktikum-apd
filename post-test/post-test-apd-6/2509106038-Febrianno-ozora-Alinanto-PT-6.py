import os
import time

user = {
   "admin" : "admin34",
   "user"  : "user1234"
}

echo = {
   "cost4" : ["Bell-Borne Geochelone", "crownless", "Fellian Beringal", "inferno rider"],
   "cost3" : ["chop chop", "chaserazor", "kerasaur", "hoochief"],
   "cost1" : ["fusion prism", "gulpuff", "excarat", "aero predator"]
}

preset_user = {}
cost_preset = {}
list_preset = []
list_cost = []
echo_cost = []
new_preset = []

modify_preset = ""
input_user = ""
username_input = ""
password_input = ""
admin_input = ""
new_user = ""
new_pass = ""


 
  
count_try = 0
role = 2
stop_modify = 0
total_cost = 0

## user login 
print("""ketik 1 untuk login
ketik 2 untuk regist
ketik 3 untuk log out""")
username_input = input("masukkan pilihan :")
while True :
  while role != 0 or role != 1 :
   if username_input == "2":
      username_input = input("masukkan nama baru anda : ")
      if username_input in user :
         print("user sudah ada")
         continue
      else :
         password_input = input("masukkan password baru anda : ")
         user[username_input] = (password_input) 
         print(f"selamat datang {new_user}!")  
   
   elif username_input == "3" :
      print("keluar dari program...")
      time.sleep(2)
      break

   elif username_input == "1" :

      username_input = input("masukkan nama anda : ")
      password_input = input("masukkan password anda : ")  

      if count_try >= 2 :
          print("terlalu banyak mencoba, silakan coba nanti")
          time.sleep(2)
          username_input = "out"
          count_try = 0
          break  
      
      elif username_input in user and password_input in user[username_input]:
          if username_input == "admin" :
             if username_input not in preset_user :
                preset_user[username_input] = {}
                cost_preset[username_input] = {}
             role = 0
             break
          else :
             print(f"selamat datang {username_input}")
             role = 1
             if username_input not in preset_user :
                preset_user[username_input] = {}
                cost_preset[username_input] = {}
             break
      
      else :
          count_try += 1
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"password/username salah, coba {3 - count_try} kali lagi ")

   else : 
      print("invalid")
      print("ketik 1 untuk login")
      print("ketik 2 untuk regist")
      print("ketik 3 untuk keluar")
      username_input = input("masukkan pilihan :")

   print("ketik 1 untuk login")
   print("ketik 2 untuk regist")
   print("ketik 3 untuk keluar")
   username_input = input("masukkan pilihan :")

  if role == 0 :
     print(f"selamat datang {username_input}")
     print("masuk fitur user (0)")
     print("masuk fitur admin (1)")
     print("atau log out (20)?")
     admin_input = int(input("masukkan pilihan : "))
 
  preset_siapa = preset_user[username_input]
  cost_siapa = cost_preset[username_input] 

##role 1 = user biasa, bisa buat preset echo
  if role == 1 or (admin_input == 0 and role == 0):
    print("echo cost 4 : ")
    for index,cost4 in enumerate(echo["cost4"]) :
        print(f"{index} : {cost4}")
    
    print("echo cost 3 : ")
    for index,cost3 in enumerate(echo["cost3"]) :
        print(f"{index + len(echo['cost4'])} : {cost3}")
    
    print("echo cost 1 : ")
    for index,cost1 in enumerate(echo["cost1"]) :
        print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
    
    print("tekan 20 untuk log out")
    print("tekan 50 untuk melihat preset yang ada")
    print("atau lanjut masukkan nomor echo untuk buat preset baru")
    input_user = int(input("masukkan pilihan : "))
    print("preset akan otomatis dibuat jika cost sudah 12 atau slot echo sudah 5")
    print("jika total cost preset sudah lebih 12, akan menghapus echo terbaru dan otomatis membuat preset baru")
    
    while input_user != 20 :
        #dibawah ini untuk buat buat preset baru
        while True :
         if input_user <= len(echo["cost4"]) - 1 :
            new_preset.append(echo["cost4"][input_user])
            echo_cost.append(4)
            total_cost += 4
            temporary_cost = 4
    
         elif input_user <= len(echo["cost4"] + echo["cost3"]) - 1 :
            new_preset.append(echo["cost3"][input_user - len(echo["cost3"])])
            echo_cost.append(3)
            total_cost += 3
            temporary_cost = 3
    
         elif input_user <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) - 1 :
            new_preset.append(echo["cost1"][input_user - len(echo["cost4"] + echo["cost3"])])
            echo_cost.append(1)
            total_cost += 1
            temporary_cost = 1
    
         elif input_user == 20 :
            print("log out..")
            break
         
         elif input_user == 21:
    
            if len(new_preset) < 1 and len(echo_cost) < 1:
               print("tidak ada echo yang dimasukkan")
    
            else :
               print("preset dibuat")
               cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
               preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset
               print("tekan 20 untuk log out")
               print("tekan 50 untuk melihat preset yang ada")

               new_preset = []
               echo_cost = []
               total_cost = 0

         #pengecekan sebelum masuk edit
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
            for key, value in preset_siapa.items():
             print(f"{key} : {value}")    
            modify_preset = int(input("mau edit/hapus preset? 14 untuk edit 15 untuk hapus"))
            break    
         elif input_user == 50 and len(preset_siapa) < 1 :

            print("kamu belum punya preset untuk dilihat")

         elif input_user == 50 :
            for key, value in preset_siapa.items():
               print(f"{key} : {value}")    
            modify_preset = int(input("mau edit/hapus preset? 14 untuk edit 15 untuk hapus : "))
            break
         
         else :
          print("input salah")
    
         if total_cost > 12:
            print("cost echo yang kamu masukkan sudah lebih dari 12")
            new_preset.pop()  
            echo_cost.pop()
    
            cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
            preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset

            new_preset = []
            echo_cost = []
            total_cost = 0
    
         elif total_cost == 12 :
            print("donee wak udah 12")
            cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
            preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset

            new_preset = []
            echo_cost = []
            total_cost = 0
    
         elif len(new_preset) == 5:
            print("echo kamu sudah 5")
            cost_siapa[f"new preset {len(preset_siapa)}"] = echo_cost
            preset_siapa[f"new preset {len(preset_siapa)}"] = new_preset
            
            new_preset = []
            echo_cost = []
            total_cost = 0
         print("tekan 21 untuk selesai buat preset")
         input_user = int(input("masukkan lagi echo yang mau dipilih : "))  
         
        if input_user == 20 :
           break
        
        #masuk edit 
        if modify_preset == 14 :
           while True :
            print("edit preset(0)")
            print("ingin tambah echo(1)")
            print("ganti nama preset(2)")
            print("")
            edit1 = int(input("atau selesai edit(12)? : "))
            # edit dipisah, nambah echo baru ke preset atau ubah echo di preset
            #yang ini nambahin echo
            if edit1 == 1 :
               while True :
                 
                 for key, value in preset_siapa.items():
                    if len(preset_siapa[key]) == 5 or sum(cost_siapa[key]) == 12:
                       print(f"{key} : tidak bisa ditambah")
                    else :
                       print(f"{key} : bisa ditambah")

                 edit1 = input(f"pilih preset (tekan 0 atau selain preset sebanyak dua kali untuk keluar) : ")
    
                 if stop_modify == 2:
                  print("opsi edit berhenti")
                  stop_modify = 0
                  break
                 
                 elif edit1 not in preset_siapa:
                  print("preset tidak ada")
                  stop_modify += 1
    
                 else : 
                    print(f"echo yang dipilih : {preset_siapa[edit1]}")
    
                    if len(preset_siapa[edit1]) == 5 :
                       print("penambahan echo tidak valid : slot penuh")
                    elif sum(cost_siapa[edit1]) == 12 :
                       print("penambahan echo tidak valid : cost penuh")
                    else :
                           print("echo cost 4 : ")
                           for index,cost4 in enumerate(echo["cost4"]) :
                               print(f"{index} : {cost4}")
                           
                           print("echo cost 3 : ")
                           for index,cost3 in enumerate(echo["cost3"]) :
                               print(f"{index + len(echo['cost4'])} : {cost3}")
                           
                           print("echo cost 1 : ")
                           for index,cost1 in enumerate(echo["cost1"]) :
                               print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
                               
                    edit2 = int(input("pilih echo yang dimasukkan : "))
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
                       total_cost += 3
                       temporary_cost = 3
  
                    else :
                       print("input salah")  
                    if total_cost > 12 :
                       print("echo yang dimasukkan butuh cost lebih")
                       print("gagal menambahkan")
                       preset_siapa[edit1].pop()
                       cost_siapa[edit1].pop()
                       total_cost -= temporary_cost
                    else :
                       print("berhasil menambahkan")
                       os.system('cls' if os.name == 'nt' else 'clear')

            elif edit1 == 2 :
               os.system('cls' if os.name == 'nt' else 'clear')
               while True :
                 
                 for key, value in preset_siapa.items():
                     print(f"{key} : {value}")

                 edit1 = input(f"pilih preset yang ingin di ganti namanya (tekan 0 atau selain preset sebanyak dua kali untuk berhenti edit) : ")
                 
                 if stop_modify == 2:
                    print("opsi edit berhenti")
                    stop_modify = 0
                    break
                 
                 elif edit1 not in preset_siapa :
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
                    


           #ini  mode edit 
            elif edit1 == 0 :
               os.system('cls' if os.name == 'nt' else 'clear')
               while True :
                 
                 for key, value in preset_siapa.items():
                     print(f"{key} : {value}")
    
                 edit1 = input(f"pilih preset yang ingin di edit (tekan 0 atau selain preset sebanyak dua kali untuk berhenti edit) : ")
           
                 if stop_modify == 2:
                    print("opsi edit berhenti")
                    stop_modify = 0
                    break
           
                 elif edit1 not in preset_siapa :
                    print("preset tidak ada")
                    stop_modify += 1
           
                 else :
                    print(f"echo yang dipilih : {preset_siapa[edit1]}")
                 
                    temp_preset_list = preset_siapa[edit1][:]
                    temp_cost_list = cost_siapa[edit1][:]
                    total_cost = sum(cost_siapa[edit1])    
           
                    edit2 = int(input("edit value yang ke? : "))
    
                    if edit2 > len(preset_siapa[edit1]) -1 :
                       os.system('cls' if os.name == 'nt' else 'clear')
                       print("echo tidak ada")
                       continue
    
                    print("echo cost 4 : ")
                    for index,cost4 in enumerate(echo["cost4"]) :
                        print(f"{index} : {cost4}")
                    
                    print("echo cost 3 : ")
                    for index,cost3 in enumerate(echo["cost3"]) :
                        print(f"{index + len(echo['cost4'])} : {cost3}")
                    
                    print("echo cost 1 : ")
                    for index,cost1 in enumerate(echo["cost1"]) :
                        print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
                              
                    final_edit = int(input(f"ubah {preset_siapa[edit1][edit2]} jadi? : "))
                   
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
                       continue 
                    os.system('cls' if os.name == 'nt' else 'clear')
    
            elif edit1 == 12 :
               print("edit echo selesai")
               total_cost = 0
               break
            
            else : 
               print("salah pilihan")
        #masuk mode hapus preset
        elif modify_preset == 15 :
          while True :
           
           if len(preset_siapa) < 1 :
              print("tidak ada preset lagi")
              print("echo cost 4 : ")
              for index,cost4 in enumerate(echo["cost4"]) :
                  print(f"{index} : {cost4}")
          
              print("echo cost 3 : ")
              for index,cost3 in enumerate(echo["cost3"]) :
                  print(f"{index + len(echo['cost4'])} : {cost3}")
              
              print("echo cost 1 : ")
              for index,cost1 in enumerate(echo["cost1"]) :
                  print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
              break
           
           for key, value in preset_siapa.items():
             print(f"{key} : {value}")
           edit1 = input(f"pilih preset yang ingin di hapus ( tekan 0 atau selain preset lebih dua kali untuk berhenti edit) : ")
           
           if stop_modify == 2:
              print("opsi hapus berhenti")
              stop_modify = 0
              break
           
           elif edit1 not in preset_siapa :
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
    
        else :
          os.system('cls' if os.name == 'nt' else 'clear')
          print("kamu ga milih keduanya")
          print("echo cost 4 : ")
          for index,cost4 in enumerate(echo["cost4"]) :
              print(f"{index} : {cost4}")
          
          print("echo cost 3 : ")
          for index,cost3 in enumerate(echo["cost3"]) :
              print(f"{index + len(echo['cost4'])} : {cost3}")
          
          print("echo cost 1 : ")
          for index,cost1 in enumerate(echo["cost1"]) :
              print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("echo cost 4 : ")
        for index,cost4 in enumerate(echo["cost4"]) :
            print(f"{index} : {cost4}")
        
        print("echo cost 3 : ")
        for index,cost3 in enumerate(echo["cost3"]) :
            print(f"{index + len(echo['cost4'])} : {cost3}")
        
        print("echo cost 1 : ")
        for index,cost1 in enumerate(echo["cost1"]) :
            print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
    
        input_user = int(input("pilih echo berdasarkan nomor, 50 untuk hapus/edit preset, atau 20 jika ingin log out : "))
        print("preset akan otomatis dibuat jika cost sudah 12 atau slot echo sudah 5")
        print("jika total cost preset sudah lebih 12, akan menghapus echo terbaru dan otomatis membuat preset baru")
        if input_user == 20 :
           new_preset = []
           echo_cost = []
           break  
#   role 0 = admin, bisa menambah atau menghapus echo untuk user nanti
  elif role == 0 and admin_input == 1: 
        print("echo cost 4 : ")
        for index,cost4 in enumerate(echo["cost4"]) :
            print(f"{index} : {cost4}")
        
        print("echo cost 3 : ")
        for index,cost3 in enumerate(echo["cost3"]) :
            print(f"{index + len(echo['cost4'])} : {cost3}")
        
        print("echo cost 1 : ")
        for index,cost1 in enumerate(echo["cost1"]) :
            print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")

        admin_input = int(input("ingin tambah(0) echo, hapus(1) echo, atau log out(20)? : "))
        while admin_input != 20 :
          #opsi admin = nambahkan echo sesuai dengan cost
          if admin_input == 0 :
             while True :  
               os.system('cls' if os.name == 'nt' else 'clear')
               print("echo cost 4 : ")
               for index,cost4 in enumerate(echo["cost4"]) :
                   print(f"{index} : {cost4}")
        
               print("echo cost 3 : ")
               for index,cost3 in enumerate(echo["cost3"]) :
                   print(f"{index + len(echo['cost4'])} : {cost3}")
        
               print("echo cost 1 : ")
               for index,cost1 in enumerate(echo["cost1"]) :
                   print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")

               admin_input = int(input("tambah echo cost berapa? (tekan 5 untuk jika selesai) : "))

               if admin_input == 5 :
                  ("selesai menambahkan ")
                  break  

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

          #hapus echo 
          elif admin_input == 1 :
           while True :  
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(echo["cost4"]) < 2 or len(echo["cost3"]) < 2 or len(echo["cost1"]) < 2 :
               print("opsi hapus berhenti")
               print("masing masing echo dgn cost berbeda setidaknya punya 1 echo")
               break
            print("echo cost 4 : ")
            for index,cost4 in enumerate(echo["cost4"]) :
               print(f"{index} : {cost4}")
        
            print("echo cost 3 : ")
            for index,cost3 in enumerate(echo["cost3"]) :
                print(f"{index + len(echo['cost4'])} : {cost3}")
            
            print("echo cost 1 : ")
            for index,cost1 in enumerate(echo["cost1"]) :
                print(f"{index + len(echo['cost4'] + echo['cost3'])} : {cost1}")
               
            admin_input= int(input("masukkan nomor yang ingin dihapus (20 untuk selesai) : "))
            
            if admin_input <= len(echo["cost4"]) - 1 :
               echo["cost4"].pop(admin_input)  

            elif admin_input <= len(echo["cost4"] + echo["cost3"]) -1 :
               echo["cost3"].pop(admin_input - len(echo["cost3"]))  

            elif admin_input <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) -1 :
               echo["cost1"].pop(admin_input - len(echo["cost3"] + echo["cost1"]))  

            elif admin_input == 20 :
               print("selesai hapus echo")
               break  

            else :
               print("input salah")  

          elif admin_input == 20 :
             print("log out admin")
             break
          
          admin_input = int(input("ingin tambah(0) echo, hapus(1) echo, atau log out(20)? : "))  
          
  elif username_input == "3" :
      os.system('cls' if os.name == 'nt' else 'clear')
      break
  
  elif admin_input == 20 :
     role = 2 
  
  else : 
     print("input invalid")
     print("masuk fitur user (0)")
     print("masuk fitur admin (1)")
     print("atau log out (20)?")
     admin_input = int(input("masukkan pilihan : "))
     
  
  os.system('cls' if os.name == 'nt' else 'clear')
#   preset_user = {}
#   cost_preset = {}
  print("log out..")
  print("ketik 1 untuk login")
  print("ketik 2 untuk regist")
  print("ketik 3 untuk keluar")
  username_input = input("masukkan pilihan :") 
            
          
             
#kayanya berlebihan