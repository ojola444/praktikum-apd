try :
    nama = input("masukkan nama : ")
    if nama == "" or  nama == " " * len(nama):
        raise ValueError("nama tidak boleh kosong atau spasi saja")
except ValueError as takbole :
    print(takbole)
  