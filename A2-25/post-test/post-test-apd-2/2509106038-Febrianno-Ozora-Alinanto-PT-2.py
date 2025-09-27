list = ["0.122", 123, 145.0,True, False ]

print(list)
print("tipe data setiap elemen =")
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[3]))

print("""jumlah data yang bertipe float dan int
int = 1
float = 1
      """)

newlist = [float(list[0]), float(list[1]), int(list[2]), str(list[3]), int(list[4]) ]

print("list baru setelah diubah tipe datanya =")
print(newlist)
print(type(newlist[0]))
print(type(newlist[1]))
print(type(newlist[2]))
print(type(newlist[3]))
print(type(newlist[4]))

print("""jumlah data yang bertipe float dan int
int = 2
float = 2
      """)

