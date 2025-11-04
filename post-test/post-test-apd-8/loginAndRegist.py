import os
import time

import variable

def loginn() :
    count_try = 0

    print("[1] untuk login")
    print("[2] untuk regist")
    print("[3] untuk keluar")
    variable.username_input = input("masukkan pilihan :")
    if variable.username_input == "2":
      try :
       variable.username_input = input("masukkan nama baru anda : ")
       if variable.username_input == "" or  variable.username_input == " " * len(variable.username_input):
          raise ValueError("nama tidak boleh kosong atau spasi saja")
      except ValueError as kosong :
         print(kosong)
       
      if variable.username_input in variable.user :
         print("user sudah ada")
      else :
         try :
          password_input = input("masukkan password baru anda : ")
          if password_input == "" or  password_input == " " * len(password_input):
             raise ValueError("password tidak boleh kosong atau spasi saja")
          else :
             variable.user[variable.username_input] = [password_input]
             print(f"selamat datang {variable.username_input}")
         except ValueError as kosong :
            print(kosong) 
            

    elif variable.username_input == "3" :
      print("keluar dari program...")
      time.sleep(2)
      exit()
    elif variable.username_input == "1" :
      while True :

        if count_try == 3 :
            print("terlalu banyak mencoba, silakan coba nanti")
            time.sleep(2)
            exit()  

        variable.username_input = input("masukkan nama anda : ")
        password_input = input("masukkan password anda : ")  

        if variable.username_input in variable.user and (password_input in variable.user[variable.username_input]):
            count_try = 0
            if variable.username_input == "admin" :
                variable.role = 0
                if variable.username_input not in variable.preset_user :
                    variable.preset_user[variable.username_input] = {}
                    variable.cost_preset[variable.username_input] = {}
              
            else :
                print(f"selamat datang {variable.username_input}")
                variable.role = 1
                if variable.username_input not in variable.preset_user :
                    variable.preset_user[variable.username_input] = {}
                    variable.cost_preset[variable.username_input] = {}
            return variable.username_input, variable.role
            
        
        else :
            count_try += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"password/username salah, coba {3 - count_try} kali lagi ")

    else : 
        print("invalid")