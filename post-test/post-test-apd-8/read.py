from prettytable import PrettyTable
import variable
from variable import echo, preset_user

def listEcho() :

    table = PrettyTable()

    table.field_names = ["No.", "Echo", "Cost"]
    
    nomor_urut = 0
    urutan = ["cost4", "cost3", "cost1"]
    
    for cost_key in urutan:
        cost_value = int(cost_key.replace("cost", "")) 
        echo_list = echo[cost_key]

        table.add_row(["---", f"==== ECHO COST {cost_value} ====", "---"])
    
        for echo_name in echo_list:
        
            table.add_row([
                nomor_urut,         
                echo_name,          
                cost_value
            ])
            nomor_urut += 1

    print(table)


def listPreset(punya_user) :
   table = PrettyTable()
   table.field_names = ["nama preset", "isi preset"]

   for key, value in punya_user.items():
            table.add_row([key, value])

   print(table)


def lihatPreset(preset_siapa) :
   if len(preset_siapa) < 1 :
      print("belum ada preset yang ditampilkan")
   else :
      print(f"kamu punya {len(preset_user[variable.username_input])} preset")
      print("\n")
      listPreset(preset_siapa)

def terpilih(keyMana, isiKey ) :
    table = PrettyTable()
    table.field_names = ["nama preset", "isi preset"]
    table.add_row([keyMana, isiKey])
    
    print("preset yang terpilih :")
    print(table)
