import os
from prettytable import PrettyTable

from read import listEcho, listPreset, terpilih
from variable import echo
def tambahEchoPreset(preset_siapa, cost_siapa) :
    
    stop_modify = 0
    temporary_cost = 0
    count = 0

    if len(preset_siapa) < 1 :
      print("belum ada preset yang ditampilkan")
      return

    while True :

        table = PrettyTable()
        table.field_names = ["nama preset", "status preset"]

        for key in preset_siapa:
           
           if len(preset_siapa[key]) == 5 or sum(cost_siapa[key]) == 12:
              table.add_row([key, "tidak bisa ditambah"])
              count += 1

           else :
              table.add_row([key, "bisa ditambah"])

        print(table)

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
           
           terpilih(edit1, preset_siapa[edit1])

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
    if len(preset_siapa) < 1 :
      print("belum ada preset yang ditampilkan")
      return

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
           terpilih(edit1, preset_siapa[edit1])
        
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
   if len(preset_siapa) < 1 :
      print("belum ada preset yang ditampilkan")
      return
   
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
         terpilih(edit1, preset_siapa[edit1])
         edit2 = input("ubah jadi? : ")
         if edit2 in preset_siapa :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("preset dengan nama yang sama sudah ada")
         else : 
            os.system('cls' if os.name == 'nt' else 'clear')
            preset_siapa[edit2] = preset_siapa.pop(edit1)
            cost_siapa[edit2] = cost_siapa.pop(edit1)
            print("ubah nama berhasil")
