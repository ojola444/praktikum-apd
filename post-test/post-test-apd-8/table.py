from prettytable import PrettyTable

preset = {
    "antokeren" : {"preset 1" : [123,2243],
                   "preset 2" : ["keren", "keren"]}
    
}
anto = preset["antokeren"]
table = PrettyTable()
table.field_names = ["nama preset", "isi preset"] 

table.min_width["nama preset"] = 30
table.min_width["isi preset"] = 50

for key, value in anto.items() :
    table.add_row([key, value])
    table.add_row(["-" * 30, "-" * 50 ])

print(table)