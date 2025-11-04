import os
import variable
from variable import echo
from read import listEcho

def buatPreset(preset_siapa, cost_siapa) :
    
    variable.total_cost = 0
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
           variable.new_preset.append(echo["cost4"][input_user])
           variable.echo_cost.append(4)
           variable.total_cost += 4

        elif input_user <= len(echo["cost4"] + echo["cost3"]) - 1 :
           variable.new_preset.append(echo["cost3"][input_user - len(echo["cost3"])])
           variable.echo_cost.append(3)
           variable.total_cost += 3
  
        elif input_user <= len(echo["cost4"] + echo["cost3"] + echo["cost1"]) - 1 :
           variable.new_preset.append(echo["cost1"][input_user - len(echo["cost4"] + echo["cost3"])])
           variable.echo_cost.append(1)
           variable.total_cost += 1
        
        elif input_user == 21:   
         
           if len(variable.new_preset) < 1 and len(variable.echo_cost) < 1:
              os.system('cls' if os.name == 'nt' else 'clear')
              listEcho ()
              print("tidak ada echo yang dimasukkan")    

           else :
              os.system('cls' if os.name == 'nt' else 'clear')
              cost_siapa[f"new preset {len(preset_siapa)}"] = variable.echo_cost
              preset_siapa[f"new preset {len(preset_siapa)}"] = variable.new_preset
              listEcho()
              print("preset dibuat")
              variable.new_preset = []
              variable.echo_cost = []
              variable.total_cost = 0    

        elif input_user == 50 and len(variable.new_preset) > 0 :
           input_user = int(input("kamu punya preset belum disimplan, tekan 1 untuk menyimpan "))    
           if input_user == 1 :
             cost_siapa[f"new preset {len(preset_siapa)}"] = variable.echo_cost
             preset_siapa[f"new preset {len(preset_siapa)}"] = variable.new_preset
    
             variable.new_preset = []
             variable.echo_cost = []
             variable.total_cost = 0
           else :
             variable.new_preset = []
             variable.echo_cost = []
             variable.total_cost = 0 
           os.system('cls' if os.name == 'nt' else 'clear')
           print("buat preset selesai ")
           print("keluar dari opsi...")
           break

        elif input_user == 50 and len(variable.new_preset) == 0 :
           os.system('cls' if os.name == 'nt' else 'clear')
           print("keluar dari opsi...")
           break
        
        else :
         print("input salah")  

        if variable.total_cost > 12:
           os.system('cls' if os.name == 'nt' else 'clear')
           listEcho()
           print("cost echo yang kamu masukkan sudah lebih dari 12")
           variable.new_preset.pop()  
           variable.echo_cost.pop()    
           cost_siapa[f"new preset {len(preset_siapa)}"] = variable.echo_cost
           preset_siapa[f"new preset {len(preset_siapa)}"] = variable.new_preset    
           variable.new_preset = []
           variable.echo_cost = []
           variable.total_cost = 0    

        elif variable.total_cost == 12 :
           os.system('cls' if os.name == 'nt' else 'clear')
           listEcho()
           print("donee wak udah 12")
           cost_siapa[f"new preset {len(preset_siapa)}"] = variable.echo_cost
           preset_siapa[f"new preset {len(preset_siapa)}"] = variable.new_preset   
           variable.new_preset = []
           variable.echo_cost = []
           variable.total_cost = 0    

        elif len(variable.new_preset) == 5:
           os.system('cls' if os.name == 'nt' else 'clear')
           listEcho()
           print("echo kamu sudah 5")
           cost_siapa[f"new preset {len(preset_siapa)}"] = variable.echo_cost
           preset_siapa[f"new preset {len(preset_siapa)}"] = variable.new_preset
           
           variable.new_preset = []
           variable.echo_cost = []
           variable.total_cost = 0
        