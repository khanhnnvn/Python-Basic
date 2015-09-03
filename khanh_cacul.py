choice = raw_input("Moi ban chon phep tinh: 1 Cong, 2 Tru, 3 Nhan, 4 Chia")
x = int(raw_input("x"))
y = int(raw_input("y"))
r = {
'1':lambda x,y: x+y,
'2':lambda x,y: x-y,
'3':lambda x,y: x*y,
'4':lambda x,y: x/y,
}.get(choice, lambda x,y: x+y)(x,y)
print r