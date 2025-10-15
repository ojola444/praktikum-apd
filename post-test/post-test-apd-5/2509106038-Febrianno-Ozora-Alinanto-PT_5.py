import os
import time

echo4 = ["Bell-Borne Geochelone", "crownless", "Fellian Beringal", "inferno rider"]
echo3 = ["chop chop", "chaserazor", "kerasaur", "hoochief"]
echo1 = ["fusion prism", "gulpuff", "excarat", "aero predator"]

list_preset = []
list_cost = []
echo_cost = []
new_preset = []

user = "user"
pass_user = "user1234"
new_user = ""
new_pass = ""
admin = "admin"
admin_pass = "admin34"

modify_preset = ""
input_user = ""
username_input = ""
password_input = ""
admin_input = ""

count_try = 0
role = 2
stop_modify = 0
total_cost = 0

## user login 
print("login user")
print("ingin daftar? ketik regist untuk buat akun baru")
print("ketik out jika ingin keluar")
username_input = input("masukkan nama  :")
while True :
  while role != 0 or role != 1 :
   if username_input == "regist" or username_input == "Regist":
      username_input = input("masukkan nama baru anda : ")
      password_input = input("masukkan password baru anda : ")
      new_user = username_input
      new_pass = password_input  
      print(f"selamat datang {new_user}!")  
      username_input = input("masukkan nama :")
 
   elif username_input == "out" or username_input == "Out" :
      print("keluar dari program...")
      time.sleep(2)
      break
    
   password_input = input("masukkan password anda : ")  
   if count_try >= 2 :
       print("terlalu banyak mencoba, silakan coba nanti")
       time.sleep(2)
       username_input = "out"
       count_try = 0
       break  
   
   elif username_input == user and password_input == pass_user :
       print(f"selamat datang {user}")
       role = 1
       break
 
   elif username_input == new_user and password_input == new_pass :
       print(f"selamat datang {new_user}")
       role = 1
       break
   
   elif username_input == admin and password_input == admin_pass :
       print(f"selamat datang {admin}")
       role = 0
       break
   
   else :
       count_try += 1
       print(f"password salah, coba {3 - count_try} kali lagi ")
       username_input = input("masukkan nama (ketik regist untuk daftar):")

##role 1 = user biasa, bisa buat preset echo
  if role == 1 :
    print("echo cost 4 : ")
    for index,cost4 in enumerate(echo4) :
        print(f"{index} : {cost4}")
    
    print("echo cost 3 : ")
    for index,cost3 in enumerate(echo3) :
        print(f"{index + len(echo4)} : {cost3}")
    
    print("echo cost 1 : ")
    for index,cost1 in enumerate(echo1) :
        print(f"{index + len(echo4 + echo3)} : {cost1}")
    
    input_user = int(input("masukkan echo yang dipilih (tekan 20 untuk log out) : "))
    print("preset akan otomatis dibuat jika cost sudah 12 atau slot echo sudah 5")
    print("jika total cost preset sudah lebih 12, akan menghapus echo terbaru dan otomatis membuat preset baru")
    
    while input_user != 20 :
        #dibawah ini untuk buat buat preset baru
        while True :
         if input_user <= len(echo4) - 1 :
            new_preset.append(echo4[input_user])
            echo_cost.append(4)
            total_cost += 4
            temporary_cost = 4
    
         elif input_user <= len(echo4 + echo3) - 1 :
            new_preset.append(echo3[input_user - len(echo4)])
            echo_cost.append(3)
            total_cost += 3
            temporary_cost = 3
    
         elif input_user <= len(echo4 + echo3 + echo3) - 1 :
            new_preset.append(echo1[input_user - len(echo4 + echo3)])
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
               list_preset.append(new_preset)
               list_cost.append(echo_cost)
               new_preset = []
               echo_cost = []
               total_cost = 0
         #pengecekan sebelum masuk edit
         elif input_user == 50 and len(new_preset) > 0 :
            input_user = int(input("kamu punya preset belum disimplan, tekan 1 untuk menyimpan "))    
            if input_user == 1 :
              list_preset.append(new_preset)
              list_cost.append(echo_cost)
        
              new_preset = []
              echo_cost = []
              total_cost = 0
            else :
              new_preset = []
              echo_cost = []
              total_cost = 0      
            for index, preset in enumerate(list_preset):
             print(f"preset ke {index} : {preset}")    
            modify_preset = int(input("mau edit/hapus preset? 14 untuk edit 15 untuk hapus"))
            break    
         elif input_user == 50 and len(list_preset) < 1 :

            print("kamu belum punya preset untuk dilihat")

         elif input_user == 50 :
            for index, preset in enumerate(list_preset):
               print(f"preset ke {index} : {preset}")    
            modify_preset = int(input("mau edit/hapus preset? 14 untuk edit 15 untuk hapus : "))
            break
         
         else :
          print("input salah")
    
         if total_cost > 12:
            print("cost echo yang kamu masukkan sudah lebih dari 12")
            new_preset.pop()  
            echo_cost.pop()
    
            list_preset.append(new_preset)
            list_cost.append(echo_cost)
            new_preset = []
            echo_cost = []
            total_cost = 0
    
         elif total_cost == 12 :
            print("donee wak udah 12")
            list_preset.append(new_preset)
            list_cost.append(echo_cost)
            new_preset = []
            echo_cost = []
            total_cost = 0
    
         elif len(new_preset) == 5:
            print("echo kamu sudah 5")
            list_preset.append(new_preset)
            list_cost.append(echo_cost)
            new_preset = []
            echo_cost = []
            total_cost = 0
          
         input_user = int(input("masukkan lagi echo yang mau dipilih (tekan 50 untuk melihat preset yang ada atau 21 untuk selesai buat) : "))  
         
        if input_user == 20 :
           break
    
        #masuk edit 
        if modify_preset == 14 :
           while True :

            edit1 = int(input("ingin edit(0),tambah echo preset(1), atau selesai edit(12)? : "))
            # edit dipisah, nambah echo baru ke preset atau ubah echo di preset
            #yang ini nambahin echo
            if edit1 == 1 :
               while True :
                 print("preset yang tersedia slot atau terdapat cost sisa  :")
    
                 for index, preset in enumerate(list_preset):
                    if len(list_preset[index]) == 5 or sum(list_cost[index]) == 12:
                     continue
                    print(f"preset ke {index} : bisa ditambah")

                 edit1 = int(input(f"pilih preset (tekan {len(list_preset) + 1} atau lebih sebanyak dua kali untuk keluar : )"))
    
                 if stop_modify == 1:
                  print("opsi edit berhenti")
                  stop_modify = 0
                  break
                 
                 elif edit1 > len(list_preset) :
                  print("preset tidak ada")
                  stop_modify += 1
    
                 else : 
                    print(f"echo yang dipilih : {list_preset[edit1]}")
    
                    if len(list_preset[edit1]) == 5 :
                       print("penambahan echo tidak valid : slot penuh")
                    elif sum(list_cost[edit1]) == 12 :
                       print("penambahan echo tidak valid : cost penuh")
                    else :
                       edit2 = int(input("pilih echo yang dimasukkan : "))
                       total_cost = sum(list_cost[edit1])
    
                       if edit2 <= len(echo4) -  1:
                          list_preset[edit1].append(echo4[edit2])
                          list_cost[edit1].append(4)
                          total_cost += 4
                          temporary_cost = 4
    
                       elif edit2 <= len(echo4 + echo3) -  1:
                          list_preset[edit1].append(echo3[edit2 - len(echo3)])
                          list_cost[edit1].append(3)
                          total_cost += 3
                          temporary_cost = 3
    
                       elif edit2 <= len(echo4 + echo3 + echo1) -  1:
                          list_preset[edit1].append(echo3[edit2 - len(echo4 + echo3)])
                          list_cost[edit1].append(3)
                          total_cost += 3
                          temporary_cost = 3
    
                       else :
                          print("input salah")
                       
                       if total_cost > 12 :
                          print("echo yang dimasukkan butuh cost lebih")
                          print("gagal menambahkan")
                          list_preset[edit1].pop()
                          list_cost[edit1].pop()
                          total_cost -= temporary_cost
                       else :
                          print("berhasil menambahkan")

           #ini  mode edit 
            elif edit1 == 0 :
               while True :
                 
                 for index, preset in enumerate(list_preset):
                     print(f"preset ke {index} : {preset}")
    
                 edit1 = int(input(f"pilih preset yang ingin di edit (tekan {len(list_preset) + 1} atau lebih sebanyak dua kali untuk berhenti edit) : "))
           
                 if stop_modify == 1:
                    print("opsi edit berhenti")
                    stop_modify = 0
                    break
           
                 elif edit1 > len(list_preset) :
                    print("preset tidak ada")
                    stop_modify += 1
           
                 else :
                    print(f"echo yang dipilih : {list_preset[edit1]}")
                 
                    temp_preset_list = list_preset[edit1][:]
                    temp_cost_list = list_cost[edit1][:]
                    total_cost = sum(list_cost[edit1])    
           
                    edit2 = int(input("edit value yang ke? : "))
    
                    if edit2 > len(list_preset[edit1]) -1 :
                       print("echo tidak ada")
                       continue
    
                    print("echo cost 4 : ")
                    for index,cost4 in enumerate(echo4) :
                        print(f"{index} : {cost4}")
                    
                    print("echo cost 3 : ")
                    for index,cost3 in enumerate(echo3) :
                        print(f"{index + len(echo4)} : {cost3}")
                    
                    print("echo cost 1 : ")
                    for index,cost1 in enumerate(echo1) :
                        print(f"{index + len(echo4 + echo3)} : {cost1}")
              
                    final_edit = int(input(f"ubah {list_preset[edit1][edit2]} jadi? : "))
                   
                    if final_edit > len(echo4 + echo3 + echo1) - 1 :
                      print("input tidak tersedia")    
                      continue
                    
                    elif final_edit <= len(echo4) - 1 :
                       list_preset[edit1][edit2] = echo4[final_edit]
                       total_cost -= list_cost[edit1][edit2]
                       list_cost[edit1][edit2] = 4
                       temporary_cost = 4     
                    elif final_edit <= len(echo4 + echo3) - 1 :
                       list_preset[edit1][edit2] = echo3[final_edit - len(echo4)]
                       total_cost -= list_cost[edit1][edit2]
                       list_cost[edit1][edit2] = 3
                       temporary_cost = 3    
                    elif final_edit <= len(echo4 + echo3 + echo1) - 1 :
                       list_preset[edit1][edit2] = echo1[final_edit - len(echo3 + echo4)]
                       total_cost -= list_cost[edit1][edit2]
                       list_cost[edit1][edit2] = 1
                       temporary_cost = 1
                     
                    
                    total_cost += temporary_cost    
                    if total_cost > 12 :
                       print("error : cost sudah melebihi 12")
                       list_preset[edit1] = temp_preset_list
                       list_cost[edit1] = temp_cost_list
                       
                    else :
                       continue 
    
            elif edit1 == 12 :
               print("edit echo selesai")
               total_cost = 0
               break
            
            else : 
               print("salah pilihan")
        #masuk mode hapus preset
        elif modify_preset == 15 :
          while True :
           
           if len(list_preset) < 1 :
              print("tidak ada preset lagi")
              break
           
           for index, preset in enumerate(list_preset):
             print(f"preset ke {index} : {preset}")
           edit1 = int(input(f"pilih preset yang ingin di hapus (tekan {len(list_preset) + 1} atau lebih dua kali untuk berhenti edit) : "))
           if stop_modify == 1:
              print("opsi hapus berhenti")
              stop_modify = 0
              break
           
           elif edit1 > len(list_preset) - 1 :
             print("preset tidak ada")
             stop_modify += 1
             
           else : 
              print(f"preset yang dipilih : {list_preset[edit1]}")
              edit2 = int(input("yakin ingin hapus preset?(0 untuk ya) :"))

              if edit2 == 0 :
                 list_preset.pop(edit1)
                 list_cost.pop(edit1)
                 print("hapus preset berhasil")

              else :
                 print("cancel penghapusan :")
    
        else :
          print("kamu ga milih keduanya")
          print("echo cost 4 : ")
          for index,cost4 in enumerate(echo4) :
              print(f"{index} : {cost4}")
          
          print("echo cost 3 : ")
          for index,cost3 in enumerate(echo3) :
              print(f"{index + len(echo4)} : {cost3}")
          
          print("echo cost 1 : ")
          for index,cost1 in enumerate(echo1) :
              print(f"{index + len(echo4 + echo3)} : {cost1}")
    
        input_user = int(input("pilih echo berdasarkan nomor, 50 untuk hapus/edit preset, atau 20 jika ingin log out : "))
        print("preset akan otomatis dibuat jika cost sudah 12 atau slot echo sudah 5")
        print("jika total cost preset sudah lebih 12, akan menghapus echo terbaru dan otomatis membuat preset baru")
        if input_user == 20 :
           new_preset = []
           echo_cost = []
           break  
#   role 0 = admin, bisa menambah atau menghapus echo untuk user nanti
  elif role == 0: 
        print("echo cost 4 : ")
        for index,cost4 in enumerate(echo4) :
            print(f"{index} : {cost4}")
        
        print("echo cost 3 : ")
        for index,cost3 in enumerate(echo3) :
            print(f"{index + len(echo4)} : {cost3}")
        
        print("echo cost 1 : ")
        for index,cost1 in enumerate(echo1) :
           print(f"{index + len(echo4 + echo3)} : {cost1}")

        admin_input = int(input("ingin tambah(0) echo, hapus(1) echo, atau log out(20)? : "))
        while admin_input != 20 :
          #opsi admin = nambahkan echo sesuai dengan cost
          if admin_input == 0 :
             while True :  
               admin_input = int(input("tambah echo cost berapa? (tekan 5 untuk jika selesai) : "))

               if admin_input == 5 :
                  ("selesai menambahkan ")
                  break  

               admin_mod = input("masukkan nama echo : ")  
               if admin_input == 4 :
                  echo4.append(admin_mod)
                  print(f"berhasil menambahkan {admin_mod} ke echo cost 4")
                  
               elif admin_input == 3 :
                  echo3.append(admin_mod)
                  print(f"berhasil menambahkan {admin_mod} ke echo cost 3")  
               elif admin_input == 1 :
                  echo1.append(admin_mod)
                  print(f"berhasil menambahkan {admin_mod} ke echo cost 1")
               
               
               else :
                  print(f"echo cost {admin_input} tidak ada ")  
               print("echo cost 4 : ")
               for index,cost4 in enumerate(echo4) :
                   print(f"{index} : {cost4}")
               
               print("echo cost 3 : ")
               for index,cost3 in enumerate(echo3) :
                   print(f"{index + len(echo4)} : {cost3}")
               
               print("echo cost 1 : ")
               for index,cost1 in enumerate(echo1) :
                   print(f"{index + len(echo4 + echo3)} : {cost1}")

          #hapus echo 
          elif admin_input == 1 :
           while True :  
            if len(echo4) < 2 or len(echo3) < 2 or len(echo1) < 2 :
               print("opsi hapus berhenti")
               print("masing masing echo dgn cost berbeda setidaknya punya 1 echo")
               break

            print("echo cost 4 : ")
            for index,cost4 in enumerate(echo4) :
                 print(f"{index} : {cost4}")
             
            print("echo cost 3 : ")
            for index,cost3 in enumerate(echo3) :
                 print(f"{index + len(echo4)} : {cost3}")
             
            print("echo cost 1 : ")
            for index,cost1 in enumerate(echo1) :
                 print(f"{index + len(echo4 + echo3)} : {cost1}")
               
            admin_input= int(input("masukkan nomor yang ingin dihapus (20 untuk selesai) : "))
            
            if admin_input <= len(echo4) -1 :
               echo4.pop(admin_input)  

            elif admin_input <= len(echo4 + echo3) -1 :
               echo3.pop(admin_input - len(echo3))  

            elif admin_input <= len(echo4 + echo3 + echo1) -1 :
               echo1.pop(admin_input - len(echo3 + echo1))  

            elif admin_input == 20 :
               print("selesai hapus echo")
               break  

            else :
               print("input salah")  

          elif admin_input == 20 :
             print("log out admin")
             break
          
          admin_input = int(input("ingin tambah(0) echo, hapus(1) echo, atau log out(20)? : "))  
          
  elif username_input == "out" or username_input == "Out" :
      os.system('cls' if os.name == 'nt' else 'clear')
      break
  
  print("log out..")
  print("ketik out jika ingin keluar")
  username_input = input("masukkan nama :")  
            
          
             
##kayanya berlebihan