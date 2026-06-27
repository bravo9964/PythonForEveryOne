cars = ['tesla','toyota','benz','byd']
for i,c in enumerate(cars,start=1): #enumerate เป็นการเจนเลขขึ้นมา strat เป็นตัวเริ่มต้น
    print(' ลำดับที่ {} {}'.format(i,c)) # c คือ สมาชิกใน cars
# ถึงที่ 1:00:00
# enumerate ฟังก์ชั่นสร้างลำดับเลขขึ้นมา num + generate
# ord สำหรับหาค่าตัวเลขจากตัวอักษร ord('ก')
# chr สำหรับแปลงค่าตัวเลขเป็นตัวอักษร chr(3585)
number = {'1001':'Sayaka','1002':'Tsubasa','1003':'Chisato'}
for n in number.items():#เรียก Index 0
    print(n[0])
for n in number.items():#เรียก Index 1
    print(n[1])
for n in number.items():#เรียกค่าทั้งหมด
    print(n)
for n in number.keys(): #เรียกคีย์
    print(n)
for n in number.values():# เรียกค่า
    print(n)

